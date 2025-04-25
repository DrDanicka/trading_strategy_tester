
# Logical Conditions

Logical conditions are used to combine multiple other conditions using boolean logic. They allow you to construct complex condition trees that can be evaluated as part of a trading strategy.

All logical conditions inherit from the base `Condition` class and implement the standard `evaluate`, `get_graphs`, and `to_dict` methods.

---

## `AND`

Combines two or more conditions and returns `True` only if **all** of them are satisfied at the same time.

### **Arguments**
```python
AND(*conditions: Condition)
```

- `conditions`: A variable number of `Condition` instances to be combined with logical AND.

---

## `OR`

Combines two or more conditions and returns `True` if **any** of them are satisfied.

### **Arguments**
```python
OR(*conditions: Condition)
```

- `conditions`: A variable number of `Condition` instances to be combined with logical OR.

---

## Example

```python
condition = AND(
    CrossOverCondition(
        first_series=SMA("AAPL", SourceType.CLOSE, 50),
        second_series=SMA("AAPL", SourceType.CLOSE, 200)
    ),
    GreaterThanCondition(
        first_series=RSI("AAPL", SourceType.CLOSE, 14),
        second_series=CONST(30)
    )
)
```

This example evaluates if the 50-SMA has crossed above the 200-SMA and the RSI is above 30.
