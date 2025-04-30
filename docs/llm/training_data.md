
# Training Data Module

The `training_data` module is responsible for generating synthetic and structured datasets used to fine-tune language models for the purpose of understanding and generating trading strategies.
It produces prompt-response pairs useful for supervised fine-tuning.

---

## Module Structure

- [**`training_data.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/training_data.py)  
  Entry point for generating complete training datasets, combining all individual components.

- [**`prompt_builder.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/training_data.py)  
  Constructs natural language prompts from structured strategy definitions.

- [**`condition_generator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/condition_generator.py)  
  Randomly generates valid strategy entry/exit conditions.

- [**`interval_generator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/interval_generator.py)  
  Supplies typical time intervals defined [here](../dev/modules/enums/interval.md).

- [**`stop_loss_take_profit_generator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/stop_loss_take_profit_generator.py)  
  Generates stop-loss and take-profit configurations.

- [**`capital_size_commission_generator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/capital_size_commission_generator.py)  
  Produces initial capita, order size and commission configurations.

- [**`strategy_type_generator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/strategy_type_generator.py)  
  Defines whether the strategy is long-only, short-only, or both using [`PositionTypeEnum`](../dev/modules/enums/position_type.md).

- [**`start_end_date_generator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/start_end_date_generator.py)  
  Sets up historical date ranges for backtests.

- [**`ticker_generator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/ticker_generator.py)
  Randomly selects from a pool of ticker symbols. Tickers are defined in [`sp500.csv`](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/prompt_data/sp500.csv).

---

## `prompt_data/` Submodule

- [**`condition_dicts.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/prompt_data/condition_dicts.py)  
  Provides mappings of condition types and corresponding indicators.

- [**`string_options.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/prompt_data/string_options.py)  
  Contains sets of predefined string values from which to randomly select to generate prompts.

- [**`sp500.csv`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/prompt_data/sp500.csv))  
  A list of S&P 500 tickers used by the `ticker_generator`.

---

## How It Works

The module is designed to be highly modular. You can:
- Use each generator individually
- Combine them via `training_data.py` to create full training examples
- Set random seeds for reproducibility

---

## What does it generate?

Vie the `training_data.py` module, you can generate a dataset of prompt-response pairs. Every time you call the `generate_trading_data()` function, it will create a new dataset with the specified number of examples. It always creates **prompt** that is a text in natural language and **response** to the prompt extracting from the prompt:

- Whole Strategy object
- Ticker
- Position Type
- Conditions
- Stop Loss
- Take Profit
- Start Date
- End Date
- Interval
- Period
- Initial Capital
- Order Size
- Trade Commissions

All of those datasets are saved as `.jsonl` files and used for fine-tuning the models.