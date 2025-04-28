
# `KC_UPPER` — Keltner Channel Upper Band Trading Series

The `KC_UPPER` trading series represents the upper band of the Keltner Channel, based on a moving average and the Average True Range (ATR).

It is built upon the [Keltner Channel indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volatility/kc.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
KC_UPPER(
    ticker: str,
    source: SourceType,
    length: int = 20,
    multiplier: int = 2,
    use_exp_ma: bool = True,
    atr_length: int = 10
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`source`** (`SourceType`): Price source used for moving average. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Period for the moving average. Default is 20.
- **`multiplier`** (`int`): Multiplier applied to ATR. Default is 2.
- **`use_exp_ma`** (`bool`): Use EMA instead of SMA. Default is `True`.
- **`atr_length`** (`int`): ATR lookback period. Default is 10.

---

## Description

- The upper Keltner Channel serves as a dynamic resistance level.
- The channel expands/contracts based on volatility via ATR.

---

## Example Usage

```python
KC_UPPER(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20,
    multiplier=2,
    use_exp_ma=True,
    atr_length=10
)
```
