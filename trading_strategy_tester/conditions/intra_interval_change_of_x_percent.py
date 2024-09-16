import pandas as pd

from trading_strategy_tester.conditions.change_of_x_percent_on_y_days import ChangeOfXPercentOnYDaysCondition
from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class IntraIntervalChangeOfXPercentCondition(Condition):

    def __init__(self, series: TradingSeries, percent: float):
        self.series = series
        self.percent = percent
        self.change_of_x_percent_on_y_days_condition = ChangeOfXPercentOnYDaysCondition(series, percent, 1)

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        result, _ =  self.change_of_x_percent_on_y_days_condition.evaluate(downloader, df)

        signal_series = result.apply(
            lambda x: f'IntraIntervalChangeOfXPercentSignal({self.percent}, {self.series.get_name()})' if x else None
        )

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        # TODO plotting

        return None

    def to_string(self) -> str:
        return f'IntraIntervalChangeOfXPercentCondition({self.percent}, {self.series.get_name()})'
