import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.sources import get_source_series
from trading_strategy_tester.indicators.momentum.macd import macd_signal


class MACD_SIGNAL(TradingSeries):
    """
    A class for calculating the Moving Average Convergence Divergence (MACD) Signal line
    for a given ticker symbol. The MACD Signal line is a smoothed moving average of the MACD,
    often used as a trigger for buy/sell signals in technical analysis.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, fast_length: int = 12, slow_length: int = 26,
                 oscillator_ma_type: SmoothingType = SmoothingType.EMA,
                 signal_ma_type: SmoothingType = SmoothingType.EMA, signal_length: int = 9):
        """
        Initialize the MACD_SIGNAL class with specified parameters.

        :param ticker: The ticker symbol of the asset for which the MACD Signal line will be calculated.
        :type ticker: str
        :param source: The source data type used in the MACD Signal line calculation (e.g., closing price).
        :type source: SourceType, optional
        :param fast_length: The period for the fast moving average in MACD. Default is 12.
        :type fast_length: int, optional
        :param slow_length: The period for the slow moving average in MACD. Default is 26.
        :type slow_length: int, optional
        :param oscillator_ma_type: The type of moving average for MACD. Default is SmoothingType.EMA.
        :type oscillator_ma_type: SmoothingType, optional
        :param signal_ma_type: The type of moving average for the signal line calculation. Default is SmoothingType.EMA.
        :type signal_ma_type: SmoothingType, optional
        :param signal_length: The period of the moving average applied to the MACD to create the signal line. Default is 9.
        :type signal_length: int, optional
        """
        super().__init__(ticker)
        self.source = source
        self.fast_length = fast_length
        self.slow_length = slow_length
        self.oscillator_ma_type = oscillator_ma_type
        self.signal_ma_type = signal_ma_type
        self.signal_length = signal_length
        # Define the name of the MACD Signal series with relevant parameters for easy identification
        self.name = f'{self._ticker}_MACD-SIGNAL_{self.fast_length}_{self.slow_length}_{self.oscillator_ma_type.value}_{self.signal_ma_type.value}_{self.signal_length}'

    @property
    def ticker(self) -> str:
        """
        Retrieve the ticker symbol of the asset associated with this MACD Signal instance.

        :return: The ticker symbol for this MACD Signal instance.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Generate the MACD Signal data series for the specified ticker. If the series does not exist
        in the provided DataFrame, download the price data and calculate the MACD Signal.

        :param downloader: The download module to fetch the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame where the MACD Signal series will be added if absent.
        :type df: pd.DataFrame
        :return: A pandas Series containing the calculated MACD Signal values, indexed by date.
        :rtype: pd.Series
        """
        # If MACD Signal is not already in the DataFrame, calculate and add it
        if self.name not in df.columns:
            # Download the historical price data for the given ticker
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the MACD Signal series using the specified parameters
            macd_signal_series = macd_signal(
                series=get_source_series(new_df, source=self.source),
                fast_length=self.fast_length,
                slow_length=self.slow_length,
                oscillator_ma_type=self.oscillator_ma_type,
                signal_ma_type=self.signal_ma_type,
                signal_length=self.signal_length
            )

            # Add the calculated MACD Signal series to the DataFrame
            df[self.name] = macd_signal_series

        # Return the MACD Signal series as a pandas Series with appropriate naming
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Retrieve the name of the MACD Signal series, which includes ticker and parameter details.

        :return: A string representing the MACD Signal series name for this instance.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the MACD_SIGNAL signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'MACD_SIGNAL',
            'ticker': self._ticker,
            'source': self.source,
            'fast_length': self.fast_length,
            'slow_length': self.slow_length,
            'oscillator_ma_type': self.oscillator_ma_type,
            'signal_ma_type': self.signal_ma_type,
            'signal_length': self.signal_length
        }