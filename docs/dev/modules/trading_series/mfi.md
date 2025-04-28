# `MFI` — Money Flow Index Trading Series

The `MFI` trading series represents the Money Flow Index, a momentum indicator that uses price and volume to identify overbought or oversold conditions.

It is built upon the [Money Flow Index indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volume/mfi.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
MFI(
    ticker: str,
    length: int = 14
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Period for MFI calculation. Default is 14.

---

## Description

- MFI readings above 80 typically indicate overbought conditions.
- MFI readings below 20 typically indicate oversold conditions.
- Combines price and volume for momentum analysis.

---

## Example Usage

```python
MFI(
    ticker="AAPL",
    length=14
)
```
