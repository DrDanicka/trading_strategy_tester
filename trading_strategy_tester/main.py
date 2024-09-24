from datetime import datetime
import json
from trading_strategy_tester.conditions.parameterized_conditions.after_x_days_condition import AfterXDaysCondition
from trading_strategy_tester.conditions.parameterized_conditions.intra_interval_change_of_x_percent_condition import \
    IntraIntervalChangeOfXPercentCondition
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.conditions.stoploss_takeprofit.take_profit import TakeProfit
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.trading_series.default_series.close_series import CLOSE
from trading_strategy_tester.trading_series.default_series.const_series import CONST
from trading_strategy_tester.trading_series.ma_series.ema_series import EMA
from trading_strategy_tester.trading_series.rsi_series.rsi_series import RSI
from trading_strategy_tester.conditions.logical_conditions.or_condition import OrCondition
from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.conditions.threshold_conditions.less_than_condition import LessThanCondition
from trading_strategy_tester.strategy.strategy import Strategy

'''
This is one of the examples of strategy.
'''

ticker = 'AAPL'

strat = Strategy(
    ticker=ticker,
    position_type= PositionTypeEnum.LONG,
    buy_condition=OrCondition(
        AfterXDaysCondition(
            CrossOverCondition(
                RSI(ticker=ticker),
                CONST(30)
            ),
            50
        ),
        AfterXDaysCondition(
            LessThanCondition(
                EMA(ticker=ticker),
                CLOSE(ticker=ticker)
            ),
            -100
        )
    ),
    sell_condition=OrCondition(
        CrossOverCondition(
            CONST(70),
            RSI(ticker=ticker)
        ),
        IntraIntervalChangeOfXPercentCondition(
            CLOSE(ticker=ticker),
            -5
        )
    ),
    stop_loss=StopLoss(5),
    take_profit=TakeProfit(10),
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2024, 1, 1)
)

df = strat.execute()

# Plots strategy plots
# strat.get_graphs()['PRICE'].show_plot(dark=True)
# strat.get_graphs()['BUY'][1].show_plot(dark=False)

# Prints strategy trades
# print(strat.get_trades())

# Prints stats about the strategy
# print(json.dumps(strat.get_statistics(), sort_keys=True, indent=4))