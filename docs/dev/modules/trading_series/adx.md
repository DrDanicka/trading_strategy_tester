
# `ADX` — Average Directional Index Trading Series

The `ADX` trading series represents the Average Directional Index (ADX), a popular indicator that measures the strength of a trend, without regard to its direction. Higher ADX values indicate a stronger trend.

It is built upon the [ADX indicator](../../../../trading_strategy_tester/indicators/trend/adx.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
ADX(
    ticker: str,
    smoothing_length: int = 14,
    length: int = 14
)
```

- **`ticker`** (`str`): The symbol of the asset (e.g., `"AAPL"`).
  
- **`smoothing_length`** (`int`): Number of periods used for smoothing the ADX line. Default is 14, which is a common setting in technical analysis.
  
- **`length`** (`int`): The lookback period over which the +DI and -DI are calculated before smoothing. Default is 14, which is a common setting in technical analysis.

---

## Description

The Average Directional Index is used to quantify the strength of a trend.
- ADX above 25 generally indicates a strong trend.
- ADX below 20 may suggest a weak trend or range-bound market.
- It does not indicate the direction of the trend — only the strength.

---

## Example Usage

```python
ADX(
    ticker="AAPL",
    smoothing_length=14,
    length=14
)
```
This creates an ADX Trading Series for AAPL using a 14-period length and 14-period smoothing. Using get_data() and passing a downloader instance and a DataFrame will return the ADX values for the specified ticker.
