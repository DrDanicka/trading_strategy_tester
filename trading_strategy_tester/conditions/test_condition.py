import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class TestCondition(Condition):
    def __init__(self, series: TradingSeries):
        self.series = series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        result = self.series.get_data(downloader, df)
        signal_series = result.apply(lambda x: self.to_string() if x else None)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        return []

    def to_string(self) -> str:
        return f'TestCondition({self.series.get_name()})'