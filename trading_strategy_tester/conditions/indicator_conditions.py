import pandas as pd
from trading_strategy_tester.indicators.indicator_accessor import IndicatorAccessor
from .condition import Condition

class RSICondition(Condition):
    def __init__(self, threshold: float, comparison: str, column: str='Close', length: int = 14):
        self.threshold = threshold
        self.comparison = comparison
        self.column = column
        self.length = length

    def evaluate(self, df: pd.DataFrame) -> pd.Series:
        df = df.indicator.rsi(self.column, self.length)

        return df[f'RSI_Close_14'] > self.threshold