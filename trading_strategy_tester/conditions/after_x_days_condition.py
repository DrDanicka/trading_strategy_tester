import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class AfterXDaysCondition(Condition):
    def __init__(self, condition: Condition, number_of_days: int):
        self.condition = condition
        self.number_of_days = number_of_days

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        return self.condition.evaluate(downloader, df).shift(self.number_of_days).fillna(False).astype(bool)

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = self.condition.get_graphs(downloader, df)

        # TODO shift graphs

        return graphs

    def get_string(self):
        return f'After{self.number_of_days}DaysSignal({self.condition.to_string()})'