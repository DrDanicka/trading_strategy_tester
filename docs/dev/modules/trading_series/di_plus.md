
# `DI_PLUS` — Positive Directional Indicator (+DI) Trading Series

The `DI_PLUS` trading series represents the Positive Directional Indicator (+DI), a component of the ADX system that measures upward price movement strength.

It is built upon the [Directional Movement Index (+DI)](../../../../trading_strategy_tester/indicators/trend/adx.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
DI_PLUS(
    ticker: str,
    length: int = 14
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period to calculate the +DI. Default is 14.

---

## Description

- Higher +DI values suggest stronger upward movement.
- Often combined with -DI and ADX to assess overall trend strength and direction.

---

## Example Usage

```python
DI_PLUS(
    ticker="AAPL",
    length=14
)
```
