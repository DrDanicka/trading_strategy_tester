
# `MOMENTUM` — Momentum Indicator Trading Series

The `MOMENTUM` trading series represents a simple momentum oscillator, calculating the difference between the current price and the price `length` periods ago.

It is built upon the [Momentum indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/momentum.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
MOMENTUM(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    length: int = 10
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): Price source for calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for momentum calculation. Default is 10.

---

## Description

- Positive values indicate upward momentum.
- Negative values indicate downward momentum.
- Useful for identifying trend strength and direction.

---

## Example Usage

```python
MOMENTUM(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=10
)
```
