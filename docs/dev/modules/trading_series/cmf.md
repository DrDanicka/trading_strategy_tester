
# `CMF` — Chaikin Money Flow Trading Series

The `CMF` trading series represents the Chaikin Money Flow indicator, which measures the volume-weighted average of accumulation and distribution over a specified period.

It is built upon the [Chaikin Money Flow indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volume/cmf.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
CMF(
    ticker: str,
    length: int = 20
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period for calculating CMF. Default is 20.

---

## Description

- Positive CMF values suggest buying pressure (accumulation).
- Negative CMF values suggest selling pressure (distribution).
- Useful for confirming price trends and breakouts.

---

## Example Usage

```python
CMF(
    ticker="AAPL",
    length=20
)
```
