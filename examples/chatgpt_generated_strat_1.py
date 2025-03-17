from trading_strategy_tester.conditions.threshold_conditions.greater_than_condition import GreaterThanCondition
from trading_strategy_tester.conditions.threshold_conditions.less_than_condition import LessThanCondition
from trading_strategy_tester.conditions.logical_conditions.and_condition import AND
from trading_strategy_tester.conditions.logical_conditions.or_condition import OR
from trading_strategy_tester.conditions.fibonacci_retracement_levels_conditions.downtrend_fib_retracement import DowntrendFibRetracementLevelCondition
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.conditions.stoploss_takeprofit.take_profit import TakeProfit
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels
from trading_strategy_tester.strategy.strategy import Strategy  
from trading_strategy_tester.trading_series.ma_series.ema_series import EMA
from trading_strategy_tester.trading_series.adx_series.adx_series import ADX
from trading_strategy_tester.trading_series.di_series.di_minus_series import DI_MINUS
from trading_strategy_tester.trading_series.di_series.di_plus_series import DI_PLUS
from trading_strategy_tester.trading_series.default_series.const_series import CONST
from trading_strategy_tester.trading_series.default_series.close_series import CLOSE
from trading_strategy_tester.trade.order_size.contracts import Contracts
from datetime import datetime
import json

# Define the EMA series for Google (GOOGL) with length 21
ema_series = EMA('GOOGL', length=21)
close_series = CLOSE('GOOGL')

# Define the ADX and DI series
adx_series = ADX('GOOGL', length=14)  # Typical length of 14 for ADX
di_plus = DI_PLUS('GOOGL', length=14)
di_minus = DI_MINUS('GOOGL', length=14)

# Define the buy condition: EMA(21) < CLOSE and ADX > 30
buy_condition = AND(
    LessThanCondition(
        first_series=ema_series,
        second_series=close_series
    ),
    GreaterThanCondition(
        first_series=adx_series,
        second_series=CONST(30)
    )
)

# Define the sell condition: -DI > +DI or Downtrend Fibonacci retracement level reaches 61.8%
sell_condition = OR(
    GreaterThanCondition(
        first_series=di_minus,
        second_series=di_plus
    ),
    DowntrendFibRetracementLevelCondition(
        fib_level=FibonacciLevels.LEVEL_61_8,  # Specify the 61.8% level
        length=14  # Use a default or appropriate length for evaluation
    )
)

# Define the stop loss and take profit conditions
stop_loss = StopLoss(percentage=7)
take_profit = TakeProfit(percentage=15)

# Define the order size as 3 contracts
order_size = Contracts(3)

# Create the Strategy object
strat = Strategy(
    ticker='GOOGL',
    position_type=PositionTypeEnum.LONG_SHORT_COMBINED,
    buy_condition=buy_condition,
    sell_condition=sell_condition,
    stop_loss=stop_loss,
    take_profit=take_profit,
    start_date=datetime(2018, 1, 1),
    end_date=datetime(2020, 12, 31),
    initial_capital=100000,  # Initial capital of $100,000
    order_size=order_size
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