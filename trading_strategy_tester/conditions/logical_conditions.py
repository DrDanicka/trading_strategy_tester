import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule
from ..trading_plot.trading_plot import TradingPlot


class AndCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        result = pd.Series([True] * len(df))
        signal_series = pd.Series([''] * len(df))

        for i, condition in enumerate(self.conditions):
            cond_result, signal_result = condition.evaluate(downloader, df)
            # Bool AND for True and False values
            result &= cond_result
            # Add previous signals as string
            signal_series += signal_result.astype(str)

            if i != len(self.conditions) - 1:
                signal_series += pd.Series([', '] * len(df))

        # If the result is False then put None in place of the strings
        signal_series = signal_series.where(result, None)
        # Wrap signal in AndSignal
        signal_series = signal_series.apply(lambda x: f'And({x})' if x is not None else None)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = []

        for condition in self.conditions:
            graphs += condition.get_graphs(downloader, df)

        return graphs

    def to_string(self) -> str:
        signals = []
        for condition in self.conditions:
            signals.append(condition.to_string())

        return f'AndCondition({', '.join(signals)})'



class OrCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        result = pd.Series([False] * len(df))
        signal_series = pd.Series([None] * len(df)).astype(object)

        for condition in self.conditions:
            cond_result, signal_result = condition.evaluate(downloader, df)
            # Bool OR for True and False values
            result |= cond_result
            # Keep signals from previous conditions
            signal_series = signal_series.combine_first(signal_result)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = []

        for condition in self.conditions:
            graphs += condition.get_graphs(downloader, df)

        return graphs

    def to_string(self) -> str:
        signals = []
        for condition in self.conditions:
            signals.append(condition.to_string())

        return f'OrCondition({', '.join(signals)})'

class IfThenElseCondition(Condition):
    def __init__(self, if_condition: Condition, else_condition: Condition):
        self.if_condition = if_condition
        self.else_condition = else_condition

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        result = pd.Series([True] * len(df))
        signal_series = pd.Series([None] * len(df))

        # Evaluate conditions
        if_cond_result, if_signal_result = self.if_condition.evaluate(downloader, df)
        else_cond_result, else_signal_result = self.else_condition.evaluate(downloader, df)

        # If if_cond is True then keep True otherwise look at else_cond
        result = (result & if_cond_result ) | else_cond_result

        # Keep signals from previous conditions
        signal_series = signal_series.combine_first(if_signal_result).combine_first(else_signal_result)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        graphs = []

        for condition in [self.if_condition, self.else_condition]:
            graphs += condition.get_graphs(downloader, df)

        return graphs

    def to_string(self) -> str:
        return f'IfThenElseCondition({self.if_condition.to_string()}, {self.else_condition.to_string()})'