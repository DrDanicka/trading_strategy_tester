# `AROON_DOWN` — Aroon Down Trading Series

The `AROON_DOWN` trading series represents the Aroon Down indicator, which measures how long it has been since the lowest low during a specified period. It is primarily used to detect the strength of a downtrend.

It is built upon the [Aroon Down indicator](../../../../trading_strategy_tester/indicators/trend/aroon.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
AROON_DOWN(
    ticker: str,
    length: int = 14
)
```

- **`ticker`** (`str`):  
  The symbol of the asset (e.g., `"AAPL"`).

- **`length`** (`int`):  
  The number of periods over which to calculate the Aroon Down indicator. Default is 14.

---

## Description

- Values close to 100 indicate a strong downtrend.
- Values near 0 suggest a weak or non-existent downtrend.
- Often used alongside the Aroon Up indicator to detect trend reversals.

---

## Example Usage

```python
AROON_DOWN(
    ticker="AAPL",
    length=14
)
```

This creates an Aroon Down Trading Series for AAPL using a 14-period lookback window.
