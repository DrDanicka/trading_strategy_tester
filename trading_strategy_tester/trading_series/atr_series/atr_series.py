import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volatility.atr import atr


class ATR(TradingSeries):
    """
    The ATR class retrieves the high, low, and close price data for a given ticker and computes the ATR based on the
    specified parameters. ATR is used to measure market volatility.
    """

    def __init__(self, ticker: str, length: int = 14, smoothing: SmoothingType = SmoothingType.RMA):
        """
        Initializes the ATR series with the specified parameters.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        length : int, optional
            The number of periods over which to calculate the ATR. Default is 14.

        smoothing : SmoothingType, optional
            The type of smoothing method used in ATR calculation (e.g., RMA). Default is SmoothingType.RMA.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for ATR calculation
        self.smoothing = smoothing  # Set the smoothing method for ATR calculation
        self.name = f'{self._ticker}_ATR_{self.length}_{self.smoothing.value}'
        # Define the name for the ATR series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this ATR series.

        This property provides access to the ticker symbol that was specified when the ATR instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the Average True Range (ATR) data series for the specified ticker.

        This method checks if the ATR for the given ticker and configuration (length, smoothing) already exists in the
        provided DataFrame. If it does not exist, it downloads the necessary price data, calculates the ATR, and adds it
        to the DataFrame. It returns a pandas Series containing the ATR values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest price data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the ATR does not exist in this DataFrame, it will be
            calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the ATR values for the specified ticker and configuration, labeled with the
            appropriate name.
        """
        # Check if the ATR series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the ATR using the specified parameters
            atr_series = atr(high=new_df['High'], low=new_df['Low'], close=new_df['Close'],
                             length=self.length, smoothing=self.smoothing)

            # Add the ATR series to the DataFrame
            df[self.name] = atr_series

        # Return the ATR series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name