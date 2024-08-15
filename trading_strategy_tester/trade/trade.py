import pandas as pd
import yfinance as yf
from datetime import datetime
from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.conditions.trade_conditions import TradeConditions


class Trade:
    def __init__(self, ticker: str, buy_condition: Condition, sell_condition: Condition, start_date: datetime,
                 end_date: datetime, interval: str):
        self.ticker = ticker
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.entry_date = start_date
        self.exit_date = end_date
        self.interval = interval

    def evaluate(self) -> pd.DataFrame:
        df = yf.download(self.ticker, interval=self.interval, start=self.entry_date, end=self.exit_date)

        trade_condition = TradeConditions(buy_condition=self.buy_condition, sell_condition=self.sell_condition)
        evaluated_df = trade_condition.evaluate_conditions(df)

        return evaluated_df
