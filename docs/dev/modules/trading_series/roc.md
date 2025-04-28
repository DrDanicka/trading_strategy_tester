
# `ROC` — Rate of Change Trading Series

The `ROC` trading series represents the Rate of Change (ROC) indicator, which measures the percentage change between the current price and the price `length` periods ago.

It is built upon the [Rate of Change indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/roc.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
ROC(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    length: int = 9
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): Price source for calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for ROC calculation. Default is 9.

---

## Description

- Positive ROC indicates upward momentum.
- Negative ROC indicates downward momentum.
- Useful for identifying momentum shifts and trend reversals.

---

## Example Usage

```python
ROC(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=9
)
```
