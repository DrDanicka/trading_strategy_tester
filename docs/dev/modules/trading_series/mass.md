# `MASS_INDEX` — Mass Index Trading Series

The `MASS_INDEX` trading series measures the range expansion between high and low prices to identify potential reversals.

It is built upon the [Mass Index indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/trend/mass.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
MASS_INDEX(
    ticker: str,
    length: int = 10
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`length`** (`int`): Period for smoothing the range. Default is 10.

---

## Description

- A Mass Index greater than 27 often signals a potential trend reversal.
- Uses a ratio of EMAs of the price range.

---

## Example Usage

```python
MASS_INDEX(
    ticker="AAPL",
    length=10
)
```
