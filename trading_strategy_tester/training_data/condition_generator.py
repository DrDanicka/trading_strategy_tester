import random
from enum import Enum

# Import necessary enums and resources for building conditions
from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.training_data.prompt_data.condition_dicts import conditions_dict
from trading_strategy_tester.validation.implemented_objects import implemented_indicators
from trading_strategy_tester.training_data.prompt_data.string_options import parameter_equality_options

# Enum for different types of condition structures
class ConditionType(Enum):
    condition_with_2_trading_series = 1
    condition_with_trading_series_and_number = 2
    condition_with_trading_series_and_2_numbers = 3
    condition_with_trading_series_and_percentage = 4
    condition_with_fibonacci_levels = 5

def process_one_trading_series(rng: random.Random, ticker: str):
    """
    Randomly selects and builds one trading series configuration with its parameters.

    :param rng: Random number generator.
    :param ticker: The stock ticker symbol to use.
    :return: Tuple of (description text, parameter instantiation text).
    """
    trading_series_index = rng.randint(0, len(implemented_indicators) - 1)

    # Get a row of the trading series
    trading_series = implemented_indicators.iloc[trading_series_index]

    number_of_parameters_trading_series = len(trading_series['Parameters'].split()) - 1

    # Choose whether to use full indicator name or shortcut
    is_name_not_shortcut = rng.choice([True, False])
    chosen_trading_series = trading_series['Indicator'] if is_name_not_shortcut else trading_series['Shortcut']

    const_number = -1
    # Check if the trading series is a constant (CONST)
    if chosen_trading_series == '':
        const_number = rng.randint(1, 99)
        class_with_parameters = f"CONST({const_number}"
    else:
        class_with_parameters = f"{trading_series['Class_name']}('{ticker}'"

    parameter_values = []

    # Handle indicator parameters if applicable
    if number_of_parameters_trading_series > 0:
        number_of_parameters_trading_series = rng.randint(0, number_of_parameters_trading_series)

        # Randomly select parameters
        parameters = rng.sample(trading_series['Parameters'].split()[1:], k=number_of_parameters_trading_series)

        for parameter in parameters:
            parameter_name, parameter_type = parameter.split(':')
            if parameter_type == 'int':
                parameter_value = rng.randint(1, 99)
                parameter_values.append(
                    rng.choice(parameter_equality_options).format(name=parameter_name, value=parameter_value))
            elif parameter_type == 'float':
                parameter_value = round(rng.uniform(0.1, 99.9), 2)
                parameter_values.append(
                    rng.choice(parameter_equality_options).format(name=parameter_name, value=parameter_value))
            elif parameter_type == 'SmoothingType':
                parameter_value = rng.choice([
                    SmoothingType.SMA,
                    SmoothingType.EMA,
                    SmoothingType.RMA,
                    SmoothingType.WMA
                ])
                parameter_values.append(f'smoothing type set to {parameter_value.value}')
            elif parameter_type == 'SourceType':
                parameter_value = rng.choice([
                    SourceType.CLOSE,
                    SourceType.OPEN,
                    SourceType.HIGH,
                    SourceType.LOW,
                    SourceType.HLC3,
                    SourceType.HL2,
                    SourceType.OHLC4,
                    SourceType.HLCC4
                ])
                parameter_values.append(f'source set to {parameter_value.value}')
                parameter_value = str(parameter_value)
            elif parameter_type == 'bool':
                parameter_value = rng.choice([True, False])
                parameter_values.append(f'{parameter_name} is set to {parameter_value}')
            else:
                raise ValueError("Invalid parameter type")

            class_with_parameters += f', {parameter_name}={parameter_value}'

    # Build final text description
    final_text = chosen_trading_series \
        if const_number == -1 \
        else f'{rng.choice([const_number, f"{const_number} line", f"{const_number} level", f"line {const_number}"])}'

    if len(parameter_values) > 0:
        final_text += rng.choice([' where ', ' with ', ' having '])
        final_text += ', '.join(parameter_values)

    class_with_parameters += ')'

    return final_text, class_with_parameters

def create_condition(rng: random.Random, ticker: str):
    """
    Create a full trading condition, including text and parameters, based on random choices.

    :param rng: Random number generator.
    :param ticker: Stock ticker symbol.
    :return: Tuple of (condition text, condition parameter instantiation).
    """
    condition_type = rng.randint(1, len(conditions_dict))
    current_condition_dict = conditions_dict[condition_type]

    condition_number = rng.randint(1, len(conditions_dict[condition_type]))
    possible_texts, class_name = current_condition_dict[condition_number]

    # Handle condition types separately
    if condition_type == ConditionType.condition_with_2_trading_series.value:
        trading_series1_text, trading_series1_parameters = process_one_trading_series(rng, ticker)
        trading_series2_text, trading_series2_parameters = process_one_trading_series(rng, ticker)

        condition_text = rng.choice(possible_texts)
        condition_text = condition_text.format(indicator=trading_series1_text, value=trading_series2_text)

        condition_param = f"{class_name}(first_series={trading_series1_parameters}, second_series={trading_series2_parameters})"

    elif condition_type == ConditionType.condition_with_trading_series_and_number.value:
        trading_series_text, trading_series_parameters = process_one_trading_series(rng, ticker)

        condition_text = rng.choice(possible_texts)
        number_of_days = rng.randint(1, 99)
        condition_text = condition_text.format(indicator=trading_series_text, days=number_of_days)

        condition_param = f"{class_name}(series={trading_series_parameters}, number_of_days={number_of_days})"

    elif condition_type == ConditionType.condition_with_trading_series_and_2_numbers.value:
        trading_series_text, trading_series_parameters = process_one_trading_series(rng, ticker)

        condition_text = rng.choice(possible_texts)
        percent = round(rng.uniform(0.1, 99.9), 2)
        number_of_days = rng.randint(1, 99)
        condition_text = condition_text.format(indicator=trading_series_text, percent=percent, days=number_of_days)

        condition_param = f"{class_name}(series={trading_series_parameters}, percent={percent}, number_of_days={number_of_days})"

    elif condition_type == ConditionType.condition_with_trading_series_and_percentage.value:
        trading_series_text, trading_series_parameters = process_one_trading_series(rng, ticker)

        condition_text = rng.choice(possible_texts)
        percent = round(rng.uniform(0.1, 99.9), 2)
        condition_text = condition_text.format(indicator=trading_series_text, percent=percent)

        condition_param = f"{class_name}(series={trading_series_parameters}, percent={percent})"

    elif condition_type == ConditionType.condition_with_fibonacci_levels.value:
        condition_text = rng.choice(possible_texts)
        length = rng.randint(1, 100)
        level = rng.choice([
            FibonacciLevels.LEVEL_0,
            FibonacciLevels.LEVEL_23_6,
            FibonacciLevels.LEVEL_38_2,
            FibonacciLevels.LEVEL_50,
            FibonacciLevels.LEVEL_61_8,
            FibonacciLevels.LEVEL_100
        ])
        condition_text = condition_text.format(level=level.value, length=length)

        condition_param = f"{class_name}(fib_level={level}, length={length})"

    else:
        raise ValueError("Invalid condition type")

    # Optionally add \"after X days\" to condition
    insert_after_x_days = rng.choices([True, False], weights=[0.05, 0.95])[0]
    if insert_after_x_days:
        after_x_days = rng.randint(1, 99)
        condition_text = f"{condition_text} after {after_x_days} days"
        condition_param = f"AfterXDaysCondition(condition={condition_param}, number_of_days={after_x_days})"

    return condition_text, condition_param

def build_logical_expression(ops, words, params):
    """
    Build a logical expression combining multiple conditions with 'AND'/'OR'.

    :param ops: List of logical operators.
    :param words: List of condition texts.
    :param params: List of condition parameter strings.
    :return: Tuple of (logical text, logical parameters).
    """
    and_groups = []
    current_group = [params[0]]

    for i, op in enumerate(ops):
        if op == "and":
            current_group.append(params[i + 1])
        else:  # "or"
            and_groups.append(current_group if len(current_group) > 1 else current_group[0])
            current_group = [params[i + 1]]

    and_groups.append(current_group if len(current_group) > 1 else current_group[0])

    # Build parameters string
    if len(and_groups) == 1:
        logical_condition_params = (
            f"AND({', '.join(and_groups[0])})" if isinstance(and_groups[0], list) else and_groups[0]
        )
    else:
        logical_condition_params = f"OR({', '.join(['AND(' + ', '.join(group) + ')' if isinstance(group, list) else group for group in and_groups])})"

    # Build text string
    logical_condition_text = " ".join(word if i == 0 else f"{ops[i-1]} {word}" for i, word in enumerate(words))

    return logical_condition_text, logical_condition_params

def get_random_condition(rng: random.Random, up_to_n: int = 3, ticker: str = 'AAPL'):
    """
    Randomly generate a set of conditions connected by logical operators.

    :param rng: Random number generator.
    :param up_to_n: Maximum number of conditions.
    :param ticker: Stock ticker symbol.
    :return: Tuple of (full logical condition text, condition parameter string).
    """
    number_of_conditions = rng.randint(1, up_to_n)
    conditions_list = [create_condition(rng, ticker) for _ in range(number_of_conditions)]

    conditions_text_list = [condition[0] for condition in conditions_list]
    conditions_param_list = [condition[1] for condition in conditions_list]

    logical_operators = ['and', 'or']
    logical_operators_sequence = rng.choices(logical_operators, k=number_of_conditions - 1)

    condition_text, condition_param = build_logical_expression(logical_operators_sequence, conditions_text_list, conditions_param_list)

    return condition_text, condition_param
