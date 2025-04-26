
# `Trade` Module

The `trade` module works as a summary of a single trade, including entry and exit details, trade size, and commission effects. It is designed to have all the necessary information to calculate the profit or loss of a trade.

---

# `Trade` Class

The `Trade` class encapsulates the execution of a single trade, including entry and exit details, trade size, and commission effects.

## Parameters (Constructor)

```python
Trade(
    df_slice: pd.DataFrame,
    trade_id: int,
    order_size: OrderSize,
    current_capital: float,
    initial_capital: float,
    trade_commissions: TradeCommissions,
    long: bool = True
)
```

- **`df_slice`** (`pd.DataFrame`):  
  DataFrame slice containing the data for the trade. This is typically a subset of the historical data used for backtesting.

- **`trade_id`** (`int`):  
  Unique identifier for the trade. This is used to track the trade throughout the backtesting process.

- **`order_size`** (`OrderSize`):  
  Object defining how much capital is allocated to the trade. Supported order sizes are linked [here](strategy_parameters/order_size.md).

- **`current_capital`** (`float`):  
  Current capital available for trading. This is updated as trades are executed.

- **`initial_capital`** (`float`):  
  Capital available when the trade was initiated.

- **`trade_commissions`** (`TradeCommissions`):  
  Object describing commissions applied to each trade. Supported commission types are linked [here](strategy_parameters/trade_commissions.md).

- **`long`** (`bool`):  
  Indicates whether the trade is a long position. Default is `True`. If `False`, the trade is considered a short position.

---

Trade objects are returned in a list as a result of the `Strategy` class. The list contains all trades executed during the backtest.
