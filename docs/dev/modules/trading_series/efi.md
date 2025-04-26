
# `EFI` — Elder Force Index Trading Series

The `EFI` trading series represents the Elder Force Index, a volume-based momentum indicator that quantifies buying and selling pressure.

It is built upon the [Elder Force Index indicator](../../../../trading_strategy_tester/indicators/volume/efi.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
EFI(
    ticker: str,
    length: int = 13
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`): Period for smoothing the raw Force Index. Default is 13.

---

## Description

- Positive EFI values indicate buying pressure.
- Negative EFI values indicate selling pressure.
- Combines price change and volume for a powerful momentum signal.

---

## Example Usage

```python
EFI(
    ticker="AAPL",
    length=13
)
```
