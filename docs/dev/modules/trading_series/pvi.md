
# `PVI` — Positive Volume Index Trading Series

The `PVI` trading series represents the Positive Volume Index (PVI), which tracks price changes on days when volume increases.

It is built upon the [Positive Volume Index indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volume/pvi.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
PVI(
    ticker: str
)
```

- **`ticker`** (`str`): Asset ticker symbol.

---

## Description

- Focuses on days when trading volume increases compared to the prior day.
- Helps identify bullish market activity driven by mass participation.

---

## Example Usage

```python
PVI(
    ticker="AAPL"
)
```
