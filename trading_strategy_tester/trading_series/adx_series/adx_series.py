import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.trend.adx import adx
from trading_strategy_tester.enums.source_enum import SourceType


class ADX(TradingSeries):
    """
    The ADX (Average Directional Index) indicator is used to quantify the strength of a trend,
    whether it is an uptrend or downtrend. It is derived from the Directional Indicators (DI) and
    is commonly used in trend-following strategies.
    """

    def __init__(self, ticker: str, smoothing_length: int = 14, length: int = 14):
        """
        Initialize the ADX indicator with the specified parameters.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param smoothing_length: The smoothing period used in the ADX calculation. Default is 14.
        :type smoothing_length: int, optional
        :param length: The period length for calculating the Directional Indicators (DI). Default is 14.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.adx_smoothing = smoothing_length  # Set the ADX smoothing period
        self.DI_length = length  # Set the period length for Directional Indicators
        self.name = f'{self._ticker}_ADX_{self.adx_smoothing}_{self.DI_length}'
        # Define the name for the ADX series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this ADX indicator.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the ADX data series for the specified ticker.

        If the ADX data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the ADX indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the ADX values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the ADX series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the ADX values using the specified parameters
            adx_series = adx(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                close=new_df[SourceType.CLOSE.value],
                adx_smoothing=self.adx_smoothing,
                di_length=self.DI_length
            )

            # Add the ADX series to the DataFrame
            df[self.name] = adx_series

        # Return the ADX series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the ADX indicator.

        :return: The name of the ADX indicator, formatted with the ticker and configuration.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the ADX indicator to a dictionary representation.

        :return: A dictionary representation of the ADX indicator.
        :rtype: dict
        """
        return {
            "type": "ADX",
            "ticker": self._ticker,
            "smoothing_length": self.adx_smoothing,
            "length": self.DI_length
        }
