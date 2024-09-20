import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.trend.aroon import aroon_up


class AROON_UP(TradingSeries):
    """
    The Aroon Up indicator measures the number of periods since the highest high over a specified period.
    It is used to identify trends and potential reversal points by analyzing the strength of the uptrend.
    """

    def __init__(self, ticker: str, length: int = 14):
        """
        Initializes the Aroon Up series with the specified parameters.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        length : int, optional
            The number of periods over which to calculate the Aroon Up indicator. Default is 14.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for Aroon Up calculation
        self.name = f'{self._ticker}_AROONUP_{self.length}'
        # Define the name for the Aroon Up series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this Aroon Up series.

        This property provides access to the ticker symbol that was specified when the AroonUp instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the Aroon Up data series for the specified ticker.

        This method checks if the Aroon Up series for the given ticker and length already exists in the
        provided DataFrame. If it does not exist, it downloads the necessary price data, calculates the Aroon Up
        values, and adds them to the DataFrame. It returns a pandas Series containing the Aroon Up values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest price data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the Aroon Up series does not exist in this DataFrame,
            it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the Aroon Up values for the specified ticker and configuration, labeled with the
            appropriate name.
        """
        # Check if the Aroon Up series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the Aroon Up values using the specified parameters
            aroon_up_series = aroon_up(new_df['High'], self.length)

            # Add the Aroon Up series to the DataFrame
            df[self.name] = aroon_up_series

        # Return the Aroon Up series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name