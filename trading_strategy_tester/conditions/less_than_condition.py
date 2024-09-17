import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.trading_plot.less_than_plot import LessThanPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot

class LessThanCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        series1 = self.first_series.get_data(downloader, df)
        series2 = self.second_series.get_data(downloader, df)

        # Calculate less_than: True if series1 is less than series2
        less_than = pd.Series(series1 < series2)

        signal_series = less_than.apply(
            lambda x: f'LessThanSignal({self.first_series.get_name()}, {self.second_series.get_name()})' if x else None)

        return less_than, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        return [LessThanPlot(
            self.first_series.get_data(downloader, df),
            self.second_series.get_data(downloader, df)
        )]

    def to_string(self) -> str:
        return f'LessThanCondition({self.first_series.get_name()}, {self.second_series.get_name()})'