import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.trend.aroon import aroon_down


class AROON_DOWN(TradingSeries):
    """
    The Aroon Down indicator measures the number of periods since the lowest low over a specified period.
    It is used to identify trends and potential reversal points by analyzing the strength of the downtrend.
    """

    def __init__(self, ticker: str, length: int = 14):
        """
        Initializes the Aroon Down series with the specified parameters.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        length : int, optional
            The number of periods over which to calculate the Aroon Down indicator. Default is 14.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for Aroon Down calculation
        self.name = f'{self.ticker}_AROONDOWN_{self.length}'
        # Define the name for the Aroon Down series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this Aroon Down series.

        This property provides access to the ticker symbol that was specified when the AroonDown instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the Aroon Down data series for the specified ticker.

        This method checks if the Aroon Down series for the given ticker and length already exists in the
        provided DataFrame. If it does not exist, it downloads the necessary price data, calculates the Aroon Down
        values, and adds them to the DataFrame. It returns a pandas Series containing the Aroon Down values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest price data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the Aroon Down series does not exist in this DataFrame,
            it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the Aroon Down values for the specified ticker and configuration, labeled with the
            appropriate name.
        """
        # Check if the Aroon Down series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the Aroon Down values using the specified parameters
            aroon_down_series = aroon_down(new_df['Low'], self.length)

            # Add the Aroon Down series to the DataFrame
            df[self.name] = aroon_down_series

        # Return the Aroon Down series as a pandas Series
        return pd.Series(df[self.name], name=self.name)


    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name