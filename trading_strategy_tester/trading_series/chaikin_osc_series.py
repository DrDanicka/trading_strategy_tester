import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.indicators.chaikin_osc import chaikin_osc
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class CHAIKIN_OSC(TradingSeries):
    """
    ChaikinOsc class represents the Chaikin Oscillator, a volume-based indicator that measures the accumulation/distribution
    of an asset over a specified period.

    It calculates the difference between fast and slow Exponential Moving Averages (EMAs) of the Accumulation/Distribution Line.
    """

    def __init__(self, ticker: str, fast_length: int, slow_length: int):
        """
        Initializes the ChaikinOsc class with the specified ticker, fast and slow EMA lengths.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        fast_length : int
            The period for the fast EMA in the Chaikin Oscillator calculation.

        slow_length : int
            The period for the slow EMA in the Chaikin Oscillator calculation.
        """
        super().__init__(ticker)
        self.fast_length = fast_length  # Set the period for the fast EMA
        self.slow_length = slow_length  # Set the period for the slow EMA
        self.name = f'{self._ticker}_CHAIKINOSC_{self.fast_length}_{self.slow_length}'  # Define the name for the Chaikin Oscillator series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this ChaikinOsc series.

        This property provides access to the ticker symbol that was specified when the ChaikinOsc instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the Chaikin Oscillator series for the specified ticker.

        This method checks if the Chaikin Oscillator for the given ticker and configuration (fast and slow lengths)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates the Chaikin Oscillator,
        and adds it to the DataFrame. It returns a pandas Series containing the Chaikin Oscillator values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the Chaikin Oscillator does not exist in this DataFrame,
            it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the Chaikin Oscillator values for the specified ticker and configuration, labeled with the appropriate name.
        """
        # Check if the Chaikin Oscillator series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self.ticker)
            # Calculate the Chaikin Oscillator using the specified parameters
            chaikin_osc_series = chaikin_osc(
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                volume=df['Volume'],
                fast_length=self.fast_length,
                slow_length=self.slow_length
            )

            # Add the Chaikin Oscillator series to the DataFrame
            df[self.name] = chaikin_osc_series

        # Return the Chaikin Oscillator series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series.

        This method provides the unique name of the Chaikin Oscillator series based on the ticker, fast length, and slow length.

        Returns:
        --------
        str
            The name of the Chaikin Oscillator series.
        """
        return self.name
