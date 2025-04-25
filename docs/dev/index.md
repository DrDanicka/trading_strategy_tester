# Developer Documentation

Welcome to the **Developer Documentation** for the Trading Strategy Tester.

This section is intended for contributors, maintainers, or anyone interested in the internal workings of the project. Here you'll find detailed explanations of the architecture, core modules, and guidelines on how to extend or integrate the system.

---

## Project Structure

The project is organized into the following key modules:

- [**`download`**](modules/download.md): Handles downloading and managing historical market data.
- [**`strategy`**](modules/strategy.md): Defines trading strategies and how they execute trades.
- [**`conditions`**](modules/conditions/index.md): Contains logic for entry and exit conditions used in strategies.
- [**`trading_series`**](modules/trading_series.md): Manages time series data used during backtesting.
- **`trading_plot`**: Provides tools for visualizing trading performance and signals.
- [**`indicators`**](modules/indicators.md): Implements technical indicators commonly used in strategies.
- **`trade`**: Represents individual trades and their properties.
- **`statistics`**: Calculates performance metrics such as profit, drawdown, win rate, etc.

---

## Large Language Model (LLM) Integration

The project integrates with Large Language Models (LLMs) to help generate and optimize trading strategies from natural language descriptions.

Two main techniques are used:

### Fine-tuning

Fine-tuning involves taking a pre-trained model and training it further on a custom dataset. This allows the model to specialize in interpreting and generating trading strategy code.

The dataset consists of natural language strategy descriptions paired with their code implementations. It is created using the `training_dataset` module.

### Retrieval-Augmented Generation (RAG)

RAG enhances language model outputs by retrieving relevant information from a knowledge base during generation. In this project, RAG is used to inject context (e.g., existing strategy documentation or indicator definitions) into the LLM’s response.

The knowledge base is generated from the project’s internal documentation and strategy schema.

---