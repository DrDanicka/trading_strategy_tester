import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.indicators.volume.chaikin_osc import chaikin_osc
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.enums.source_enum import SourceType


class CHAIKIN_OSC(TradingSeries):
    """
    The CHAIKIN_OSC class represents the Chaikin Oscillator, a volume-based indicator that measures the
    accumulation/distribution of an asset over a specified period.

    It calculates the difference between fast and slow Exponential Moving Averages (EMAs) of the
    Accumulation/Distribution Line.
    """

    def __init__(self, ticker: str, fast_length: int = 3, slow_length: int = 10):
        """
        Initialize the CHAIKIN_OSC class with the specified ticker, fast EMA length, and slow EMA length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param fast_length: The period for the fast EMA in the Chaikin Oscillator calculation.
        :type fast_length: int
        :param slow_length: The period for the slow EMA in the Chaikin Oscillator calculation.
        :type slow_length: int
        """
        super().__init__(ticker)
        self.fast_length = fast_length  # Set the period for the fast EMA
        self.slow_length = slow_length  # Set the period for the slow EMA
        self.name = f'{self._ticker}_CHAIKINOSC_{self.fast_length}_{self.slow_length}'  # Define the name for the Chaikin Oscillator series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this Chaikin Oscillator series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Chaikin Oscillator series for the specified ticker.

        If the Chaikin Oscillator data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the Chaikin Oscillator indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the Chaikin Oscillator values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the Chaikin Oscillator series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self.ticker)
            # Calculate the Chaikin Oscillator using the specified parameters
            chaikin_osc_series = chaikin_osc(
                high=df[SourceType.HIGH.value],
                low=df[SourceType.LOW.value],
                close=df[SourceType.CLOSE.value],
                volume=df[SourceType.VOLUME.value],
                fast_length=self.fast_length,
                slow_length=self.slow_length
            )

            # Add the Chaikin Oscillator series to the DataFrame
            df[self.name] = chaikin_osc_series

        # Return the Chaikin Oscillator series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the Chaikin Oscillator series.

        :return: The name of the Chaikin Oscillator series, formatted with the ticker, fast length, and slow length.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the Chaikin Oscillator series to a dictionary representation.

        :return: A dictionary representation of the Chaikin Oscillator series.
        :rtype: dict
        """
        return {
            'type': 'CHAIKIN_OSC',
            'ticker': self._ticker,
            'fast_length': self.fast_length,
            'slow_length': self.slow_length
        }