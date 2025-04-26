
# `UO` — Ultimate Oscillator Trading Series

The `UO` trading series represents the Ultimate Oscillator (UO), which combines short, medium, and long-term price movements to avoid false divergence signals.

It is built upon the [Ultimate Oscillator indicator](../../../../trading_strategy_tester/indicators/momentum/uo.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
UO(
    ticker: str,
    fast_length: int = 7,
    middle_length: int = 14,
    slow_length: int = 28
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`fast_length`** (`int`): Fastest period (default 7).
- **`middle_length`** (`int`): Middle period (default 14).
- **`slow_length`** (`int`): Slowest period (default 28).

---

## Description

- Values above 70 suggest overbought conditions.
- Values below 30 suggest oversold conditions.
- Designed to improve divergence signal reliability compared to other oscillators.

---

## Example Usage

```python
UO(
    ticker="AAPL",
    fast_length=7,
    middle_length=14,
    slow_length=28
)
```
