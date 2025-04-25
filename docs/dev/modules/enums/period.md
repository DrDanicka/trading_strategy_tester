
# `Period` Enum

The `Period` enum defines common time spans over which historical data can be requested or analyzed. These are typically used in trading strategy backtesting and financial data aggregation.

---

## Enum Import

```python
from trading_strategy_tester.enums.period_enum import Period
```

---

## Members

- `Period.ONE_DAY` — `'1d'`  
  A 1-day period.

- `Period.FIVE_DAYS` — `'5d'`  
  A 5-day period.

- `Period.ONE_MONTH` — `'1mo'`  
  A 1-month period.

- `Period.THREE_MONTHS` — `'3mo'`  
  A 3-month period.

- `Period.SIX_MONTHS` — `'6mo'`  
  A 6-month period.

- `Period.ONE_YEAR` — `'1y'`  
  A 1-year period.

- `Period.TWO_YEARS` — `'2y'`  
  A 2-year period.

- `Period.FIVE_YEARS` — `'5y'`  
  A 5-year period.

- `Period.TEN_YEARS` — `'10y'`  
  A 10-year period.

- `Period.YEAR_TO_DATE` — `'ytd'`  
  Year-to-date period.

- `Period.MAX` — `'max'`  
  The maximum available data period.

- `Period.NOT_PASSED` — `'not_passed'`  
  Indicates that no period was explicitly passed. Used as a fallback to date range (`start_date`, `end_date`).

---

## Usage Example

```python
strategy = Strategy(
    ticker="AAPL",
    period=Period.ONE_YEAR,
    ...
)
```

This configures the strategy to run using 1 year of historical data.
