# Trading Strategy Tester

A flexible Python package for simulating and evaluating algorithmic trading strategies with modular conditions, strategies, and trade simulations.

## Installation

To install the Trading Strategy Tester package, you can use pip:

```bash
pip install trading-strategy-tester
```

If you want to install the latest development version, you can clone the repository and install it locally:

```bash
git clone https://github.com/DrDanicka/trading_strategy_tester.git
```

## Documentation

The documentation is available in the `docs` directory. You can view it online at [this link](https://drdanicka.github.io/trading_strategy_tester/).

## Examples
You can find examples of how to use the package in the [`examples`](https://drdanicka.github.io/trading_strategy_tester/user/) tab of the user documentation. These examples cover various aspects of the package, including strategy creation, execution, and visualization or using technical indicators.

## LLM Integration

The project integrates with Large Language Models (LLMs) to help generate trading strategies from natural language descriptions. It provides a user-friendly interface for generating via web UI.

This project uses `Llama 3.2` models via [Ollama](https://ollama.com) framework. The models are fine-tuned on a custom dataset of trading strategies and their natural language descriptions. For running the project with LLM integration follow these steps:

1. Install Ollama on your machine from [here](https://ollama.com/download).
2. Clone this meta-repository with backend and frontend.
```bash
git clone --recurse-submodules https://github.com/DrDanicka/trading_strategy_tester_docker.git
```
3. Navigate to the `trading_strategy_tester_docker` directory and build the Docker image:
```bash
cd trading_strategy_tester_docker
docker-compose up --build 
```
Note: Building the image may take some time, because it downloads the weights of the Llama models.
4. Open your web browser and navigate to `http://localhost:5001` to access the web UI.