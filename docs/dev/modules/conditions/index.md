
# `conditions` — Strategy Condition Module

This module defines the various condition classes used to create complex entry and exit logic in trading strategies. These conditions are categorized into logical, threshold-based, trend-following, Fibonacci retracement and parameterized (time/value-based) mechanisms.

All condition classes inherit from the base `Condition` class, which provides a common interface for evaluating conditions against time series data.

Abstract `Condition` class has the following methods:

```python
class Condition(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def evaluate(self, data: pd.DataFrame) -> pd.Series:
        pass

    @abstractmethod
    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
```

As a condition is evaluated over a time series, it returns a boolean series indicating whether the condition is satisfied at each point in time. These boolean series can be combined using logical conditions to create complex strategies and are stored in the `pd.DataFrame`.

---

## Module Structure

### [1. Logical Conditions](logical_conditions.md)
*Located in [`trading_strategy_tester/conditions/logical_conditions/`](../../../../trading_strategy_tester/conditions/logical_conditions)*

- [`AND`](logical_conditions.md#and) — Combines multiple conditions using logical AND
- [`OR`](logical_conditions.md#or) — Combines multiple conditions using logical OR

---

### [2. Threshold Conditions](threshold_conditions.md)
*Located in [`trading_strategy_tester/conditions/threshold_conditions/`](../../../../trading_strategy_tester/conditions/threshold_conditions)*

- [`CrossOverCondition`](threshold_conditions.md#crossovercondition) — Condition when one series crosses over another
- [`CrossUnderCondition`](threshold_conditions.md#crossundercondition) — Condition when one series crosses under another
- [`GreaterThanCondition`](threshold_conditions.md#greaterthancondition) — Checks if one series is greater than another
- [`LessThanCondition`](threshold_conditions.md#lessthancondition) — Checks if one series is less than another

---

### [3. Trend Conditions](trend_conditions.md)
*Located in [`trading_strategy_tester/conditions/trend_conditions/`](../../../../trading_strategy_tester/conditions/trend_conditions)*

- [`UptrendForXDaysCondition`](trend_conditions.md#uptrendforxdayscondition) — Detects uptrend over X consecutive days
- [`DowntrendForXDaysCondition`](trend_conditions.md#downtrendforxdayscondition) — Detects downtrend over X consecutive days

---

### [4. Fibonacci Retracement Conditions](fibonacci_retracement_levels_conditions.md)
*Located in [`trading_strategy_tester/conditions/fibonacci_retracement_levels_conditions/`](../../../../trading_strategy_tester/conditions/fibonacci_retracement_levels_conditions)*

- [`UptrendFibRetracementLevelCondition`](fibonacci_retracement_levels_conditions.md#uptrendfibretracementlevelcondition) — Uses Fibonacci levels during uptrend
- [`DowntrendFibRetracementLevelCondition`](fibonacci_retracement_levels_conditions.md#downtrendfibretracementlevelcondition) — Uses Fibonacci levels during downtrend

---

### [5. Parameterized Conditions](parameterized_conditions.md)
*Located in [`trading_strategy_tester/conditions/parameterized_conditions/`](../../../../trading_strategy_tester/conditions/parameterized_conditions)*

- [`AfterXDaysCondition`](parameterized_conditions.md#afterxdayscondition) — Triggers condition after X days of another condition
- [`ChangeOfXPercentPerYDaysCondition`](parameterized_conditions.md#changeofxpercentperydayscondition) — Checks percentage change over Y days
- [`IntraIntervalChangeOfXPercentCondition`](parameterized_conditions.md#intraintervalchangeofxpercentcondition) — Percentage change within a single interval chosen in the strategy definition

---

## Integration

Each condition class is typically used inside a `Strategy` object as a `buy_condition` or `sell_condition`. Conditions can be nested using logical conditions for complex rule-based strategies.
