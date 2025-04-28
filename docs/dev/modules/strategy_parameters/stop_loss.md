
# `StopLoss` — Stop Loss Condition

The `StopLoss` object defines a stop loss mechanism for trades, used to automatically exit a position when a loss threshold is breached.

It is implemented in the [stop_loss.py](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/conditions/stoploss_takeprofit/stop_loss.py) module.

Stop loss takes into account the position type and calculates the loss level for long and short trades differently.

---

## Parameters

```python
StopLoss(
    percentage: float,
    stop_loss_type: StopLossType
)
```

- **`percentage`** (`float`):  
  The maximum allowable loss as a percentage of the entry price (e.g., 0.02 for 2%).

- **`stop_loss_type`** (`StopLossType`):  
  Type of stop loss. Supported types are linked [here](#stop-loss-types).
    - `NORMAL` — Traditional fixed stop loss.
    - `TRAILING` — Trailing stop loss that moves in favor of the trade.

---

## Description

- A **Normal Stop Loss** exits the position if price falls a fixed percentage from the entry.
- A **Trailing Stop Loss** follows the price if it moves favorably and locks in gains while maintaining a loss threshold.

---

## Example Usage

```python
StopLoss(
    percentage=3,
    stop_loss_type=StopLossType.TRAILING
)
```

This sets a 3% trailing stop loss on a trade.

# Stop Loss Types

The `StopLossType` enum defines the types of stop loss mechanisms available for trades. This determines how the stop loss is applied and managed during the trade.

## Enum Import

```python
from trading_strategy_tester.enums.stop_loss_type_enum import StopLossType
```

## Members
- `StopLossType.NORMAL` — `'NORMAL'`  
  Represents a **normal stop loss**. The stop loss is fixed at a certain percentage below the entry price.
- `StopLossType.TRAILING` — `'TRAILING'`  
  Represents a **trailing stop loss**. The stop loss moves in favor of the trade, locking in profits as the price increases.
