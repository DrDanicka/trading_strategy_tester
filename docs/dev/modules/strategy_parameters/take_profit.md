
# `TakeProfit` — Take Profit Module

The `TakeProfit` object defines a take profit mechanism for trades, used to automatically exit a position when a gain threshold is achieved.

It is implemented in the [take_profit.py](../../../../trading_strategy_tester/conditions/stoploss_takeprofit/take_profit.py) file.

It takes into account the position type and calculates the profit level for long and short trades differently.

---

## Parameters

```python
TakeProfit(
    percentage: float
)
```

- **`percentage`** (`float`):  
  The minimum profit percentage needed to trigger a take profit exit (e.g., 0.05 for 5%).

---

## Description

- A **Take Profit** exits the position when the trade's price appreciates by a set percentage from the entry price.
- Helps lock in gains before a potential reversal.

---

## Example Usage

```python
TakeProfit(
    percentage=5
)
```

This sets a take profit target at 5% above the entry price.
