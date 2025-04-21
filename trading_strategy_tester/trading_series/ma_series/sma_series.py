import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.overlap.sma import sma
from trading_strategy_tester.utils.parameter_validations import get_base_sources


class SMA(TradingSeries):
    """
    The SMA (Simple Moving Average) class retrieves the specified price data (e.g., 'Close') for a given ticker
    and applies the SMA calculation based on the specified length and offset.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 9, offset: int = 0):
        """
        Initialize the SMA series with the specified ticker symbol, target column, SMA length, and offset.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param source: The column in the DataFrame on which the SMA is calculated (e.g., 'Close'). Default is 'Close'.
        :type source: SourceType, optional
        :param length: The number of periods over which to calculate the SMA. Default is 9.
        :type length: int, optional
        :param offset: The number of periods by which to shift the SMA. Default is 0.
        :type offset: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the SMA calculation
        self.offset = offset  # Set the offset (number of periods to shift the SMA)
        self.name = f'{self._ticker}_SMA_{self.source}_{self.length}_{self.offset}'  # Define the name for the SMA series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this SMA series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the SMA data series for the specified ticker.

        If the SMA data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the SMA indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the SMA values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the SMA series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the SMA using the specified target column, length, and offset
            sma_series = sma(series=new_df[self.source], length=self.length, offset=self.offset)

            # Add the SMA series to the DataFrame
            df[self.name] = sma_series

        # Return the SMA series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the SMA series.

        :return: The name of the SMA series, formatted with the ticker, source, length, and offset.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the SMA series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'SMA',
            'ticker': self._ticker,
            'source': self.source,
            'length': self.length,
            'offset': self.offset
        }