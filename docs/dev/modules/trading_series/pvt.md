
# `PVT` — Price Volume Trend Trading Series

The `PVT` trading series represents the Price Volume Trend (PVT) indicator, which combines price change and volume to identify trend strength.

It is built upon the [Price Volume Trend indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volume/pvt.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
PVT(
    ticker: str
)
```

- **`ticker`** (`str`): Asset ticker symbol.

---

## Description

- Accumulates volume based on proportional price changes.
- Used to confirm trends and possible reversals.

---

## Example Usage

```python
PVT(
    ticker="AAPL"
)
```
