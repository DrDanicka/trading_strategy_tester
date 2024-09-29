from datetime import datetime

import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.conditions.stoploss_takeprofit.take_profit import TakeProfit
from trading_strategy_tester.conditions.trade_conditions import TradeConditions
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.statistics.statistics import get_strategy_stats
from trading_strategy_tester.trade.order_size.contracts import Contracts
from trading_strategy_tester.trade.order_size.order_size import OrderSize
from trading_strategy_tester.trade.trade import create_all_trades
from trading_strategy_tester.trade.trade_commissions.money_commissions import MoneyCommissions
from trading_strategy_tester.trade.trade_commissions.trade_commissions import TradeCommissions
from trading_strategy_tester.utils.validations import get_position_type_from_enum


class Strategy:
    """
    A trading strategy that defines conditions for buying and selling
    a financial instrument, with optional stop loss and take profit features.

    :param ticker: The financial instrument to trade.
    :param position_type: The type of position to take (e.g., long or short).
    :param buy_condition: The condition that must be met to execute a buy.
    :param sell_condition: The condition that must be met to execute a sell.
    :param stop_loss: Optional stop loss condition.
    :param take_profit: Optional take profit condition.
    :param start_date: The start date for backtesting (default is 2024-01-01).
    :param end_date: The end date for backtesting (default is today).
    :param interval: The time interval for the trading data (default is daily).
    :param period: The period for which to evaluate the conditions (default is not passed).
    :param trade_commissions: The commissions associated with trades (default is zero commission).
    """

    def __init__(self,
                 ticker: str,
                 position_type: PositionTypeEnum,
                 buy_condition: Condition,
                 sell_condition: Condition,
                 stop_loss: StopLoss = None,
                 take_profit: TakeProfit = None,
                 start_date: datetime = datetime(2024, 1, 1),
                 end_date: datetime = datetime.today(),
                 interval: Interval = Interval.ONE_DAY,
                 period: Period = Period.NOT_PASSED,
                 initial_capital: float = 1_000_000,
                 order_size: OrderSize = Contracts(1),
                 trade_commissions: TradeCommissions = MoneyCommissions(0)
                 ):
        self.ticker = ticker
        self.position_type_enum = position_type
        self.position_type = get_position_type_from_enum(position_type)
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.period = period
        self.trade_commissions = trade_commissions
        self.initial_capital = initial_capital
        self.order_size = order_size
        self.trade_conditions = None
        self.graphs = dict()
        self.trades = list()
        self.stats = dict()

    def execute(self) -> pd.DataFrame:
        """
        Executes the trading strategy by downloading data, evaluating
        conditions, setting stop losses and take profits, and generating
        trade statistics.

        :return: A DataFrame containing the evaluated conditions for buying and selling.
        :rtype: pd.DataFrame
        """
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
            self.take_profit.set_take_profit(evaluated_conditions_df, self.position_type_enum)
        if self.stop_loss is not None:
            self.stop_loss.set_stop_loss(evaluated_conditions_df, self.position_type_enum)

        # Clean the BUY and SELL columns based on the position type
        self.position_type.clean_buy_sell_columns(evaluated_conditions_df)

        # Create Graphs
        self.graphs = self.trade_conditions.get_graphs(df)

        # Create list of trades
        self.trades = create_all_trades(df, self.order_size, self.initial_capital, self.trade_commissions)

        # Create stats of the strategy
        self.stats = get_strategy_stats(self.trades, evaluated_conditions_df, None)

        # Delete temp downloaded files
        downloader.delete_temp_files()

        return evaluated_conditions_df

    def get_trades(self) -> list:
        """
        Returns the list of trades executed by the strategy.

        :return: A list of trades.
        :rtype: list
        """
        return self.trades

    def get_graphs(self) -> dict:
        """
        Returns the generated graphs based on trading conditions.

        :return: A dictionary containing the generated graphs.
        :rtype: dict
        """
        return self.graphs

    def get_statistics(self) -> dict:
        """
        Returns the statistics of the trading strategy.

        :return: A dictionary containing the strategy statistics.
        :rtype: dict
        """
        return self.stats
