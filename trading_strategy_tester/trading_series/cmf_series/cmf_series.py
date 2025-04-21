import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volume.cmf import cmf
from trading_strategy_tester.enums.source_enum import SourceType


class CMF(TradingSeries):
    """
    The CMF (Chaikin Money Flow) class retrieves the specified price data (e.g., 'High', 'Low', 'Close')
    and volume data for a given ticker and applies the CMF calculation based on the specified length.

    The Chaikin Money Flow is a technical analysis indicator that measures the buying and selling pressure
    over a specified period.
    """

    def __init__(self, ticker: str, length: int = 20):
        """
        Initialize the CMF series with the specified ticker symbol and CMF length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate the CMF. Default is 20.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for the CMF calculation
        self.name = f'{self._ticker}_CMF_{self.length}'  # Define the name for the CMF series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this CMF series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the CMF data series for the specified ticker.

        If the CMF data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the CMF indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the CMF values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the CMF series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the CMF using the specified high, low, close, volume columns and length
            cmf_series = cmf(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                close=new_df[SourceType.CLOSE.value],
                volume=new_df[SourceType.VOLUME.value],
                length=self.length
            )

            # Add the CMF series to the DataFrame
            df[self.name] = cmf_series

        # Return the CMF series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the CMF series.

        :return: The name of the CMF series, formatted with the ticker and CMF length.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the CMF series to a dictionary representation.

        :return: A dictionary containing the CMF series data.
        :rtype: dict
        """
        return {
            'type': 'CMF',
            'ticker': self._ticker,
            'length': self.length
        }