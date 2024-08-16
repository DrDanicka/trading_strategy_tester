import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule
from ..trading_series.trading_series import TradingSeries


class CrossOverCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule) -> pd.Series:
        series1 = self.first_series.get_data(downloader)
        series2 = self.second_series.get_data(downloader)

        crossover = (series1.shift(1) < series2.shift(1)) & (series1 > series2)

        return crossover.fillna(False)

class GreaterThanCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule) -> pd.Series:
        series1 = self.first_series.get_data(downloader)
        series2 = self.second_series.get_data(downloader)

        return series1 > series2

class LessThanCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule) -> pd.Series:
        series1 = self.first_series.get_data(downloader)
        series2 = self.second_series.get_data(downloader)

        return series1 < series2

