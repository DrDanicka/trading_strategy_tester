import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.chop import chop


class CHOP(TradingSeries):
    """
    The CHOP class calculates the Choppiness Index for a given ticker symbol.

    The Choppiness Index is a technical analysis indicator that quantifies the market's tendency to trend
    or to consolidate. A high Choppiness Index indicates a choppy, sideways market, while a low value indicates
    a strong trending market.
    """

    def __init__(self, ticker: str, length: int = 14, offset: int = 0):
        """
        Initializes the CHOP series with the specified ticker symbol, length, and offset.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        length : int, optional
            The number of periods over which to calculate the Choppiness Index. Default is 14.

        offset : int, optional
            The number of periods to shift the resulting series. Default is 0.
        """
        super().__init__(ticker)
        self.length = length
        self.offset = offset
        self.name = f'{self._ticker}_CHOP_{self.length}_{self.offset}'

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this CHOP series.

        This property provides access to the ticker symbol that was specified when the CHOP instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the Choppiness Index data series for the specified ticker.

        This method checks if the Choppiness Index for the given ticker and configuration (length, offset)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates
        the Choppiness Index, and adds it to the DataFrame. It returns a pandas Series containing the
        Choppiness Index values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the Choppiness Index does not exist in
            this DataFrame, it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the Choppiness Index values for the specified ticker and configuration,
            labeled with the appropriate name.
        """
        # Check if the CHOP series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the Choppiness Index using the specified high, low, close prices, length, and offset
            chop_series = chop(
                high=new_df['High'],
                low=new_df['Low'],
                close=new_df['Close'],
                length=self.length,
                offset=self.offset
            )

            # Add the Choppiness Index series to the DataFrame
            df[self.name] = chop_series

        # Return the Choppiness Index series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the Choppiness Index series.

        This method returns a string that includes the ticker symbol, length, and offset, which uniquely
        identifies the Choppiness Index series.

        Returns:
        --------
        str
            The name of the Choppiness Index series.
        """
        return self.name