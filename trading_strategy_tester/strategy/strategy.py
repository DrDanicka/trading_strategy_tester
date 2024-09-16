from datetime import datetime
from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.conditions.stop_loss import StopLoss
from trading_strategy_tester.conditions.take_profit import TakeProfit
from trading_strategy_tester.conditions.trade_conditions import TradeConditions
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.utils.validations import get_position_type_from_enum


class Strategy():
    def __init__(self,
                 ticker:str,
                 position_type: PositionTypeEnum,
                 buy_condition: Condition,
                 sell_condition: Condition,
                 stop_loss: StopLoss = None,
                 take_profit: TakeProfit = None,
                 start_date: datetime = datetime(2024, 1, 1),
                 end_date: datetime = datetime.today(),
                 interval: Interval = Interval.ONE_DAY,
                 period: Period = Period.NOT_PASSED):
        self.ticker = ticker
        self.position_type = get_position_type_from_enum(position_type)
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.period = period
        self.trade_conditions = None
        self.graphs = dict()

    def execute(self):
        downloader = DownloadModule(self.start_date, self.end_date, self.interval, self.period)
        df = downloader.download_ticker(self.ticker)

        self.trade_conditions = TradeConditions(
            buy_condition=self.buy_condition,
            sell_condition=self.sell_condition,
            downloader=downloader
        )

        evaluated_conditions_df = self.trade_conditions.evaluate_conditions(df)

        # Sets stop losses and take profits
        if self.take_profit is not None:
            self.take_profit.set_take_profit(evaluated_conditions_df)
        if self.stop_loss is not None:
            self.stop_loss.set_stop_loss(evaluated_conditions_df)

        # Clean the BUY and SELL columns based of the position type
        self.position_type.clean_buy_sell_columns(evaluated_conditions_df)

        # Create Graphs
        self.graphs = self.trade_conditions.get_graphs(df)

        # TODO Create trades
        # TODO Create Stats

        # Delete temp downloaded files
        downloader.delete_temp_files()

        return evaluated_conditions_df

    def get_trades(self):
        # TODO
        pass

    def get_graphs(self) -> dict:
        return self.graphs

    def get_statistics(self):
        # TODO
        pass