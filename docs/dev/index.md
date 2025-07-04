# Documentation for Developers

Welcome to the **Developer Documentation** for the Trading Strategy Tester.

This section is intended for contributors, maintainers, or anyone interested in the internal workings of the project. Here you'll find detailed explanations of the architecture, core modules, and guidelines on how to extend or integrate the system.

---

## Python package Structure

The project is organized into the following key modules:

- [**`download`**](modules/download.md): Handles downloading and managing historical market data.
- [**`strategy`**](modules/strategy.md): Defines trading strategies and how they execute trades.
- [**`conditions`**](modules/conditions/index.md): Contains logic for entry and exit conditions used in strategies.
- [**`trading_series`**](modules/trading_series.md): Manages time series data used during backtesting.
- [**`trading_plot`**](modules/trading_plot.md): Provides tools for visualizing trading performance and signals.
- [**`indicators`**](modules/indicators.md): Implements technical indicators commonly used in strategies.
- [**`trade`**](modules/trade.md): Represents individual trades and their properties.
- [**`statistics`**](modules/statistics.md): Calculates performance metrics such as profit, drawdown, win rate, etc.

---
