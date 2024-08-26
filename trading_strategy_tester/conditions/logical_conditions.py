import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule
from ..trading_plot.trading_plot import TradingPlot


class AndCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        result = self.conditions[0].evaluate(downloader, df)

        for condition in self.conditions[1:]:
            result &= condition.evaluate(downloader, df)

        return result

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = []

        for condition in self.conditions:
            graphs += condition.get_graphs(downloader, df)

        return graphs

    


class OrCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        result = self.conditions[0].evaluate(downloader, df)

        for condition in self.conditions:
            result |= condition.evaluate(downloader, df)

        return result

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = []

        for condition in self.conditions:
            graphs += condition.get_graphs(downloader, df)

        return graphs

class IfThenElseCondition(Condition):
    def __init__(self, if_condition: Condition, else_condition: Condition):
        self.if_condition = if_condition
        self.else_condition = else_condition

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        result = self.if_condition.evaluate(downloader, df)
        result |= self.else_condition.evaluate(downloader, df)

        return result

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = []

        for condition in [self.if_condition, self.else_condition]:
            graphs += condition.get_graphs(downloader, df)

        return graphs