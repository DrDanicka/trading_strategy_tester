import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.willr import willr
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.sources import get_source_series


class WILLR(TradingSeries):
    """
    The WILLR class retrieves the specified price data (e.g., 'Close', 'High', 'Low') for a given ticker
    and applies the Williams %R calculation based on the specified length.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 14):
        """
        Initialize the Williams %R series with the specified ticker symbol, target column, and calculation length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param source: The column in the DataFrame on which the Williams %R is calculated (e.g., 'Close'). Default is 'Close'.
        :type source: SourceType, optional
        :param length: The number of periods over which to calculate Williams %R. Default is 14.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.source = source  # Store the source type (e.g., Close, High, Low)
        self.length = length  # Set the length (number of periods) for the Williams %R calculation
        self.name = f'{self.ticker}_WILLR_{self.source.value}_{self.length}'  # Define the name for the series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this Williams %R series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Williams %R data series for the specified ticker.

        This method checks if the Williams %R for the given ticker and configuration (target, length) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the Williams %R, and adds it to
        the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the Williams %R does not exist in this DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the Williams %R values for the specified ticker and configuration, labeled with the appropriate name.
        :rtype: pd.Series
        """
        # Check if the Williams %R series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the Williams %R using the specified high, low, and source column
            willr_series = willr(
                source=get_source_series(new_df, self.source),
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                length=self.length
            )

            # Add the Williams %R series to the DataFrame
            df[self.name] = willr_series

        # Return the Williams %R series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the Williams %R series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the WILLR signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'WILLR',
            'ticker': self._ticker,
            'source': self.source,
            'length': self.length
        }