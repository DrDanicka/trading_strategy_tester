
# `DC_BASIS` — Donchian Channel Basis Trading Series

The `DC_BASIS` trading series represents the middle line (basis) of the Donchian Channel, calculated as the average of the upper and lower bands.

It is built upon the [Donchian Channel indicator](../../../../trading_strategy_tester/indicators/volatility/dc.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
DC_BASIS(
    ticker: str,
    length: int = 20,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period for calculating the basis. Default is 20.
- **`offset`** (`int`): Shifts the resulting series forward or backward. Default is 0.

---

## Description

- The basis line represents the average price between the Donchian upper and lower bands.
- Can be used as a mean reversion reference or dynamic support/resistance.

---

## Example Usage

```python
DC_BASIS(
    ticker="AAPL",
    length=20,
    offset=0
)
```
