from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.conditions.logical_conditions.or_condition import OR
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.strategy.strategy import Strategy
from trading_strategy_tester.trading_series.default_series.close_series import CLOSE
from trading_strategy_tester.trading_series.atr_series.atr_series import ATR
from trading_strategy_tester.trading_series.bb_series.bb_upper_series import BBUPPER
from trading_strategy_tester.trading_series.bb_series.bb_lower_series import BBLOWER
from datetime import datetime
import json

# Define the series for Logitech (LOGI)
close_series = CLOSE('LOGI')
atr_series = ATR('LOGI', length=14)  # ATR with length 14
bb_upper_series = BBUPPER('LOGI', length=20)  # Bollinger Bands with length 20
bb_lower_series = BBLOWER('LOGI', length=20)

# Define the sell condition: Close price crosses below ATR
sell_condition_1 = CrossOverCondition(
    first_series=atr_series,
    second_series=close_series
)

# Define the buy condition: Close price crosses above ATR
buy_condition_1 = CrossOverCondition(
    first_series=close_series,
    second_series=atr_series
)

# Define the buy condition: Close price is above the upper Bollinger Band
buy_condition_2 = CrossOverCondition(
    first_series=close_series,
    second_series=bb_upper_series
)

# Define the sell condition: Close price is below the lower Bollinger Band
sell_condition_2 = CrossOverCondition(
    first_series=bb_lower_series,
    second_series=close_series
)

# Combine the buy conditions using OrCondition
buy_condition = OR(buy_condition_1, buy_condition_2)

# Combine the sell conditions using OrCondition
sell_condition = OR(sell_condition_1, sell_condition_2)

# Define the stop loss with a 10% limit
stop_loss = StopLoss(percentage=10)

# Create the Strategy object
strat = Strategy(
    ticker='LOGI',
    position_type=PositionTypeEnum.SHORT,  # Short-only strategy
    buy_condition=buy_condition,
    sell_condition=sell_condition,
    stop_loss=stop_loss,
    start_date=datetime(2015, 1, 1),
    end_date=datetime(2023, 12, 31),
    interval=Interval.ONE_WEEK,  # Weekly timeframe using IntervalEnum
    initial_capital=100000  # Optional: specify initial capital if needed
)

df = strat.execute()

# Plots strategy plots
dark = True
strat.get_graphs()['PRICE'].show_plot(dark=dark)
strat.get_graphs()['BUY'][1].show_plot(dark=dark)
strat.get_graphs()['SELL'][1].show_plot(dark=dark)


# Prints strategy trades
print('Trades:')
print(strat.get_trades())

# Prints stats about the strategy
print('Performance of the strategy:')
print(json.dumps(strat.get_statistics(), indent=4))