
# `KST_SIGNAL` — KST Signal Line Trading Series

The `KST_SIGNAL` trading series represents the signal line for the Know Sure Thing (KST) oscillator.

It is built upon the [Know Sure Thing Signal indicator](../../../../trading_strategy_tester/indicators/momentum/kst.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
KST_SIGNAL(
    ticker: str,
    source: SourceType,
    roc_length_1: int,
    roc_length_2: int,
    roc_length_3: int,
    roc_length_4: int,
    sma_length_1: int,
    sma_length_2: int,
    sma_length_3: int,
    sma_length_4: int,
    signal_length: int
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`source`** (`SourceType`): Price source. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`roc_length_1/2/3/4`** (`int`): ROC periods.
- **`sma_length_1/2/3/4`** (`int`): SMA smoothing periods.
- **`signal_length`** (`int`): Length for signal line smoothing.

---

## Description

- Smoothed version of KST for generating crossover buy/sell signals.

---

## Example Usage

```python
KST_SIGNAL(
    ticker="AAPL",
    source=SourceType.CLOSE,
    roc_length_1=10,
    roc_length_2=15,
    roc_length_3=20,
    roc_length_4=30,
    sma_length_1=10,
    sma_length_2=10,
    sma_length_3=10,
    sma_length_4=15,
    signal_length=9
)
```
