
# `CCI_SMOOTHENED` — Smoothened Commodity Channel Index Trading Series

The `CCI_SMOOTHENED` trading series represents a smoothed version of the Commodity Channel Index (CCI), offering a less noisy view of price movements.

It is built upon the [CCI Smoothened indicator](../../../../trading_strategy_tester/indicators/momentum/cci.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
CCI_SMOOTHENED(
    ticker: str,
    source: SourceType = SourceType.HLC3,
    length: int = 20,
    smoothing_type: SmoothingType = SmoothingType.RMA,
    smoothing_length: int = 5
)
```

- **`ticker`** (`str`):
Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): 
 Price source to calculate CCI. Default is `SourceType.HLC3`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for base CCI calculation. Default is 20.
- **`smoothing_type`** (`SmoothingType`): Type of smoothing applied to the CCI. Default is `SmoothingType.RMA`. Supported smoothing types are linked [here](../enums/smoothing.md).
- **`smoothing_length`** (`int`): Period of smoothing. Default is 5.

---

## Description

- Helps reduce noise compared to regular CCI.
- Better suited for longer-term strategies and smoother signal generation.

---

## Example Usage

```python
CCI_SMOOTHENED(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20,
    smoothing_type=SmoothingType.RMA,
    smoothing_length=5
)
```
