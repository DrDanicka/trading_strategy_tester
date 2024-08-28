import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.cmf import cmf

class CMF(TradingSeries):
    """
    The CMF class retrieves the specified price data (e.g., 'High', 'Low', 'Close') and volume data for a given ticker
    and applies the Chaikin Money Flow (CMF) calculation based on the specified length.

    The Chaikin Money Flow is a technical analysis indicator that measures the buying and selling pressure
    over a specified period.
    """

    def __init__(self, ticker: str, length: int = 20):
        """
        Initializes the CMF series with the specified ticker symbol and CMF length.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        length : int, optional
            The number of periods over which to calculate the CMF. Default is 20.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for the CMF calculation
        self.name = f'{self._ticker}_CMF_{self.length}'  # Define the name for the CMF series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this CMF series.

        This property provides access to the ticker symbol that was specified when the CMF instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the CMF data series for the specified ticker.

        This method checks if the CMF for the given ticker and configuration (length) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the CMF, and adds it to
        the DataFrame. It returns a pandas Series containing the CMF values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the CMF does not exist in this DataFrame, it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the CMF values for the specified ticker and configuration, labeled with the appropriate name.
        """
        # Check if the CMF series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the CMF using the specified high, low, close, volume columns and length
            cmf_series = cmf(
                high=new_df['High'],
                low=new_df['Low'],
                close=new_df['Close'],
                volume=new_df['Volume'],
                length=self.length
            )

            # Add the CMF series to the DataFrame
            df[self.name] = cmf_series

        # Return the CMF series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series.

        This method provides the name that identifies the CMF series, which is based on the ticker symbol and the CMF length.

        Returns:
        --------
        str
            The name of the CMF series.
        """
        return self.name
