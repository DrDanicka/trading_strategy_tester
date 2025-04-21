import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.sources import get_source_series
from trading_strategy_tester.indicators.momentum.cci import cci

class CCI_SMOOTHENED(TradingSeries):
    """
    A class to represent the smoothened Commodity Channel Index (CCI) for a given financial instrument.

    The smoothened Commodity Channel Index (CCI) is a technical indicator that combines the CCI with a
    smoothing function to reduce market noise and provide clearer trend signals. This class extends
    the TradingSeries class and uses historical data to compute the smoothened CCI values.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.HLC3, length: int = 20,
                 smoothing_type: SmoothingType = SmoothingType.SMA, smoothing_length: int = 5):
        """
        Initialize the CCISmoothened class with a ticker, source, length, smoothing type, and smoothing length.

        :param ticker: The ticker symbol of the financial instrument.
        :type ticker: str
        :param source: The price source used for the CCI calculation. Default is HLC3 (High-Low-Close average).
        :type source: SourceType, optional
        :param length: The number of periods to use for the CCI calculation. Default is 20.
        :type length: int, optional
        :param smoothing_type: The type of smoothing to apply to the CCI calculation. Default is SmoothingType.SMA.
        :type smoothing_type: SmoothingType, optional
        :param smoothing_length: The number of periods for the smoothing calculation. Default is 5.
        :type smoothing_length: int, optional
        """
        super().__init__(ticker)
        self.source = source
        self.length = length
        self.smoothing_type = smoothing_type
        self.smoothing_length = smoothing_length
        self.name = f'{self.ticker}_CCISmoothened_{self.source.value}_{self.length}_{self.smoothing_type.value}_{self.smoothing_length}'

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol of the financial instrument.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve and calculate the smoothened CCI data for the financial instrument.

        Downloads the necessary historical data, computes the smoothened CCI values,
        and returns them as a pandas Series. If the smoothened CCI data is already present
        in the provided DataFrame, it uses the existing data.

        :param downloader: The module responsible for downloading historical data.
        :type downloader: DownloadModule
        :param df: The DataFrame containing the existing data.
        :type df: pd.DataFrame
        :return: A pandas Series containing the calculated smoothened CCI values.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            new_df = downloader.download_ticker(self._ticker)
            source_series = get_source_series(new_df, self.source)
            cci_series = cci(source_series, length=self.length, smoothing_type=self.smoothing_type,
                             smoothing_length=self.smoothing_length)

            df[self.name] = cci_series

        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the smoothened CCI series.

        :return: The name of the smoothened CCI series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the smoothened CCI series to a dictionary representation.

        :return: A dictionary representation of the smoothened CCI series.
        :rtype: dict
        """
        return {
            'type': 'CCISmoothened',
            'ticker': self._ticker,
            'source': self.source.value,
            'length': self.length,
            'smoothing_type': self.smoothing_type.value,
            'smoothing_length': self.smoothing_length
        }