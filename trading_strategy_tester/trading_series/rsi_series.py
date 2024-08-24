import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.rsi import rsi


class RSI(TradingSeries):
    """
    The RSI class retrieves the specified price data (e.g., 'Close') for a given ticker and applies the RSI
    calculation based on the specified length.
    """

    def __init__(self, ticker: str, target: str = 'Close', length: int = 14):
        """
        Initializes the RSI series with the specified ticker symbol, target column, and RSI length.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        target : str, optional
            The column in the DataFrame on which the RSI is calculated (e.g., 'Close'). Default is 'Close'.

        length : int, optional
            The number of periods over which to calculate the RSI. Default is 14.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.target = target  # Set the target column for the RSI calculation
        self.length = length  # Set the length (number of periods) for the RSI calculation
        self.name = f'{self._ticker}_RSI_{self.target}_{self.length}'  # Define the name for the RSI series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this RSI series.

        This property provides access to the ticker symbol that was specified when the RSI instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the RSI data series for the specified ticker.

        This method checks if the RSI for the given ticker and configuration (target, length) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the RSI, and adds it to
        the DataFrame. It returns a pandas Series containing the RSI values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the RSI does not exist in this DataFrame, it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the RSI values for the specified ticker and configuration, labeled with the appropriate name.
        """
        # Check if the RSI series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the RSI using the specified target column and length
            rsi_series = rsi(series=new_df[self.target], length=self.length)

            # Add the RSI series to the DataFrame
            df[self.name] = rsi_series

        # Return the RSI series as a pandas Series
        return pd.Series(df[self.name], name=self.name)
