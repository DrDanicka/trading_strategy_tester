
# `KST` — Know Sure Thing Oscillator Trading Series

The `KST` trading series represents the Know Sure Thing (KST) oscillator, a momentum indicator that sums smoothed rate of change values.

It is built upon the [Know Sure Thing indicator](../../../../trading_strategy_tester/indicators/momentum/kst.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
KST(
    ticker: str,
    source: SourceType,
    roc_length_1: int,
    roc_length_2: int,
    roc_length_3: int,
    roc_length_4: int,
    sma_length_1: int,
    sma_length_2: int,
    sma_length_3: int,
    sma_length_4: int
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`source`** (`SourceType`): Price source for calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`roc_length_1/2/3/4`** (`int`): Rate of Change periods.
- **`sma_length_1/2/3/4`** (`int`): SMA periods applied to each ROC.

---

## Description

- Summation of four weighted smoothed ROC values.
- A smoother momentum oscillator designed to reduce noise.

---

## Example Usage

```python
KST(
    ticker="AAPL",
    source=SourceType.CLOSE,
    roc_length_1=10,
    roc_length_2=15,
    roc_length_3=20,
    roc_length_4=30,
    sma_length_1=10,
    sma_length_2=10,
    sma_length_3=10,
    sma_length_4=15
)
```
