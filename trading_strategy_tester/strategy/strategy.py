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
from trading_strategy_tester.utils.parameter_validations import get_position_type_from_enum


class Strategy:
    """
    A trading strategy that defines conditions for buying and selling
    a financial instrument, with optional stop loss and take profit features.

    :param ticker: The financial instrument to trade.
    :type ticker: str
    :param position_type: The type of position to take (e.g., long or short).
    :type position_type: PositionType
    :param buy_condition: The condition that must be met to execute a buy.
    :type buy_condition: Condition
    :param sell_condition: The condition that must be met to execute a sell.
    :type sell_condition: Condition
    :param stop_loss: Optional stop loss condition.
    :type stop_loss: StopLoss
    :param take_profit: Optional take profit condition.
    :type take_profit: TakeProfit, optional
    :param start_date: The start date for backtesting (default is 2024-01-01).
    :type start_date: datetime, optional
    :param end_date: The end date for backtesting (default is today).
    :type end_date: datetime, optional
    :param interval: The time interval for the trading data (default is daily).
    :type interval: Interval
    :param period: The period for which to evaluate the conditions (default is not passed).
    :type period: Period
    :param initial_capital: The initial capital available for trading (default is 1,000,000).
    :type initial_capital: float
    :param order_size: The order size used for each trade (default is 1 contract).
    :type order_size: OrderSize, optional
    :param trade_commissions: The commissions associated with trades (default is zero commission).
    :type trade_commissions: TradeCommissions
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

        # Create list of trades
        self.trades = create_all_trades(df, self.order_size, self.initial_capital, self.trade_commissions)

        # Create Graphs
        self.graphs = self.trade_conditions.get_graphs(df, self.trades)

        # Create stats of the strategy
        self.stats = get_strategy_stats(self.trades, evaluated_conditions_df, self.initial_capital, self.order_size)

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

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the strategy.

        :return: A dictionary containing the strategy parameters.
        :rtype: dict
        """
        return {
            "ticker": self.ticker,
            "position_type": self.position_type_enum,
            "buy_condition": self.buy_condition.to_dict(),
            "sell_condition": self.sell_condition.to_dict(),
            "stop_loss": self.stop_loss if self.stop_loss else None,
            "take_profit": self.take_profit if self.take_profit else None,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "interval": self.interval,
            "period": self.period,
            "initial_capital": self.initial_capital,
            "order_size": self.order_size,
            "trade_commissions": self.trade_commissions
        }