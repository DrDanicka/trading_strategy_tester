
# `DC_LOWER` — Donchian Channel Lower Band Trading Series

The `DC_LOWER` trading series represents the lower band of the Donchian Channel, calculated as the lowest low over a specified period.

It is built upon the [Donchian Channel indicator](../../../../trading_strategy_tester/indicators/volatility/dc.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
DC_LOWER(
    ticker: str,
    length: int = 20,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period for the lowest low calculation. Default is 20.
- **`offset`** (`int`): Shifts the resulting series forward or backward. Default is 0.

---

## Description

- The lower Donchian Channel marks the lowest price observed over the last `length` periods.
- Helps identify potential support zones or breakout levels.

---

## Example Usage

```python
DC_LOWER(
    ticker="AAPL",
    length=20,
    offset=0
)
```
