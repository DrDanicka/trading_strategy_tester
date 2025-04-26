
# `OBV` — On Balance Volume Trading Series

The `OBV` trading series represents the On Balance Volume (OBV) indicator, which accumulates volume based on price direction to measure buying and selling pressure.

It is built upon the [On Balance Volume indicator](../../../../trading_strategy_tester/indicators/volume/obv.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
OBV(
    ticker: str
)
```

- **`ticker`** (`str`): Asset ticker symbol.

---

## Description

- OBV rises when price closes higher and volume is added.
- OBV falls when price closes lower and volume is subtracted.
- Helps confirm price trends based on volume flow.

---

## Example Usage

```python
OBV(
    ticker="AAPL"
)
```
