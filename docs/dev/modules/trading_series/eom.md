
# `EOM` — Ease of Movement Trading Series

The `EOM` trading series represents the Ease of Movement indicator, which combines price and volume to measure the ease with which an asset's price moves.

It is built upon the [Ease of Movement indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volume/eom.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
EOM(
    ticker: str,
    length: int = 14,
    divisor: int = 10_000
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Period for smoothing the raw Ease of Movement calculation. Default is 14.
- **`divisor`** (`int`): Divisor applied to reduce scaling issues. Default is 10,000.

---

## Description

- EOM measures how much volume is required to move prices.
- High positive values suggest easy upward movement; low negative values suggest easy downward movement.

---

## Example Usage

```python
EOM(
    ticker="AAPL",
    length=14,
    divisor=10_000
)
```
