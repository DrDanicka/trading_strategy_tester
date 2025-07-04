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

The project integrates with Large Language Models to help generate trading strategies from natural language descriptions. It is available in 2 types:

1. **WEB UI**: A web-based interface that allows users to input natural language prompts and visualize the results. You can find can learn more about the web app in this [repository](https://github.com/DrDanicka/trading_strategy_tester_web_app?tab=readme-ov-file).
2. **Code interface**: You can use the LLM integration directly in your Python code. This can be done via `process_prompt(prompt: str, llm_model: LLMModel)` function. You can do it like this:

```python
from trading_strategy_tester import process_prompt, LLMModel

trades, graphs, stats, strategy_obj, changes = process_prompt(
    prompt="""Can you generate a long strategy for LULU that goes long when the Open Price is in a negative trend for 77 days
        and price is within a 50% fibonacci level during an uptrend is correct and sells out when the Know Sure Thing varies by
        65.99 percent over 62 days is fulfilled. Set trailing stop-loss at 27.52%. Set the start date as 2013-12-13. Set the 
        interval to 5 days. Set trade commissions to 5%.""",
    llm_model=LLMModel.LLAMA_ALL
)
```

You can later use the `trades`, `graphs`, `stats`, `strategy_obj`, and `changes` variables to visualize the results, analyze the performance, and make further modifications to the strategy.

This project uses `Llama 3.2` models via [Ollama](https://ollama.com) framework. The models need to be installed first so that the package can use them. Follow these steps:
1. You need to install `Ollama` on your machine using this [link](https://ollama.com/download).
2. After that, you have to download the [model weights](https://huggingface.co/drdanicka/trading-strategy-tester-weights/tree/main). You can do the following:

```bash
git clone https://github.com/DrDanicka/trading_strategy_tester_web_app
cd trading_strategy_tester_web_app
python init_ollama.py
```
This will download and initialize the `Ollama` models. After all of this is done, you can delete the `trading_strategy_tester_web_app` directory if you want to.

Now you can use the `process_prompt` function to generate trading strategies from natural language prompts.

To learn more about how to write prompts, and LLM integration in general, you can check the [LLM Integration documentation](https://drdanicka.github.io/trading_strategy_tester/llm/).