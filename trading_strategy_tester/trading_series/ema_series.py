import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.ema import ema


class EMA(TradingSeries):
    """
    The EMA class retrieves the specified price data (e.g., 'Close') for a given ticker and applies the Exponential
    Moving Average (EMA) calculation based on the specified length and offset.
    """

    def __init__(self, ticker: str, target: str = 'Close', length: int = 9, offset: int = 0):
        """
        Initializes the EMA series with the specified ticker symbol, target column, EMA length, and offset.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        target : str, optional
            The column in the DataFrame on which the EMA is calculated (e.g., 'Close'). Default is 'Close'.

        length : int, optional
            The number of periods over which to calculate the EMA. Default is 9.

        offset : int, optional
            The number of periods by which to shift the EMA. Default is 0.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.target = target  # Set the target column for the EMA calculation
        self.length = length  # Set the length (number of periods) for the EMA calculation
        self.offset = offset  # Set the offset (number of periods to shift the EMA)
        self.name = f'{self._ticker}_EMA_{self.target}_{self.length}_{self.offset}'  # Define the name for the EMA series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this EMA series.

        This property provides access to the ticker symbol that was specified when the EMA instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the EMA data series for the specified ticker.

        This method checks if the EMA for the given ticker and configuration (target, length, offset) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the EMA, and adds it to
        the DataFrame. It returns a pandas Series containing the EMA values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the EMA does not exist in this DataFrame, it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the EMA values for the specified ticker and configuration, labeled with the appropriate name.
        """
        # Check if the EMA series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the EMA using the specified target column, length, and offset
            ema_series = ema(series=new_df[self.target], length=self.length, offset=self.offset)

            # Add the EMA series to the DataFrame
            df[self.name] = ema_series

        # Return the EMA series as a pandas Series
        return pd.Series(df[self.name], name=self.name)
