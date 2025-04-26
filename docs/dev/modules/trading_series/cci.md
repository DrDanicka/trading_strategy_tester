
# `CCI` — Commodity Channel Index Trading Series

The `CCI` trading series represents the Commodity Channel Index (CCI), an oscillator that measures the variation of an asset's price from its statistical mean.

It is built upon the [CCI indicator](../../../../trading_strategy_tester/indicators/momentum/cci.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
CCI(
    ticker: str,
    source: SourceType = SourceType.HLC3,
    length: int = 20
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): Price source to calculate CCI. Default is `SourceType.HLC3`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for CCI calculation. Default is 20.

---

## Description

- CCI values above +100 may indicate overbought conditions.
- CCI values below -100 may indicate oversold conditions.
- CCI can be used to spot trend reversals, overbought/oversold levels, and strength of trends.

---

## Example Usage

```python
CCI(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20
)
```
