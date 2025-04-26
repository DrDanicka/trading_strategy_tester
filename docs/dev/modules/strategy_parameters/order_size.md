# `OrderSize` Class

These classes determine how much capital is allocated to each trade. `OrderSize` is an abstract base class, and its subclasses define specific order sizing strategies.

```python
class OrderSize(ABC):

    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        pass

    def to_dict(self):
        return {'value': self.value}
```

## Methods:

- **`get_invested_amount(share_price: float, current_capital: float) -> (float, float)`**:  
  Calculates the amount to invest based on the share price and current capital. Returns a tuple of the invested amount and the number of shares/contracts.
- **`to_dict()`**:  
  Serializes the order size object into a dictionary for testing purposes.

## `USD`

Fixed dollar amount allocated to each trade. Partition shares will be used when dollar amount is not divisible by share price.

```python
USD(value: float)
```

- **`value`** (`float`): Dollar amount for the trade.

### Example Usage

```python
Strategy(
    ...
    order_size = USD(1000)
)
```
## `Contracts`

Fixed number of contracts/shares per trade.

```python
Contracts(value: float)
```

- **`value`** (`float`): Number of contracts or shares.

### Example Usage

```python
Strategy(
    ...
    order_size = Contracts(1)
)
```

`Contracts(1)` is also set as a default value in the `Strategy` class. This means that if no order size is specified, one contract will be used by default in every trade.

---

## `PercentOfEquity`

Dynamic sizing based on the current equity price. If the equity price is $100 and the order size is 10%, then $10 will be allocated to the trade.

```python
PercentOfEquity(value: float)
```

- **`value`** (`float`): Percentage of equity to allocate per trade.

### Example Usage

```python
Strategy(
    ...
    order_size = PercentOfEquity(50)
)
```

---