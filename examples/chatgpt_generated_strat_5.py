from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.strategy.strategy import Strategy
from trading_strategy_tester.trading_series.rsi_series.rsi_series import RSI
from trading_strategy_tester.trading_series.default_series.const_series import CONST
from trading_strategy_tester.trade.order_size.contracts import Contracts
import json

# Define the RSI series for META stock (use max available period)
rsi_series = RSI('META', length=14)

# Define the buy condition: RSI crosses above 30
buy_condition = CrossOverCondition(
    first_series=rsi_series,
    second_series=CONST(30)
)

# Define the sell condition: RSI crosses below 70
sell_condition = CrossOverCondition(
    first_series=CONST(70),
    second_series=rsi_series
)

# Define the order size of 10 shares per trade
order_size = Contracts(10)

# Create the Strategy object
strat = Strategy(
    ticker='META',
    position_type=PositionTypeEnum.LONG_SHORT_COMBINED,  # Long and short strategy
    buy_condition=buy_condition,
    sell_condition=sell_condition,
    period=Period.MAX,
    interval=Interval.ONE_DAY,  # Daily timeframe
    initial_capital=100000,  # Optional: specify initial capital if needed
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