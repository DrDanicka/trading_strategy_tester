
# `STOCH_PERCENT_D` — Stochastic %D Trading Series

The `STOCH_PERCENT_D` trading series represents the smoothed %D line of the Stochastic Oscillator.

It is built upon the [Stochastic Oscillator %D indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/stoch.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
STOCH_PERCENT_D(
    ticker: str,
    length: int = 14,
    smoothing_length: int = 3
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`length`** (`int`): Lookback period for the initial %K calculation. Default is 14.
- **`smoothing_length`** (`int`): Smoothing period for %D calculation. Default is 3.

---

## Description

- %D is a smoothed version of [%K](percent_k.md).
- Helps smooth out noise and identify crossover signals.

---

## Example Usage

```python
STOCH_PERCENT_D(
    ticker="AAPL",
    length=14,
    smoothing_length=3
)
```
