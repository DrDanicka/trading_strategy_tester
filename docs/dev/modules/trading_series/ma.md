
# Moving Average Trading Series

This module provides two core types of moving averages used widely in technical analysis: Simple Moving Average (SMA) and Exponential Moving Average (EMA).

---

# `SMA` - Simple Moving Average Trading Series

The `SMA` trading series represents the Simple Moving Average, calculated as the unweighted mean of the previous `length` data points.

## Parameters

```python
SMA(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    length: int = 20,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): Price source for calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for the average calculation. Default is 20.
- **`offset`** (`int`): Shifts the series forward/backward. Default is 0.

## Description

- SMA gives equal weight to all values.
- Smooths price data and is useful for trend identification.

## Example Usage

```python
SMA(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20,
    offset=0
)
```

---

# `EMA` - Exponential Moving Average Trading Series

The `EMA` trading series represents the Exponential Moving Average, which applies greater weight to more recent data points.

## Parameters

```python
EMA(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    length: int = 20,
    offset: int = 0
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`source`** (`SourceType`): Price source for calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for calculation. Default is 20.
- **`offset`** (`int`): Shifts the series forward/backward. Default is 0.

## Description

- EMA reacts more quickly to recent price changes compared to SMA.
- Often used for dynamic trend-following strategies.

## Example Usage

```python
EMA(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20,
    offset=0
)
```
