
# `TRIX` — Triple Exponential Average Trading Series

The `TRIX` trading series represents the TRIX indicator, which is a triple-smoothed Exponential Moving Average used to identify trends and momentum changes.

It is built upon the [Triple Exponential Average indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/trix.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
TRIX(
    ticker: str,
    length: int = 18
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Period for TRIX calculation. Default is 18.

---

## Description

- Triple-smoothed EMA reduces market noise.
- TRIX crosses above 0 signal possible bullish trends, crosses below 0 signal bearish trends.

---

## Example Usage

```python
TRIX(
    ticker="AAPL",
    length=18
)
```
