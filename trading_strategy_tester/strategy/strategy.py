from datetime import datetime
from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.conditions.trade_conditions import TradeConditions
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.enums.period_enum import Period


class Strategy():
    def __init__(self,
                 ticker:str,
                 buy_condition: Condition,
                 sell_condition: Condition,
                 start_date: datetime,
                 end_date: datetime,
                 interval: Interval,
                 period: Period = Period.NOT_PASSED):
        self.ticker = ticker
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.period = period

    def execute(self):
        # TODO
        downloader = DownloadModule(self.start_date, self.end_date, self.interval, self.period)
        df = downloader.download_ticker(self.ticker)

        evaluated_conditions_df = TradeConditions(
            buy_condition=self.buy_condition,
            sell_condition=self.sell_condition,
            downloader=downloader
        ).evaluate_conditions(df)

        # Create Trades
        # Create Graphs
        # Create Stats
        return evaluated_conditions_df

    def get_trades(self):
        # TODO
        pass

    def get_graphs(self):
        # TODO
        pass

    def get_statistics(self):
        # TODO
        pass