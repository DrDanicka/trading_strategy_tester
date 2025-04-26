
# `TradeCommissions` Classes

These classes define how trade costs are calculated. Trade commissions are applied to each trade, affecting the overall profit or loss.

The `TradeCommissions` class is an abstract base class, and its subclasses define specific commission structures.

```python
class TradeCommissions(ABC):
    
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def get_commission(self, invested: float, contracts: float) -> float:
        pass

    def to_dict(self):
        return {'value': self.value}
```

### Methods:
- **`get_commission(invested: float, contracts: float) -> float`**:  
  Calculates the commission based on the invested amount and number of contracts. Returns the commission amount.
- **`to_dict()`**:  
  Serializes the commission object into a dictionary for testing purposes.

## `MoneyCommissions`

Fixed commission per trade in dollars.

```python
MoneyCommissions(value: float)
```

- **`value`** (`float`): Flat dollar amount commission per trade.

### Example Usage

```python
Strategy(
    ...
    trade_commissions = MoneyCommissions(5.0)
)
```

This configures the strategy to apply a $5 commission for each trade executed.

---

## `PercentageCommissions`

Commission based on a percentage of the trade's value.

```python
PercentageCommissions(value: float)
```

- **`value`** (`float`): Commission percentage.

### Example Usage

```python
Strategy(
    ...
    trade_commissions = PercentageCommissions(0.1)
)
```
This configures the strategy to apply a 0.1% commission on the value of each trade executed.
