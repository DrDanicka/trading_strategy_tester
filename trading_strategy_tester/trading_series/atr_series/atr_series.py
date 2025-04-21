import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volatility.atr import atr
from trading_strategy_tester.enums.source_enum import SourceType


class ATR(TradingSeries):
    """
    The ATR (Average True Range) class retrieves the high, low, and close price data for a given ticker
    and computes the ATR based on the specified parameters. ATR is used to measure market volatility.
    """

    def __init__(self, ticker: str, length: int = 14, smoothing_type: SmoothingType = SmoothingType.RMA):
        """
        Initialize the ATR series with the specified parameters.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate the ATR. Default is 14.
        :type length: int, optional
        :param smoothing_type: The type of smoothing method used in ATR calculation (e.g., RMA).
                          Default is SmoothingType.RMA.
        :type smoothing_type: SmoothingType, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for ATR calculation
        self.smoothing = smoothing_type  # Set the smoothing method for ATR calculation
        self.name = f'{self._ticker}_ATR_{self.length}_{self.smoothing.value}'
        # Define the name for the ATR series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this ATR series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Average True Range (ATR) data series for the specified ticker.

        If the ATR data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the ATR indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the ATR values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the ATR series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the ATR using the specified parameters
            atr_series = atr(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                close=new_df[SourceType.CLOSE.value],
                length=self.length,
                smoothing=self.smoothing
            )

            # Add the ATR series to the DataFrame
            df[self.name] = atr_series

        # Return the ATR series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the ATR indicator.

        :return: The name of the ATR indicator, formatted with the ticker and configuration.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the ATR series to a dictionary representation.

        :return: A dictionary representation of the ATR series.
        :rtype: dict
        """
        return {
            'type': 'ATR',
            'ticker': self._ticker,
            'length': self.length,
            'smoothing_type': self.smoothing
        }