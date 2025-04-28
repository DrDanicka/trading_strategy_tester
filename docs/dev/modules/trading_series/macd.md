
# `MACD` — Moving Average Convergence Divergence Trading Series

The `MACD` trading series represents the classic MACD indicator, which shows the relationship between two moving averages of a security’s price.

It is built upon the [MACD indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/macd.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
MACD(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    fast_length: int = 12,
    slow_length: int = 26,
    ma_type: SmoothingType = SmoothingType.EMA
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): Price source for the calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`fast_length`** (`int`): Lookback for the fast moving average. Default is 12.
- **`slow_length`** (`int`): Lookback for the slow moving average. Default is 26.
- **`ma_type`** (`SmoothingType`): Type of moving average used. Default is `SmoothingType.EMA`. Supported types are linked [here](../enums/smoothing.md).

---

## Description

- Shows the difference between a fast EMA and a slow EMA.
- Useful for identifying trend changes and momentum.

---

## Example Usage

```python
MACD(
    ticker="AAPL",
    source=SourceType.CLOSE,
    fast_length=12,
    slow_length=26,
    ma_type=SmoothingType.EMA
)
```
