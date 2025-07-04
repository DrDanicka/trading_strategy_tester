# Indicator Examples

This section provides a collection of example indicators that can be used with the Trading Strategy Tester. They all return a series of the same length as the input series, containing the calculated indicator values. You can use them separately of the `Strategy` object for your own analysis or as part of a trading strategy.

All available indicators can be found [here](../../dev/modules/indicators.md). The indicators are implemented as functions which take input series of type `pd.Series` and parameters and return a series of the same length with the indicator values for given input series. 

### Importing indicators

```python
from trading_strategy_tester.indicators import Indicator
```
where `Indicator` can be one of the indicators linked [here](../../dev/modules/indicators.md).

Following are some examples of indicator calculations:

## RSI Calculation
```python
from trading_strategy_tester.indicators import rsi

rsi_series = rsi(
    series=YOUR_SERIES,
    length=14
)
```

## ADX Calculation
```python
from trading_strategy_tester.indicators import adx

adx_series = adx(
    high=YOUR_HIGH_SERIES,
    low=YOUR_LOW_SERIES,
    close=YOUR_CLOSE_SERIES,
    adx_smoothing=14,
    di_length=21
)
```

## ATR Calculation
```python
from trading_strategy_tester.indicators import atr
from trading_strategy_tester import SmoothingType

atr_series = atr(
    high=YOUR_HIGH_SERIES,
    low=YOUR_LOW_SERIES,
    close=YOUR_CLOSE_SERIES,
    period=14,
    smoothing=SmoothingType.RMA
)
```

## EMA Calculation
```python
from trading_strategy_tester.indicators import ema

ema_series = ema(
    series=YOUR_SERIES,
    length=14,
    offset=2
)
```