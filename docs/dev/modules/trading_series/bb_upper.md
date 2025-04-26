
# `BB_UPPER` — Bollinger Band Upper Trading Series

The `BB_UPPER` trading series represents the Upper Bollinger Band, calculated using a specified moving average and a standard deviation multiplier. It defines the upper boundary of the expected price range.

It is built upon the [Bollinger Bands indicator](../../../../trading_strategy_tester/indicators/volatility/bb.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
BB_UPPER(
    ticker: str,
    source: SourceType,
    length: int = 20,
    ma_type: SmoothingType = SmoothingType.SMA,
    std_dev: float = 2,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): The price type to use. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Number of periods for the moving average. Default is 20.
- **`ma_type`** (`SmoothingType`): Moving average type. Default is `SmoothingType.SMA`. Supported smoothing types are linked [here](../enums/smoothing.md).
- **`std_dev`** (`float`): Number of standard deviations for the band. Default is 2.
- **`offset`** (`int`): Shifts the band forwards/backwards. Default is 0.

---

## Description

- The upper Bollinger Band typically represents potential **resistance levels**.
- A close above the upper band may indicate an overbought condition or strong upside momentum.

---

## Example Usage

```python
BB_UPPER(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20,
    ma_type=SmoothingType.SMA,
    std_dev=2,
    offset=0
)
```
