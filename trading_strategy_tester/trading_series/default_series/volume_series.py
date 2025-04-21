import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.enums.source_enum import SourceType


class VOLUME(TradingSeries):
    """
    The VOLUME class inherits from TradingSeries and provides a specific implementation for retrieving the
    trading volume data associated with a given ticker symbol.
    """

    def __init__(self, ticker: str):
        """
        Initialize the VOLUME series with the specified ticker symbol.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        """
        super().__init__(ticker)
        self.name = f'{self._ticker}_{SourceType.VOLUME.value}'

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this VOLUME series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve the volume data series for the specified ticker.

        This method downloads the latest data for the ticker using the provided downloader and extracts the volume
        information from the downloaded data.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame containing existing trading data (this parameter is not used in this method but is required by the interface).
        :type df: pd.DataFrame
        :return: A pandas Series containing the volume data for the ticker, labeled with the ticker name followed by '_Volume'.
        :rtype: pd.Series
        """
        # Download the latest data for the ticker using the downloader
        new_df = downloader.download_ticker(self._ticker)

        # Extract the 'Volume' column and return it as a pandas Series
        return pd.Series(new_df[SourceType.VOLUME.value], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the VOLUME series.

        :return: The name of the VOLUME series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the VOLUME series to a dictionary representation.

        :return: A dictionary containing the ticker symbol and its corresponding volume data.
        :rtype: dict
        """
        return {
            'type': 'VOLUME',
            'ticker': self._ticker,
        }