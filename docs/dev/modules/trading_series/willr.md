
# `WILLR` — Williams %R Trading Series

The `WILLR` trading series represents Williams %R, a momentum indicator that measures overbought and oversold levels.

It is built upon the [Williams %R indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/willr.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
WILLR(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    length: int = 14
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`source`** (`SourceType`): Price source for calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for the %R calculation. Default is 14.

---

## Description

- Values near -20 suggest overbought conditions.
- Values near -80 suggest oversold conditions.
- Very similar in interpretation to the [Stochastic Oscillator](percent_k.md).

---

## Example Usage

```python
WILLR(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=14
)
```
