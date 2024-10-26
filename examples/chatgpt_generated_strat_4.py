from trading_strategy_tester.conditions.threshold_conditions.greater_than_condition import GreaterThanCondition
from trading_strategy_tester.conditions.threshold_conditions.less_than_condition import LessThanCondition
from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.conditions.logical_conditions.or_condition import OrCondition
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.strategy.strategy import Strategy
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_conversion_series import ICHIMOKU_CONVERSION
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_base_series import ICHIMOKU_BASE
from trading_strategy_tester.trading_series.default_series.high_series import HIGH
from trading_strategy_tester.trading_series.default_series.low_series import LOW
from trading_strategy_tester.trade.order_size.usd import USD
from datetime import datetime
import json

# Define the series for Apple (AAPL)
high_series = HIGH('AAPL')
low_series = LOW('AAPL')
kijun_sen = ICHIMOKU_BASE('AAPL')
tenkan_sen = ICHIMOKU_CONVERSION('AAPL')

# Define the buy conditions
buy_condition_1 = GreaterThanCondition(
    first_series=high_series,
    second_series=kijun_sen
)

buy_condition_2 = CrossOverCondition(
    first_series=tenkan_sen,
    second_series=kijun_sen
)

# Combine the buy conditions using OrCondition
buy_condition = OrCondition(buy_condition_1, buy_condition_2)

# Define the sell conditions
sell_condition_1 = LessThanCondition(
    first_series=low_series,
    second_series=kijun_sen
)

sell_condition_2 = CrossOverCondition(
    first_series=kijun_sen,
    second_series=tenkan_sen
)

# Combine the sell conditions using OrCondition
sell_condition = OrCondition(sell_condition_1, sell_condition_2)

# Define a constant order size of $100 per trade
order_size = USD(100)

# Create the Strategy object
strat = Strategy(
    ticker='AAPL',
    position_type=PositionTypeEnum.LONG,  # Long-only strategy
    buy_condition=buy_condition,
    sell_condition=sell_condition,
    start_date=datetime(2020, 1, 1),
    end_date=datetime.now(),
    interval=Interval.ONE_DAY,  # Daily timeframe
    initial_capital=9500,  # Initial budget of $9,500
    order_size=order_size
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