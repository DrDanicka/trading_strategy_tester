import pandas as pd
from .condition import Condition
from ..trade.trading_series import TradingSeries


class CrossOverCondition(Condition):
    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self) -> pd.Series:
        series1 = self.first_series.get_data()
        series2 = self.second_series.get_data()

        crossover = (series1.shift(1) < series2.shift(1)) & (series1 > series2)

        return crossover.fillna(False)