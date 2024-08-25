import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_plot.cross_over_plot import CrossOverPlot

class CrossOverCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        series1 : pd.Series = self.first_series.get_data(downloader, df)
        series2 : pd.Series = self.second_series.get_data(downloader, df)

        crossover = (series1.shift(1) < series2.shift(1)) & (series1 > series2)

        return crossover.fillna(False)

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        return [CrossOverPlot(
            self.first_series.get_data(downloader, df),
            self.second_series.get_data(downloader, df)
        )]

