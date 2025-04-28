
# `DPO` — Detrended Price Oscillator Trading Series

The `DPO` trading series represents the Detrended Price Oscillator, used to remove long-term trends from prices and focus on short-term cycles.

It is built upon the [Detrended Price Oscillator indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/trend/dpo.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
DPO(
    ticker: str,
    length: int = 20
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period to detrend the price series. Default is 20.

---

## Description

- Helps identify short-term cycles without the influence of larger trends.
- Useful for timing entries and exits based on price oscillations.

---

## Example Usage

```python
DPO(
    ticker="AAPL",
    length=20
)
```
