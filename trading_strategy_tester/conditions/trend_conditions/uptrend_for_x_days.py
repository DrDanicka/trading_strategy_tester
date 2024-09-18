import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class UptrendForXDaysCondition(Condition):
    def __init__(self, series: TradingSeries, number_of_days: int):
        self.series = series
        self.number_of_days = number_of_days

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        series : pd.Series = self.series.get_data(downloader, df)

        is_uptrend = series.rolling(window=self.number_of_days).apply(
            lambda x: (x.diff().fillna(0) >= 0).all(), raw=False
        )
        is_uptrend = is_uptrend.fillna(0).astype(bool)
        is_uptrend.name = None

        signal_series = is_uptrend.apply(
            lambda x: f'UptrendForXDaysSignal({self.number_of_days}, {self.series.get_name()})' if x else None
        )

        return is_uptrend, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        # TODO ploting

        return None

    def to_string(self) -> str:
        return f'UptrendForXDaysCondition({self.number_of_days}, {self.series.get_name()})'