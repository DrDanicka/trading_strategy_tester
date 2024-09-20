import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class CLOSE(TradingSeries):
    """
    The Close class inherits from TradingSeries and provides a specific implementation for retrieving the
    closing prices associated with a given ticker symbol.
    """

    def __init__(self, ticker: str):
        """
        Initializes the Close series with the specified ticker symbol.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        """
        super().__init__(ticker)
        self.name = f'{self._ticker}_Close'

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this Close series.

        This property provides access to the ticker symbol that was specified when the Close instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker


    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves the closing price data series for the specified ticker.

        This method downloads the latest data for the ticker using the provided downloader and extracts the closing
        prices from the downloaded data. It returns a pandas Series containing the closing prices.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame containing existing trading data (this parameter is not used in this method but is required by the interface).

        Returns:
        --------
        pd.Series
            A pandas Series containing the closing prices for the ticker, labeled with the ticker name followed by '_Close'.
        """
        # Download the latest data for the ticker using the downloader
        new_df = downloader.download_ticker(self._ticker)

        # Extract the 'Close' column and return it as a pandas Series
        return pd.Series(new_df['Close'], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name