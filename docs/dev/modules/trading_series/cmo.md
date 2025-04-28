
# `CMO` — Chande Momentum Oscillator Trading Series

The `CMO` trading series represents the Chande Momentum Oscillator (CMO), which measures momentum on both the upside and downside over a specified period.

It is built upon the [Chande Momentum Oscillator indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/cmo.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
CMO(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    length: int = 20
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): Price source to calculate the CMO. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for the CMO calculation. Default is 20.

---

## Description

- CMO oscillates between -100 and +100.
- High positive values suggest strong upward momentum.
- High negative values suggest strong downward momentum.
- Helps identify overbought and oversold conditions.

---

## Example Usage

```python
CMO(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20
)
```
