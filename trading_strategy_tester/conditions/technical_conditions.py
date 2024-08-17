import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule
from ..trading_plot.cross_over_plot import CrossOverPlot
from ..trading_plot.trading_plot import TradingPlot
from ..trading_series.trading_series import TradingSeries


class CrossOverCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        series1 : pd.Series = self.first_series.get_data(downloader)
        series2 : pd.Series = self.second_series.get_data(downloader)

        # Add series1, series2 to DataFrame
        df[series1.name] = series1
        df[series2.name] = series2

        crossover = (series1.shift(1) < series2.shift(1)) & (series1 > series2)

        return crossover.fillna(False)

    def get_graphs(self, downloader: DownloadModule) -> [TradingPlot]:
        return [CrossOverPlot(
            self.first_series.get_data(downloader),
            self.second_series.get_data(downloader)
        )]


class GreaterThanCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        series1 = self.first_series.get_data(downloader)
        series2 = self.second_series.get_data(downloader)

        # Add series1, series2 to DataFrame
        df[series1.name] = series1
        df[series2.name] = series2

        return series1 > series2

    def get_graphs(self, downloader: DownloadModule) -> [TradingPlot]:
        # TODO create greaterThanCondition graph method
        return []

class LessThanCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        series1 = self.first_series.get_data(downloader)
        series2 = self.second_series.get_data(downloader)

        # Add series1, series2 to DataFrame
        df[series1.name] = series1
        df[series2.name] = series2

        return series1 < series2

    def get_graphs(self, downloader: DownloadModule) -> [TradingPlot]:
        # TODO create greaterThanCondition graph
        return []