
# Trend Conditions

Trend conditions evaluate whether a price or indicator series is in a sustained uptrend or downtrend over a specified number of days. These conditions are useful for capturing momentum and trend-following strategy logic.

All trend conditions inherit from the base `Condition` class and implement the standard `evaluate`, `get_graphs`, and `to_dict` methods.

---

## `UptrendForXDaysCondition`

Returns `True` if the specified trading series is in an uptrend for a consecutive number of days.

### **Arguments**
```python
UptrendForXDaysCondition(series: TradingSeries, number_of_days: int)
```

- `series`: A trading series (indicator or price) to evaluate.
- `number_of_days`: Number of consecutive days where the condition must hold for the trend to be confirmed.

---

## `DowntrendForXDaysCondition`

Returns `True` if the specified trading series is in a downtrend for a consecutive number of days.

### **Arguments**
```python
DowntrendForXDaysCondition(series: TradingSeries, number_of_days: int)
```

- `series`: A trading series (indicator or price) to evaluate.
- `number_of_days`: Number of consecutive days where the condition must hold for the trend to be confirmed.

---

## Examples

```python
condition = UptrendForXDaysCondition(
    series=EMA("AAPL", SourceType.CLOSE, 20, 0),
    number_of_days=5
)
```

This example triggers if the 20-day EMA of AAPL has been increasing for the past 5 days.

```python
condition = DowntrendForXDaysCondition(
    series=CLOSE("AAPL"),
    number_of_days=3
)
```

This example triggers if the closing price of AAPL has been falling for 3 consecutive days.
