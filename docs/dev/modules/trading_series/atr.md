
# `ATR` — Average True Range Trading Series

The `ATR` trading series represents the Average True Range (ATR) indicator, which measures market volatility by decomposing the entire range of an asset price for a given period.

It is built upon the [ATR indicator](../../../../trading_strategy_tester/indicators/volatility/atr.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
ATR(
    ticker: str,
    length: int = 14,
    smoothing_type: SmoothingType = SmoothingType.RMA
)
```

- **`ticker`** (`str`):  
  The symbol of the asset (e.g., `"AAPL"`).

- **`length`** (`int`):  
  The number of periods over which to calculate the ATR. Default is 14, a common setting in technical analysis.

- **`smoothing_type`** (`SmoothingType`):  
  The type of smoothing applied to the true range. Default is RMA (Running Moving Average), but other types like SMA, EMA or WMA can also be used.

---

## Description

- The ATR is a volatility indicator showing how much an asset moves, on average, during a given time frame.
- A rising ATR indicates increased volatility; a falling ATR suggests decreased volatility.
- ATR is often used to position size adjustments, stop loss calculations, or as a volatility filter in trading strategies.

---

## Example Usage

```python
ATR(
    ticker="AAPL",
    length=14,
    smoothing_type=SmoothingType.RMA
)
```

This creates an ATR Trading Series for AAPL using a 14-period length and RMA smoothing by default.
