from datetime import datetime
from trading_strategy_tester.conditions.condition import Condition
from enum import Enum

class Interval(Enum):
    ONE_MINUTE = '1m'
    TWO_MINUTES = '2m'
    FIVE_MINUTES = '5m'
    FIFTEEN_MINUTES = '15m'
    THIRTY_MINUTES = '30m'
    SIXTY_MINUTES = '60m'
    NINETY_MINUTES = '90m'
    ONE_HOUR = '1h'
    ONE_DAY = '1d'
    FIVE_DAYS = '5d'
    ONE_WEEK = '1wk'
    ONE_MONTH = '1mo'
    THREE_MONTHS = '3mo'

class Strategy():
    def __init__(self,
                 ticker:str,
                 buy_condition: Condition,
                 sell_condition: Condition,
                 start_date: datetime,
                 end_date: datetime,
                 interval: Interval):
        self.ticker = ticker
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval.value # string value

    def execute(self):
        # TODO
        # Download
        # Evaluate Conditions
        # Create Trades
        # Create Graphs
        # Create Stats
        pass

    def get_trades(self):
        # TODO
        pass

    def get_graphs(self):
        # TODO
        pass

    def get_statistics(self):
        # TODO
        pass