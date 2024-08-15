import pandas as pd

from .condition import Condition

class TradeConditions:
    def __init__(self, buy_condition: Condition, sell_condition: Condition):
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition

    def evaluate_conditions(self, df: pd.DataFrame) -> pd.DataFrame:
        df['BUY'] = self.buy_condition.evaluate()
        df['SELL'] = self.sell_condition.evaluate()
        return df