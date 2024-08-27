import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class AfterXDaysCondition(Condition):
    def __init__(self, condition: Condition, number_of_days: int):
        self.condition = condition
        self.number_of_days = number_of_days

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        after_x_days, signal_series = self.condition.evaluate(downloader, df)

        after_x_days = pd.Series(after_x_days.shift(self.number_of_days).fillna(False))
        after_x_days.name = None

        signal_series = pd.Series(signal_series.shift(self.number_of_days))
        signal_series.name = None
        signal_series = signal_series.apply(lambda x: f'AfterXDaysSignal({self.number_of_days}, {x})' if x is not None else None)

        return after_x_days, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = self.condition.get_graphs(downloader, df)

        # TODO shift graphs

        return graphs

    def to_string(self):
        return f'AfterXDaysCondition({self.number_of_days}, {self.condition.to_string()})'