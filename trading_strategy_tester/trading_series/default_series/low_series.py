import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.enums.source_enum import SourceType

class LOW(TradingSeries):
    """
    The LOW class inherits from TradingSeries and provides a specific implementation for retrieving the
    lowest prices (daily lows) associated with a given ticker symbol.
    """

    def __init__(self, ticker: str):
        """
        Initialize the LOW series with the specified ticker symbol.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.name = f'{self._ticker}_{SourceType.LOW.value}'

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this LOW series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve the lowest price (daily low) data series for the specified ticker.

        This method downloads the latest data for the ticker using the provided downloader and extracts the daily
        low prices from the downloaded data.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame containing existing trading data (this parameter is not used in this method but is required by the interface).
        :type df: pd.DataFrame
        :return: A pandas Series containing the daily low prices for the ticker, labeled with the ticker name followed by '_Low'.
        :rtype: pd.Series
        """
        # Download the latest data for the ticker using the downloader
        new_df = downloader.download_ticker(self._ticker)

        # Extract the 'Low' column and return it as a pandas Series
        return pd.Series(new_df[SourceType.LOW.value], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the LOW series.

        :return: The name of the LOW series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the LOW series to a dictionary representation.

        :return: A dictionary containing the name of the LOW series.
        :rtype: dict
        """
        return {
            'type': 'LOW',
            'ticker': self._ticker
        }