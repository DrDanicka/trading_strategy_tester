
# `COPPOCK` — Coppock Curve Trading Series

The `COPPOCK` trading series represents the Coppock Curve, a momentum indicator developed for identifying major bottoms in markets.

It is built upon the [Coppock Curve indicator](../../../../trading_strategy_tester/indicators/momentum/cop.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
COPPOCK(
    ticker: str,
    length: int = 10,
    long_roc_length: int = 14,
    short_roc_length: int = 11
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Period for smoothing the rate of change. Default is 10.
- **`long_roc_length`** (`int`): Long-term rate of change period. Default is 14.
- **`short_roc_length`** (`int`): Short-term rate of change period. Default is 11.

---

## Description

- Coppock Curve was originally designed for identifying long-term buying opportunities.
- Positive curves suggest long opportunities; declining curves may indicate weakening momentum.
- Less sensitive to short-term noise.

---

## Example Usage

```python
COPPOCK(
    ticker="AAPL",
    length=10,
    long_roc_length=14,
    short_roc_length=11
)
```
