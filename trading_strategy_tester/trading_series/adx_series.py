import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.adx import adx


class ADX(TradingSeries):
    """
    The ADX indicator is used to quantify the strength of a trend, whether it is an uptrend or downtrend.
    It is derived from the Directional Indicators (DI) and is commonly used in trend-following strategies.
    """

    def __init__(self, ticker: str, adx_smoothing: int = 14, DI_length: int = 14):
        """
        Initializes the ADX indicator with the specified parameters.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        adx_smoothing : int, optional
            The smoothing period used in the ADX calculation. Default is 14.

        DI_length : int, optional
            The period length for calculating the Directional Indicators (DI). Default is 14.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.adx_smoothing = adx_smoothing  # Set the ADX smoothing period
        self.DI_length = DI_length  # Set the period length for Directional Indicators
        self.name = f'{self._ticker}_ADX_{self.adx_smoothing}_{self.DI_length}'
        # Define the name for the ADX series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this ADX indicator.

        This property provides access to the ticker symbol that was specified when the ADX instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the ADX data series for the specified ticker.

        This method checks if the ADX series for the given ticker and parameters already exists in the
        provided DataFrame. If it does not exist, it downloads the necessary price data, calculates the ADX
        values, and adds them to the DataFrame. It returns a pandas Series containing the ADX values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest price data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the ADX series does not exist in this DataFrame,
            it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the ADX values for the specified ticker and configuration, labeled with the
            appropriate name.
        """
        # Check if the ADX series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the ADX values using the specified parameters
            adx_series = adx(
                high=new_df['High'],
                low=new_df['Low'],
                close=new_df['Close'],
                adx_smoothing=self.adx_smoothing,
                di_length=self.DI_length
            )

            # Add the ADX series to the DataFrame
            df[self.name] = adx_series

        # Return the ADX series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name