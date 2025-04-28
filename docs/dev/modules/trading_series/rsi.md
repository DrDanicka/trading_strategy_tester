
# `RSI` — Relative Strength Index Trading Series

The `RSI` trading series represents the Relative Strength Index (RSI), a momentum oscillator that measures the speed and change of price movements.

It is built upon the [RSI indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/rsi.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
RSI(
    ticker: str,
    source: SourceType = SourceType.CLOSE,
    length: int = 14
)
```

- **`ticker`** (`str`): Asset ticker symbol.
- **`source`** (`SourceType`): Price source for calculation. Default is `SourceType.CLOSE`. Supported sources are linked [here](../enums/source.md).
- **`length`** (`int`): Lookback period for RSI calculation. Default is 14.

---

## Description

- RSI above 70 often indicates overbought conditions.
- RSI below 30 often indicates oversold conditions.
- Helps identify potential reversal points and trend strength.

---

## Example Usage

```python
RSI(
    ticker="AAPL",
    source=SourceType.CLOSE,
    length=14
)
```
