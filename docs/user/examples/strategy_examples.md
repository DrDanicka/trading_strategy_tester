
# Strategy Examples

This section provides a collection of example strategies that can be used with the Trading Strategy Tester. Each example demonstrates a different approach to trading, showcasing the flexibility and power of the framework. You can use these examples as a starting point for your own strategies or as inspiration for new ideas.

Every strategy is defined using the `Strategy` class, which allows you to specify the ticker symbol, position type, entry and exit conditions, start and end dates for backtesting, and other parameters that can be seen [here](../../dev/modules/strategy.md).

### Importing the necessary modules

For every strategy you have to import the `Strategy` class. Based on the strategy want to implement, you will also need to import the necessary conditions, trading series and other modules and enums. Here is a list of the modules and parameters and way to import them:

### Import Strategy class

```python
from trading_strategy_tester import Strategy
```

### Import Conditions

```python
from trading_strategy_tester.conditions import Condition
```
where `Condition` can be one of the conditions linked [here](../../dev/modules/conditions/index.md).

### Import Trading Series

```python
from trading_strategy_tester.trading_series import TradingSeries
```
where `TradingSeries` can be one of the series linked [here](../../dev/modules/trading_series.md).

### Import Strategy Parameters

```python
from trading_strategy_tester import PositionTypeEnum, StopLoss, StopLossType,TakeProfit, Interval, Period, Contracts, USD, PercentOfEquity, MoneyCommissions, PercentageCommissions
```
where all the parameters have their own page to explain their usage. Here are the links: [PositionTypeEnum](../../dev/modules/enums/position_type.md), [StopLoss](../../dev/modules/strategy_parameters/stop_loss.md), [TakeProfit](../../dev/modules/strategy_parameters/take_profit.md), [Interval](../../dev/modules/enums/interval.md), [Period](../../dev/modules/enums/period.md), [OrderSize](../../dev/modules/strategy_parameters/order_size.md), [TradeCommissions](../../dev/modules/strategy_parameters/trade_commissions.md).

This is basically all you need to import in order to create a strategy. Following are some examples of strategies that can be created using the `Strategy` class.


## RSI Strategy

We start with a simple strategy that uses the Relative Strength Index (RSI) to determine entry and exit points. The RSI is a momentum oscillator that measures the speed and change of price movements. It ranges from 0 to 100, with values above 70 indicating overbought conditions and values below 30 indicating oversold conditions.

This strategy will enter a long position when the RSI crosses above 30 and exit when it crosses below 70. It will also enter a short position when the RSI crosses below 70 and exit when it crosses above 30. It will buy one contract and sell one contract at a time and the strategy will be backtested on AAPL stock data from 2010 to 2020.

```python
Strategy(
    ticker="AAPL",
    position_type= PositionTypeEnum.LONG_SHORT_COMBINED,
    buy_condition= CrossOverCondition(
        first_series=RSI('AAPL'),
        second_series=CONST(30)
    ),
    sell_condition=CrossUnderCondition(
        first_series=RSI('AAPL'),
        second_series=CONST(70)
    ),
    start_date=datetime(2016, 1, 1),
    end_date=datetime(2020, 1, 1),
    order_size=Contracts(value=1)
)
```

## Uptrend Simple Moving Average Strategy

This strategy uses a simple moving average (SMA) to identify uptrends. It will enter a long position when the Simple Moving Average of length 21 is in uptrend for at least 5 days and exit when the Close price is below the Exponential Moving Average of length 50. It will also enter a short position when the Close price is above the Exponential Moving Average of length 50 and exit when the Simple Moving Average of length 21 is in downtrend for at least 5 days. It will enter every position with 100$ and backtest it on MSFT stock from all available data.

```python
Strategy(
    ticker="MSFT",
    position_type= PositionTypeEnum.LONG,
    buy_condition= UptrendForXDaysCondition(
        series=SMA('MSFT', length=21),
        number_of_days=5
    ),
    sell_condition=LessThanCondition(
        first_series=CLOSE('MSFT'),
        second_series=EMA('MSFT', length=50)
    ),
    period=Period.ONE_YEAR,
    order_size=USD(value=100)
)
```

## CCI and SMA Strategy

This strategy combines the Commodity Channel Index (CCI) and Simple Moving Average (SMA) to identify entry and exit points. It will enter a long position when the CCI crosses above -100 or the Close price crosses above the SMA of length 9. It will exit when the CCI crosses below 100 and the Close price crosses below the SMA of length 9. The strategy also includes a stop loss of 7% and a take profit of 15%. It will be backtested on GOOGL stock data from 2020 to 2024 with a commission of 0.1$ per trade.

```python
Strategy(
    ticker='GOOGL',
    position_type= PositionTypeEnum.LONG_SHORT_COMBINED,
    buy_condition= OR(
        CrossOverCondition(
            first_series=CLOSE('GOOGL'),
            second_series=SMA('GOOGL', source=SourceType.CLOSE, length=9, offset=0)
        ),
        CrossOverCondition(
            first_series=CCI('GOOGL', source=SourceType.HLC3, length=20),
            second_series=CONST(-100)
        )
    ),
    sell_condition=OR(
        CrossOverCondition(
            first_series=SMA('GOOGL', source=SourceType.CLOSE, length=9, offset=0),
            second_series=CLOSE('GOOGL')
        ),
        CrossUnderCondition(
            second_series=CCI('GOOGL', source=SourceType.HLC3, length=20),
            first_series=CONST(100)
        )
    ),
    stop_loss=StopLoss(percentage=7, stop_loss_type=StopLossType.NORMAL),
    take_profit=TakeProfit(percentage=15),
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2024, 1, 1),
    trade_commissions=MoneyCommissions(value=0.1)
)
```