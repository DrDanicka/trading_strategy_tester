import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class Volume(TradingSeries):
    """
    The Volume class inherits from TradingSeries and provides a specific implementation for retrieving the
    trading volume data associated with a given ticker symbol.
    """

    def __init__(self, ticker: str):
        """
        Initializes the Volume series with the specified ticker symbol.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        """
        super().__init__(ticker)


    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this Volume series.

        This property provides access to the ticker symbol that was specified when the Volume instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker


    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves the volume data series for the specified ticker.

        This method downloads the latest data for the ticker using the provided downloader and extracts the volume
        information from the downloaded data. It returns a pandas Series containing the volume data.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame containing existing trading data (this parameter is not used in this method but is required by the interface).

        Returns:
        --------
        pd.Series
            A pandas Series containing the volume data for the ticker, labeled with the ticker name followed by '_Volume'.
        """
        # Download the latest data for the ticker using the downloader
        new_df = downloader.download_ticker(self._ticker)

        # Extract the 'Volume' column and return it as a pandas Series
        return pd.Series(new_df['Volume'], name=f'{self._ticker}_Volume')