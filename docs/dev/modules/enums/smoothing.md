
# `SmoothingType` Enum

The `SmoothingType` enum defines the available smoothing techniques for moving average calculations in technical indicators. These methods help reduce noise and identify trends in time series data.

---

## Enum Import

```python
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
```

---

## Enum Members

- `SmoothingType.RMA` — `'RMA'`  
  **Running Moving Average**. Also known as Wilder’s Moving Average. It gives more weight to older values than EMA.

- `SmoothingType.SMA` — `'SMA'`  
  **Simple Moving Average**. Unweighted mean of the previous N data points.

- `SmoothingType.EMA` — `'EMA'`  
  **Exponential Moving Average**. Applies exponentially decreasing weights to past data points, giving more importance to recent values.

- `SmoothingType.WMA` — `'WMA'`  
  **Weighted Moving Average**. Assigns a linear weight to each value in the series, with recent data weighted more heavily.

---

## Usage Example

```python
atr_series = ATR(ticker='AAPL', length=14, smoothing_type=SmoothingType.EMA)
```

This example shows how to use the `SmoothingType` enum when creating an ATR (Average True Range) indicator instance. The `SmoothingType.EMA` option specifies that the Exponential Moving Average should be used for smoothing the ATR values.
