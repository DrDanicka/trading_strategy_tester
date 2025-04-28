
# `DI_MINUS` — Negative Directional Indicator (-DI) Trading Series

The `DI_MINUS` trading series represents the Negative Directional Indicator (-DI), a component of the ADX system that measures downward price movement strength.

It is built upon the [Directional Movement Index (-DI)](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/trend/adx.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
DI_MINUS(
    ticker: str,
    length: int = 14
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Lookback period to calculate the -DI. Default is 14.

---

## Description

- Higher -DI values suggest stronger downward movement.
- Often combined with +DI and ADX to assess overall trend strength and direction.

---

## Example Usage

```python
DI_MINUS(
    ticker="AAPL",
    length=14
)
```
