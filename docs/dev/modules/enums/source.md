
# `SourceType` Enum

The `SourceType` enum defines the different types of price or volume sources used in indicator calculations and condition evaluations. These are commonly passed as parameters to `TradingSeries` classes like `RSI`, `EMA`, `BB_UPPER`, etc.

---

## Enum Import

```python
from trading_strategy_tester.enums.source_enum import SourceType
```

---

## Members

- `SourceType.CLOSE` — `'Close'`  
  The closing price of the instrument.

- `SourceType.OPEN` — `'Open'`  
  The opening price of the instrument.

- `SourceType.HIGH` — `'High'`  
  The highest price reached during the period.

- `SourceType.LOW` — `'Low'`  
  The lowest price reached during the period.

- `SourceType.HLC3` — `'HLC3'`  
  The average of the High, Low, and Close: `(High + Low + Close) / 3`.

- `SourceType.HL2` — `'HL2'`  
  The average of the High and Low: `(High + Low) / 2`.

- `SourceType.OHLC4` — `'OHLC4'`  
  The average of Open, High, Low, and Close: `(Open + High + Low + Close) / 4`.

- `SourceType.HLCC4` — `'HLCC4'`  
  Weighted average of High, Low, and twice the Close: `(High + Low + 2 * Close) / 4`.

- `SourceType.VOLUME` — `'Volume'`  
  The trading volume for the instrument.

---

## Usage Example

```python
rsi_series = RSI(ticker="AAPL", source=SourceType.CLOSE, length=14)
```

This configures an RSI series to use closing prices for its calculation.
