
# `DC_UPPER` — Donchian Channel Upper Band Trading Series

The `DC_UPPER` trading series represents the upper band of the Donchian Channel, calculated as the highest high over a specified period.

It is built upon the [Donchian Channel indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volatility/dc.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
DC_UPPER(
    ticker: str,
    length: int = 20,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period for the highest high calculation. Default is 20.
- **`offset`** (`int`): Shifts the resulting series forward or backward. Default is 0.

---

## Description

- The upper Donchian Channel marks the highest price observed over the last `length` periods.
- Useful for spotting breakout opportunities and setting resistance zones.

---

## Example Usage

```python
DC_UPPER(
    ticker="AAPL",
    length=20,
    offset=0
)
```
