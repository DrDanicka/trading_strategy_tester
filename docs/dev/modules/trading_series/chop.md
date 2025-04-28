
# `CHOP` — Choppiness Index Trading Series

The `CHOP` trading series represents the Choppiness Index, an indicator used to determine if the market is trading sideways (choppy) or trending strongly.

It is built upon the [Choppiness Index indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volatility/chop.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
CHOP(
    ticker: str,
    length: int = 14,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period for the Choppiness Index calculation. Default is 14.
- **`offset`** (`int`): Offset for shifting the resulting series. Default is 0.

---

## Description

- Values near 100 indicate very sideways/choppy price action.
- Values near 0 suggest strong directional trending.
- CHOP helps determine whether to favor trend-following or mean-reverting strategies.

---

## Example Usage

```python
CHOP(
    ticker="AAPL",
    length=14,
    offset=0
)
```
