from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.strategy.strategy import Strategy
from trading_strategy_tester.trading_series.cci_series.cci_series import CCI
from trading_strategy_tester.trading_series.default_series.const_series import CONST
from datetime import datetime
import json

# Define the CCI series for Tesla (TSLA)
cci_series = CCI('TSLA', length=20)  # Assuming length is 20, adjust if needed

# Define the buy condition: CCI crosses above 20
buy_condition = CrossOverCondition(
    first_series=cci_series,
    second_series=CONST(20)
)

# Define the sell condition: CCI crosses below 80
sell_condition = CrossOverCondition(
    first_series=CONST(80),
    second_series=cci_series
)

# Define the stop loss with a 10% limit
stop_loss = StopLoss(percentage=10)

# Create the Strategy object
strat = Strategy(
    ticker='TSLA',
    position_type=PositionTypeEnum.LONG,  # This is a long strategy
    buy_condition=buy_condition,
    sell_condition=sell_condition,
    stop_loss=stop_loss,
    start_date=datetime(2018, 1, 1),
    end_date=datetime(2020, 12, 31),
    initial_capital=100000  # Optional: specify initial capital if needed
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