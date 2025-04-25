
# `FibonacciLevels` Enum

The `FibonacciLevels` enum defines commonly used Fibonacci retracement levels used in technical analysis. These levels help identify potential support and resistance zones based on historical price swings.

---

## Enum Import

```python
from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels
```

### Members

- `FibonacciLevels.LEVEL_0`

  The 0% retracement level. Represents no retracement.

- `FibonacciLevels.LEVEL_23_6`

  A shallow retracement level often observed in fast-moving trends.

- `FibonacciLevels.LEVEL_38_2`

  A moderate retracement level commonly used to detect pullbacks.

- `FibonacciLevels.LEVEL_50`

  A psychological midpoint level. While not from the Fibonacci sequence, it's widely used.

- `FibonacciLevels.LEVEL_61_8`

  The **Golden Ratio**, considered one of the most critical levels in technical analysis.

- `FibonacciLevels.LEVEL_100`

  Represents a full retracement of the prior move.

---

## Usage Example

```python
condition = UptrendFibRetracementLevelCondition(
    fib_level=FibonacciLevels.LEVEL_61_8,
    length=20
)
```

This sets a condition for a retracement to the 61.8% Fibonacci level in an uptrend based on the last 20 days of price action.
