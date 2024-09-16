import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class ChangeOfXPercentOnYDaysCondition(Condition):
    def __init__(self, series: TradingSeries, percent: float, number_of_days: int):
        self.series = series
        self.percent = percent
        self.number_of_days = number_of_days


    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        series: pd.Series = self.series.get_data(downloader, df)
        result = pd.Series([False] * len(df), index=df.index)

        for i in range(len(series)):
            if i >= self.number_of_days:
                current_percent = (100 * series[i]) / series[i - self.number_of_days] - 100
                # If the percent is positive then calculate more than threshold
                if 0 < self.percent <= current_percent:
                    result[i] = True
                # If the percent is negative then calculate less than threshold
                elif 0 > self.percent >= current_percent:
                    result[i] = True

        result.name = None

        signal_series = result.apply(
            lambda x: f'ChangeOfXPercentOnYDaysSignal({self.percent}, {self.number_of_days}, {self.series.get_name()})' if x else None
        )

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        # TODO plotting

        return None

    def to_string(self) -> str:
        return f'ChangeOfXPercentOnYDaysCondition({self.percent}, {self.number_of_days}, {self.series.get_name()})'

