
# `KC_LOWER` — Keltner Channel Lower Band Trading Series

The `KC_LOWER` trading series represents the lower band of the Keltner Channel, based on a moving average and the Average True Range (ATR).

It is built upon the [Keltner Channel indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/volatility/kc.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
KC_LOWER(
    ticker: str,
    source: SourceType = SouceType.CLOSE,
    length: int = 20,
    multiplier: int = 2,
    use_exp_ma: bool = True,
    atr_length: int = 10
)
```

- **`ticker`** (`str`): Asset ticker symbol (e.g., `"AAPL"`).
- **`source`** (`SourceType`): Price source used for moving average. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Period for the moving average. Default is 20.
- **`multiplier`** (`int`): Multiplier applied to the ATR for band width. Default is 2.
- **`use_exp_ma`** (`bool`): Whether to use an Exponential Moving Average (EMA) instead of SMA. Default is `True`.
- **`atr_length`** (`int`): Period for ATR calculation. Default is 10.

---

## Description

- The lower Keltner Channel typically serves as dynamic support.
- Built around an ATR-enveloped moving average.

---

## Example Usage

```python
KC_LOWER(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=20,
    multiplier=2,
    use_exp_ma=True,
    atr_length=10
)
```
