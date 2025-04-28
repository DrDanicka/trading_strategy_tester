
# `HAMMER` — Hammer Candlestick Pattern Trading Series

The `HAMMER` trading series detects the Hammer candlestick pattern, a potential bullish reversal pattern appearing after a downtrend.

It is built upon the [Hammer pattern detection](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/candlestick_patterns/hammer.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
HAMMER(
    ticker: str
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).

---

## Description

- The Hammer is characterized by a small real body and a long lower shadow.
- It indicates potential exhaustion of selling pressure and a possible trend reversal to the upside.

---

## Example Usage

```python
HAMMER(
    ticker="AAPL"
)
```
