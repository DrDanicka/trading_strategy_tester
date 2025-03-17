from datetime import datetime
import json

from trading_strategy_tester.conditions.logical_conditions.or_condition import OR
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.conditions.stoploss_takeprofit.take_profit import TakeProfit
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trade.trade_commissions.money_commissions import MoneyCommissions
from trading_strategy_tester.trading_series.default_series.close_series import CLOSE
from trading_strategy_tester.trading_series.default_series.const_series import CONST
from trading_strategy_tester.trading_series.rsi_series.rsi_series import RSI
from trading_strategy_tester.trading_series.ma_series.sma_series import SMA
from trading_strategy_tester.trading_series.cci_series.cci_series import CCI
from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.strategy.strategy import Strategy

"""
This is example of simple SMA and CCI strategy that:
* opens long when either SMA crosses price Close from below or CCI crosses -100 from below
* exits long when either SMA crosses price Close from above or CCI crosses 100 from above

* opens short when either SMA crosses price Close from above or CCI crosses 100 from above
* exits short when either SMA crosses price Close from below or CCI crosses -100 from below

There is also stop loss at 7% and take profit at 15% and also trade commission 0.1$ for each trade
"""

ticker = 'GOOG' # Google ticker

strat = Strategy(
    ticker=ticker,
    position_type= PositionTypeEnum.LONG_SHORT_COMBINED,
    buy_condition= OR(
        CrossOverCondition(
            CLOSE(ticker=ticker),
            SMA(ticker=ticker, source=SourceType.CLOSE, length=9, offset=0)
        ),
        CrossOverCondition(
            CCI(ticker=ticker, source=SourceType.HLC3, length=20),
            CONST(-100)
        )
    ),
    sell_condition=OR(
        CrossOverCondition(
            SMA(ticker=ticker, source=SourceType.CLOSE, length=9, offset=0),
            CLOSE(ticker=ticker)
        ),
        CrossOverCondition(
            CONST(100),
            CCI(ticker=ticker, source=SourceType.HLC3, length=20),
        )
    ),
    stop_loss=StopLoss(7),
    take_profit=TakeProfit(15),
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2024, 1, 1),
    trade_commissions=MoneyCommissions(0.1)
)

df = strat.execute()

# Plots strategy plots
dark = False
strat.get_graphs()['PRICE'].show_plot(dark=dark)
strat.get_graphs()['BUY'][0].show_plot(dark=dark)
strat.get_graphs()['SELL'][1].show_plot(dark=dark)


# Prints strategy trades
print('Trades:')
print(strat.get_trades())

# Prints stats about the strategy
print('Performance of the strategy:')
print(json.dumps(strat.get_statistics(), indent=4))