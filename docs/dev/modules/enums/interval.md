
# `Interval` Enum

The `Interval` enum defines commonly used time intervals for fetching and aggregating financial or time-series data. These intervals are typically used when specifying the resolution of historical price data in trading strategies.

---

## Enum Import

```python
from trading_strategy_tester.enums.interval_enum import Interval
```

---

## Members

- `Interval.ONE_DAY` — `'1d'`  
  Represents a 1-day interval. Commonly used for daily price charts.

- `Interval.FIVE_DAYS` — `'5d'`  
  Represents a 5-day interval. Useful for shorter-term swing strategies.

- `Interval.ONE_WEEK` — `'1wk'`  
  Represents a 1-week interval. Smooths out daily volatility.

- `Interval.ONE_MONTH` — `'1mo'`  
  Represents a 1-month interval. Good for longer-term or macro strategies.

- `Interval.THREE_MONTHS` — `'3mo'`  
  Represents a 3-month interval. Used for broad trend analysis or quarterly cycles.

---

## Usage Example

```python
strategy = Strategy(
    ticker="AAPL",
    interval=Interval.ONE_DAY,
    ...
)
```

This will configure the strategy to operate on daily interval data.
