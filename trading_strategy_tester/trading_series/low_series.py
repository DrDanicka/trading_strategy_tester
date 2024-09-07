import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class LOW(TradingSeries):
    """
    The Low class inherits from TradingSeries and provides a specific implementation for retrieving the
    lowest prices (daily lows) associated with a given ticker symbol.
    """

    def __init__(self, ticker: str):
        """
        Initializes the Low series with the specified ticker symbol.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.name = f'{self._ticker}_Low'

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this Low series.

        This property provides access to the ticker symbol that was specified when the Low instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves the lowest price (daily low) data series for the specified ticker.

        This method downloads the latest data for the ticker using the provided downloader and extracts the daily
        low prices from the downloaded data. It returns a pandas Series containing the daily low prices.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame containing existing trading data (this parameter is not used in this method but is required by the interface).

        Returns:
        --------
        pd.Series
            A pandas Series containing the daily low prices for the ticker, labeled with the ticker name followed by '_Low'.
        """
        # Download the latest data for the ticker using the downloader
        new_df = downloader.download_ticker(self._ticker)

        # Extract the 'Low' column and return it as a pandas Series
        return pd.Series(new_df['Low'], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name