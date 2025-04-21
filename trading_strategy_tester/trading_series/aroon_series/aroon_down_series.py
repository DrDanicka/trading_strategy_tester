import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.trend.aroon import aroon_down
from trading_strategy_tester.enums.source_enum import SourceType

class AROON_DOWN(TradingSeries):
    """
    The Aroon Down indicator measures the number of periods since the lowest low over a specified period.
    It is used to identify trends and potential reversal points by analyzing the strength of the downtrend.
    """

    def __init__(self, ticker: str, length: int = 14):
        """
        Initialize the Aroon Down series with the specified parameters.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate the Aroon Down indicator. Default is 14.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for Aroon Down calculation
        self.name = f'{self.ticker}_AROONDOWN_{self.length}' # Define the name for the Aroon Down series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this Aroon Down series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Aroon Down data series for the specified ticker.

        If the Aroon Down data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the Aroon Down indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the Aroon Down values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the Aroon Down series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the Aroon Down values using the specified parameters
            aroon_down_series = aroon_down(new_df[SourceType.LOW.value], self.length)

            # Add the Aroon Down series to the DataFrame
            df[self.name] = aroon_down_series

        # Return the Aroon Down series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the Aroon Down indicator.

        :return: The name of the Aroon Down indicator, formatted with the ticker and configuration.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the Aroon Down series to a dictionary representation.

        :return: A dictionary representation of the Aroon Down series.
        :rtype: dict
        """
        return {
            'type': 'AROON_DOWN',
            'ticker': self._ticker,
            'length': self.length
        }