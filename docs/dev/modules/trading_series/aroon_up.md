# `AROON_UP` — Aroon Up Trading Series

The `AROON_UP` trading series represents the Aroon Up indicator, which measures how long it has been since the highest high during a specified period. It is primarily used to detect the strength of an uptrend.

It is built upon the [Aroon Up indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/trend/aroon.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
AROON_UP(
    ticker: str,
    length: int = 14
)
```

- **`ticker`** (`str`): The symbol of the asset (e.g., `"AAPL"`).

- **`length`** (`int`): The number of periods over which to calculate the Aroon Up indicator. Default is 14.

---

## Description

- Values close to 100 indicate a strong uptrend.
- Values near 0 suggest a weak or non-existent uptrend.
- Often used alongside the Aroon Down indicator to detect trend reversals.

---

## Example Usage

```python
AROON_UP(
    ticker="AAPL",
    length=14
)
```

This creates an Aroon Up Trading Series for AAPL using a 14-period lookback window.
