
# `PositionTypeEnum` Enum

The `PositionTypeEnum` defines the types of market positions a trading strategy can take. This determines whether the strategy will buy (long), sell short (short), or potentially do both depending on the logic.

---

## Enum Import

```python
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
```

---

## Members

- `PositionTypeEnum.LONG` — `'LONG'`  
  Represents a **long** position. The strategy buys an asset expecting its price to increase.

- `PositionTypeEnum.SHORT` — `'SHORT'`  
  Represents a **short** position. The strategy sells an asset expecting its price to decrease.

- `PositionTypeEnum.LONG_SHORT_COMBINED` — `'LONG_SHORT_COMBINED'`  
  The strategy can take both long and short positions — either at the same time or based on separate conditions.

---

## Usage Example

```python
strategy = Strategy(
    ticker="AAPL",
    position_type=PositionTypeEnum.LONG,
    ...
)
```

This configures the strategy to take long positions only.
