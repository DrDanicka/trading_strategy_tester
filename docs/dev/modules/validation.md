
# Validation Module

The `validation` module is responsible for ensuring that trading strategies and their parameters are correctly defined before execution. This helps prevent simulation errors and enforces logical consistency across strategies.

Main objective of this module is to validate outputs from the LLMs (large language models) and ensure that the strategies are executable. It checks for required fields, correct types and syntax. In some cases when it's possible to fix the output by obeying not required fields, the model will do it. 

This module is composed of two main parts:
- Validation of entire strategies
- Validation of individual parameters

---

## Structure

- [**`implemented_objects.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/implemented_objects.py)
  - Defines supported indicators, conditions, and other elements that are allowed in strategy definitions.

- [**`strategy_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/strategy_validator.py)
  - Provides functionality to validate the overall structure of a trading strategy, ensuring that required fields are present and correctly configured. It provides this functionality by function `validate_strategy_string(strategy_str: str, logs: bool = False)` which takes a strategy string and returns a boolean indicating whether the strategy is valid or not. It also returns a dictionary of errors or changes made to the strategy string.

- [**`parameter_validations/`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/)
  - Contains specialized validators for different types of parameters:
    - [**`order_size_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/order_size_validator.py): Validates order size parameters.
    - [**`stop_loss_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/stop_loss_validator.py): Validates stop loss settings.
    - [**`take_profit_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/take_profit_validator.py): Validates take profit settings.
    - [**`ticker_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/ticker_validator.py): Ensures ticker symbols are valid.
    - [**`date_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/date_validator.py): Checks the validity of start and end dates.
    - [**`period_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/period_validator.py): Validates time periods.
    - [**`capital_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/capital_validator.py): Ensures initial capital settings are realistic.
    - [**`position_type_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/position_type_validator.py): Validates if the strategy is for long/short/both positions.
    - [**`interval_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/interval_validator.py): Ensures the trading interval is properly defined.
    - [**`trade_commissions_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/trade_commissions_validator.py): Validates trade commission structures.
    - [**`condition_validator.py`**](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/validation/parameter_validations/condition_validator.py): Verifies that trading conditions are syntactically and logically correct.

---

## How It Works

1. **Strategy Validation:**
   - The `strategy_validator` reads a strategy definition and checks:
     - All required fields are present.
     - Fields conform to expected types and value ranges.
     - Conditions reference only implemented indicators or functions.

2. **Parameter Validation:**
   - Each parameter (e.g., stop loss, ticker, capital) is independently validated by its corresponding validator module.
   - This modular approach allows for flexible extension if new parameters are introduced.

---