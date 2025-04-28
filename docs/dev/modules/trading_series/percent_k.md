
# `STOCH_PERCENT_K` — Stochastic %K Trading Series

The `STOCH_PERCENT_K` trading series represents the raw %K line of the Stochastic Oscillator, showing the current closing price relative to the high-low range over a set period.

It is built upon the [Stochastic Oscillator %K indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/stoch.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
STOCH_PERCENT_K(
    ticker: str,
    length: int = 14
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`length`** (`int`): Lookback period for %K calculation. Default is 14.

---

## Description

- %K shows the position of the close price relative to the high-low range.
- Often combined with [%D](percent_d.md) to generate trading signals.

---

## Example Usage

```python
STOCH_PERCENT_K(
    ticker="AAPL",
    length=14
)
```
