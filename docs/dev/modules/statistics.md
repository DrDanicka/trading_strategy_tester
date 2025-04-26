
# `Statistics` — Strategy Performance Metrics Calculation

The `get_strategy_stats` function calculates key performance statistics for a trading strategy based on a list of executed trades and historical market data.

---

## Function Signature

```python
get_strategy_stats(
    trades: list[Trade],
    df: pd.DataFrame,
    initial_capital: float,
    order_size: OrderSize
) -> dict
```

---

## Parameters

- **`trades`** (`list[Trade]`):  
  List of executed `Trade` objects, each representing a simulated trade.

- **`df`** (`pd.DataFrame`):  
  Market data used to calculate additional metrics like Buy-and-Hold returns.

- **`initial_capital`** (`float`):  
  The amount of starting capital at the beginning of the backtest.

- **`order_size`** (`OrderSize`):  
  The method for determining position sizing across trades. Supported OrderSizes are linked [here](strategy_parameters/order_size.md)

---

## Returned Statistics

The function returns a dictionary with the following metrics:

| Metric | Description | Units |
|:-------|:------------|:------|
| `Net Profit` | Total profit or loss from all trades | Dollars ($) |
| `Gross Profit` | Total profits from winning trades only | Dollars ($) |
| `Gross Loss` | Total losses from losing trades only | Dollars ($) |
| `Profit factor` | Ratio of Gross Profit to Gross Loss | Unitless |
| `Sharpe Ratio` | Risk-adjusted return based on trade P&L | Unitless |
| `Max Drawdown` | Maximum observed loss from a peak to a trough | Dollars ($) |
| `Buy and Hold Return` | Profit/loss if simply holding from start to end | Dollars ($) |
| `Buy and Hold Return Percentage` | Buy-and-hold return as a percent | Percentage (%) |
| `Commissions Paid` | Total commissions across all trades | Dollars ($) |
| `Total Trades` | Total number of trades executed | Count |
| `Number of Winning Trades` | Number of profitable trades | Count |
| `Number of Losing Trades` | Number of losing trades | Count |
| `Average Trade` | Average P&L per trade | Dollars ($) |
| `Largest Winning Trade` | Largest single winning trade | Dollars ($) |
| `Largest Losing Trade` | Largest single losing trade | Dollars ($) |
| `P&L` | Total profit and loss | Dollars ($) |
| `P&L Percentage` | Total profit and loss relative to initial capital | Percentage (%) |

---

## Notes

- Sharpe Ratio is computed based on trade-level returns, not daily returns.
- Commissions are subtracted from each trade's result when calculating final stats.
- If fewer than two trades exist, or trade P&L has zero standard deviation, Sharpe Ratio will be shown as `-`.
- Profit Factor is shown as `-` if there were no losses (gross loss = 0).

---
