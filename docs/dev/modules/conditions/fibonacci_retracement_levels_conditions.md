
# Fibonacci Retracement Conditions

Fibonacci retracement conditions are used to detect price reactions at key Fibonacci levels during uptrends or downtrends. These are commonly used in technical analysis to identify potential reversal or continuation zones.

All Fibonacci retracement conditions inherit from the base `Condition` class and implement the standard `evaluate`, `get_graphs`, and `to_dict` methods.

---

## `UptrendFibRetracementLevelCondition`

Returns `True` if the price pulls back to a specified Fibonacci level during an uptrend.

### **Arguments**
```python
UptrendFibRetracementLevelCondition(fib_level: FibonacciLevels, length: int)
```

- `fib_level`: The Fibonacci level to test. Supported levels are linked [here](TODO ADD LINK TO FIB LEVELS).
- `length`: Lookback period for detecting the local swing high and low.

---

## `DowntrendFibRetracementLevelCondition`

Returns `True` if the price bounces back to a specified Fibonacci level during a downtrend.

### **Arguments**
```python
DowntrendFibRetracementLevelCondition(fib_level: FibonacciLevels, length: int)
```

- `fib_level`: The Fibonacci level to test. Supported levels are linked [here](TODO ADD LINK TO FIB LEVELS).
- `length`: Lookback period for detecting the local swing high and low.

---

## Examples

```python
condition = UptrendFibRetracementLevelCondition(
    fib_level=FibonacciLevels.LEVEL_50,
    length=20
)
```

This condition is met if the price retraces to the 50% Fibonacci level during an uptrend over the past 20 days.

```python
condition = DowntrendFibRetracementLevelCondition(
    fib_level=FibonacciLevels.LEVEL_61_8,
    length=30
)
```

This condition is met if the price retraces to the 61.8% Fibonacci level during a downtrend over the last 30 days.
