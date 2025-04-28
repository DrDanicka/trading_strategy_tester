
# `CHAIKIN_OSC` — Chaikin Oscillator Trading Series

The `CHAIKIN_OSC` trading series represents the Chaikin Oscillator, which measures the momentum of the Accumulation/Distribution Line of an asset.

It is built upon the [Chaikin Oscillator indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volume/chaikin_osc.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
CHAIKIN_OSC(
    ticker: str,
    fast_length: int = 3,
    slow_length: int = 10
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`fast_length`** (`int`): Fast EMA period. Default is 3.
- **`slow_length`** (`int`): Slow EMA period. Default is 10.

---

## Description

- The Chaikin Oscillator calculates the difference between the 3-day and 10-day EMAs of the Accumulation/Distribution Line.
- Positive values suggest buying pressure; negative values suggest selling pressure.
- Useful for detecting shifts in money flow before price movements.

---

## Example Usage

```python
CHAIKIN_OSC(
    ticker="AAPL",
    fast_length=3,
    slow_length=10
)
```
