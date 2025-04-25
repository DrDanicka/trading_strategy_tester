
# `BB_LOWER` — Bollinger Band Lower Trading Series

The `BB_LOWER` trading series represents the Lower Bollinger Band, calculated using a specified moving average and a standard deviation multiplier. It defines the lower boundary of the expected price range.

It is built upon the [Bollinger Bands indicator](../../../../trading_strategy_tester/indicators/volatility/bb.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
BB_LOWER(
    ticker: str,
    source: SourceType,
    length: int = 20,
    ma_type: SmoothingType = SmoothingType.SMA,
    std_dev: float = 2,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): The price type to use (Close, Open, etc.).
- **`length`** (`int`): Number of periods for the moving average. Default is 20.
- **`ma_type`** (`SmoothingType`): Moving average type. Default is Simple Moving Average (SMA).
- **`std_dev`** (`float`): Number of standard deviations for the band. Default is 2.
- **`offset`** (`int`): Shifts the band forwards/backwards. Default is 0.

---

## Description

- The lower Bollinger Band typically represents potential **support levels**.
- A close below the lower band may indicate an oversold condition or strong downside momentum.

---

## Example Usage

```python
BB_LOWER(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20,
    ma_type=SmoothingType.SMA,
    std_dev=2,
    offset=0
)
```
