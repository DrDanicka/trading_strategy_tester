import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.downtrend_plot import DowntrendPlot
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class DowntrendForXDaysCondition(Condition):
    def __init__(self, series: TradingSeries, number_of_days: int):
        self.series = series
        self.number_of_days = number_of_days

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        series : pd.Series = self.series.get_data(downloader, df)

        is_downtrend = series.rolling(window=self.number_of_days).apply(
            lambda x: (x.diff().fillna(0) <= 0).all(), raw=False
        )
        is_downtrend = is_downtrend.fillna(0).astype(bool)
        is_downtrend.name = None

        signal_series = is_downtrend.apply(
            lambda x: f'DowntrendForXDaysSignal({self.number_of_days}, {self.series.get_name()})' if x else None
        )

        return is_downtrend, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        return [DowntrendPlot(
            self.series.get_data(downloader, df),
            self.number_of_days
        )]

    def to_string(self) -> str:
        return f'DowntrendForXDaysCondition({self.number_of_days}, {self.series.get_name()})'