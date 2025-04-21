import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.overlap.ema import ema
from trading_strategy_tester.utils.parameter_validations import get_base_sources


class EMA(TradingSeries):
    """
    The EMA (Exponential Moving Average) class retrieves the specified price data (e.g., 'Close') for a given ticker
    and applies the EMA calculation based on the specified length and offset.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 9, offset: int = 0):
        """
        Initialize the EMA series with the specified ticker symbol, target column, EMA length, and offset.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param source: The column in the DataFrame on which the EMA is calculated (e.g., 'Close'). Default is 'Close'.
        :type source: SourceType, optional
        :param length: The number of periods over which to calculate the EMA. Default is 9.
        :type length: int, optional
        :param offset: The number of periods by which to shift the EMA. Default is 0.
        :type offset: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the EMA calculation
        self.offset = offset  # Set the offset (number of periods to shift the EMA)
        self.name = f'{self._ticker}_EMA_{self.source}_{self.length}_{self.offset}'  # Define the name for the EMA series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this EMA series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the EMA data series for the specified ticker.

        If the EMA data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the EMA indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the EMA values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the EMA series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the EMA using the specified target column, length, and offset
            ema_series = ema(series=new_df[self.source], length=self.length, offset=self.offset)

            # Add the EMA series to the DataFrame
            df[self.name] = ema_series

        # Return the EMA series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the EMA series.

        :return: The name of the EMA series, formatted with the ticker, source, length, and offset.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the EMA series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'EMA',
            'ticker': self._ticker,
            'source': self.source,
            'length': self.length,
            'offset': self.offset
        }