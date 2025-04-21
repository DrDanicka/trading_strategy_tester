import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.momentum.trix import trix

class TRIX(TradingSeries):
    """
    The TRIX class retrieves the specified price data (e.g., 'Close') for a given ticker and applies the TRIX
    (Triple Exponential Average) calculation based on a specified length.
    """

    def __init__(self, ticker: str, length: int = 18):
        """
        Initialize the TRIX series with the specified ticker symbol and TRIX length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate each EMA for the TRIX calculation. Default is 18.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for the TRIX calculation
        self.name = f'{ticker}_TRIX_{length}'  # Define the name for the TRIX series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this TRIX series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the TRIX data series for the specified ticker.

        This method checks if the TRIX for the given ticker and configuration (length) already exists in the provided
        DataFrame. If it does not exist, it downloads the data, calculates TRIX, and adds it to the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the TRIX does not exist in this DataFrame,
        it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the TRIX values for the specified ticker and configuration, labeled with the appropriate name.
        :rtype: pd.Series
        """

        # Check if the TRIX series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the TRIX using the specified length
            trix_series = trix(close=new_df[SourceType.CLOSE.value], length=self.length)

            # Add the TRIX series to the DataFrame
            df[self.name] = trix_series

        # Return the TRIX series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the TRIX series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name


    def to_dict(self) -> dict:
        """
        Convert the TRIX signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'TRIX',
            'ticker': self._ticker,
            'length': self.length,
        }