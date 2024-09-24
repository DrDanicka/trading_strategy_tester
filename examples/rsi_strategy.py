from datetime import datetime
import json
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.conditions.stoploss_takeprofit.take_profit import TakeProfit
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.trading_series.default_series.const_series import CONST
from trading_strategy_tester.trading_series.rsi_series.rsi_series import RSI
from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.strategy.strategy import Strategy

"""
This is example of simple RSI strategy that:
* opens long when RSI crosses 30 from below
* exits long when RSI crosses 70 from above

There is also stop loss at 5% and take profit at 10%
"""

ticker = 'MSFT' # Microsoft ticker

strat = Strategy(
    ticker=ticker,
    position_type= PositionTypeEnum.LONG,
    buy_condition= CrossOverCondition(
        RSI(ticker=ticker),
        CONST(30)
    ),
    sell_condition=CrossOverCondition(
        CONST(70),
        RSI(ticker=ticker)
    ),
    stop_loss=StopLoss(5),
    take_profit=TakeProfit(10),
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2024, 1, 1)
)

df = strat.execute()

# Plots strategy plots
dark = True
strat.get_graphs()['PRICE'].show_plot(dark=dark)
strat.get_graphs()['BUY'][0].show_plot(dark=dark)
strat.get_graphs()['SELL'][0].show_plot(dark=dark)


# Prints strategy trades
print('Trades:')
print(strat.get_trades())

# Prints stats about the strategy
print('Performance of the strategy:')
print(json.dumps(strat.get_statistics(), indent=4))