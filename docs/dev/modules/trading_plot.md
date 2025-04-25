
# `TradingPlot` — Visualizing Trading Conditions Module

The `trading_plot` module defines an extensible interface for visualizing the behavior of trading conditions over time using `Plotly`. Each condition in your strategy can return a `TradingPlot` object to represent relevant market signals graphically.

---

## Abstract Base: `TradingPlot`

```python
class TradingPlot(ABC):
    
    @abstractmethod
    def get_plot(self, dark: bool) -> go.Figure:
        pass
        
    @abstractmethod
    def shift(self, days_to_shift: int):
        pass
    
    def show_plot(self, dark: bool):
        ...
```

### Description

This abstract base class provides a consistent interface for all condition-related visual plots:
- `get_plot(dark: bool)` → Required: Generates the actual Plotly figure.
- `shift(days_to_shift: int)` → Required: Allows time-based adjustment of plot data.
- `show_plot(dark: bool)` → Default: Displays the generated plot with a clean, user-friendly layout.

---

## Module Structure

The module includes specialized subclasses for various trading conditions:

| File | Condition Visualization |
|------|--------------------------|
| `cross_over_plot.py` | CrossOverCondition |
| `cross_under_plot.py` | CrossUnderCondition |
| `greater_than_plot.py` | GreaterThanCondition |
| `less_than_plot.py` | LessThanCondition |
| `downtrend_plot.py` | DowntrendForXDaysCondition |
| `uptrend_plot.py` | UptrendForXDaysCondition |
| `change_of_x_percent_per_y_days_plot.py` | ChangeOfXPercentPerYDaysCondition |
| `price_plot.py` | Generic price visualization |

Logical conditions (`AND`, `OR`) are not visualized directly but they populate the `TradingPlot` objects of their child conditions.

Every strategy returns a dictionary of `TradingPlot` objects, which can be accessed via the `get_graphs` method of the condition. The dictionary keys are: `PRICE`, `BUY`, and `SELL`. 
