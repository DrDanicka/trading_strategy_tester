
# Threshold Conditions

Threshold conditions compare two values or series and return a boolean result based on specific criteria such as crossing, being greater than, or being less than. These are foundational for building rule-based entries and exits in trading strategies.

All threshold conditions inherit from the base `Condition` class and implement the standard `evaluate`, `get_graphs`, and `to_dict` methods.

---

## `CrossOverCondition`

Triggers when the first series crosses **above** the second series.

### **Arguments**
```python
CrossOverCondition(first_series: TradingSeries, second_series: TradingSeries)
```

- `first_series`: Trading series which can be an indicator or price series.
- `second_series`: The reference series to compare against.

---

## `CrossUnderCondition`

Triggers when the first series crosses **below** the second series.

### **Arguments**
```python
CrossUnderCondition(first_series: TradingSeries, second_series: TradingSeries)
```

- `first_series`: Trading series which can be an indicator or price series.
- `second_series`: The reference series to compare against.

---

## `GreaterThanCondition`

Returns `True` when the first series is **strictly greater than** the second series.

### **Arguments**
```python
GreaterThanCondition(first_series: TradingSeries, second_series: TradingSeries)
```

- `first_series`: Trading series which can be an indicator or price series.
- `second_series`: The reference series to compare against.

---

## `LessThanCondition`

Returns `True` when the first series is **strictly less than** the second series.

### **Arguments**
```python
LessThanCondition(first_series: TradingSeries, second_series: TradingSeries)
```

- `first_series`: Trading series which can be an indicator or price series.
- `second_series`: The reference series to compare against.

---

## Examples

```python
condition =CrossOverCondition(
    first_series=RSI("AAPL", SourceType.CLOSE, 14),
    second_series=CONST(30)
)
```

This example triggers if RSI crosses above 30.

```python
condition=LessThanCondition(
    first_series=CLOSE("AAPL"),
    second_series=BB_LOWER("AAPL", SourceType.CLOSE, 20, SmoothingType.SMA, 2, 0)
)
```

This example triggers if Close price is below the lower Bollinger Band.