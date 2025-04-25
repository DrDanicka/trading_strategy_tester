
# Parameterized Conditions

Parameterized conditions evaluate changes in indicators or price over specified timeframes or intervals. These conditions enable more dynamic, time-sensitive logic in trading strategies.

All parameterized conditions inherit from the base `Condition` class and implement the standard `evaluate`, `get_graphs`, and `to_dict` methods.

---

## `AfterXDaysCondition`

Returns `True` if a given condition has been satisfied before a specified number of days.

### **Arguments**
```python
AfterXDaysCondition(condition: Condition, number_of_days: int)
```

- `condition`: The base condition to track.
- `number_of_days`: Number of days after which the condition should be evaluated.

---

## `ChangeOfXPercentPerYDaysCondition`

Checks if the given series has changed by a specified percentage over a given number of days.

### **Arguments**
```python
ChangeOfXPercentPerYDaysCondition(series: TradingSeries, percent: float, number_of_days: int)
```

- `series`: The price or indicator series to evaluate.
- `percent`: The percentage change threshold.
- `number_of_days`: The number of days over which the change is evaluated.

---

## `IntraIntervalChangeOfXPercentCondition`

Checks if the percentage change within a single interval defined by the strategy exceeds a threshold.

### **Arguments**
```python
IntraIntervalChangeOfXPercentCondition(series: TradingSeries, percent: float)
```

- `series`: The price or indicator series to evaluate.
- `percent`: The threshold percentage for the change to trigger the condition.

---

## Examples

```python
condition = ChangeOfXPercentPerYDaysCondition(
    series=CLOSE("AAPL"),
    percent=5.0,
    number_of_days=10
)
```

This condition evaluates `True` if AAPL's close has changed by at least 5% over the last 10 days.

```python
condition = AfterXDaysCondition(
    condition=CrossOverCondition(EMA("AAPL", SourceType.CLOSE, 10, 0), CONST(150)),
    number_of_days=3
)
```

This condition evaluates `True` if AAPL's 10-day EMA has crossed above 150 3 days ago.
