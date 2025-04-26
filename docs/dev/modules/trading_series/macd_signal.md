
# `MACD_SIGNAL` — MACD Signal Line Trading Series

The `MACD_SIGNAL` trading series represents the signal line of the MACD indicator, which is typically a smoothed version of the MACD itself.

It is built upon the [MACD Signal indicator](../../../../trading_strategy_tester/indicators/momentum/macd.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
MACD_SIGNAL(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    fast_length: int = 12,
    slow_length: int = 26,
    oscillator_ma_type: SmoothingType = SmoothingType.EMA,
    signal_ma_type: SmoothingType = SmoothingType.EMA,
    signal_length: int = 9
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`source`** (`SourceType`): Price source. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`fast_length`** (`int`): Fast EMA length. Default is 12.
- **`slow_length`** (`int`): Slow EMA length. Default is 26.
- **`oscillator_ma_type`** (`SmoothingType`): MA type for the MACD oscillator. Default is `SmoothingType.EMA`. Supported types are linked [here](../enums/smoothing.md).
- **`signal_ma_type`** (`SmoothingType`): MA type for the signal line. Default is `SmoothingType.EMA`. Supported types are linked [here](../enums/smoothing.md).
- **`signal_length`** (`int`): Smoothing period for the signal line. Default is 9.

---

## Description

- Signal line helps generate buy/sell signals via crossovers with MACD.

---

## Example Usage

```python
MACD_SIGNAL(
    ticker="AAPL",
    source=SourceType.CLOSE,
    fast_length=12,
    slow_length=26,
    oscillator_ma_type=SmoothingType.EMA,
    signal_ma_type=SmoothingType.EMA,
    signal_length=9
)
```
