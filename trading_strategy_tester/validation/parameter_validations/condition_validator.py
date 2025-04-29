import ast

from trading_strategy_tester.validation.implemented_objects import implemented_conditions, implemented_trading_series
from trading_strategy_tester.validation.parameter_validations.ticker_validator import validate_ticker

# Utility to find the expected type of a given parameter name
def get_expected_type(param_name, param, param_type):
    """
    Get the expected type for a given parameter name.
    """
    if param_name in param:
        index = param.index(param_name)
        expected_type = param_type[index]
    else:
        expected_type = None

    return expected_type

# Utility to merge two dictionaries, with dict2 overwriting dict1
def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries, with dict2 overwriting dict1 for any matching keys.
    """
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Validation for trading series objects
def validate_trading_series(trading_series, changes: dict, logs: bool, buy: bool, param_name, parent_name, global_ticker) -> (bool, str, dict):
    '''
    Validate a trading series expression AST.

    This function checks if the trading series name exists, validates parameters,
    and builds a new, corrected AST if needed.
    '''
    not_valid = False
    message = f'Invalid trading series in parameter {param_name} of {parent_name}. Using defined default value.'

    keywords_res = []
    ticker = ''
    trading_series_id = ''

    try:
        trading_series_id = trading_series.func.id

        # Validate trading series class name
        if trading_series_id not in implemented_trading_series['Class_name'].values:
            message = f"Trading series '{trading_series_id}' does not exist."
            raise Exception(message)

        # Fetch expected parameter types
        expected_trading_series_params = implemented_trading_series.loc[implemented_trading_series['Class_name'] == trading_series_id, 'Parameters'].values[0].split(' ')
        param, param_type = zip(*[item.split(':') for item in expected_trading_series_params])

        args = trading_series.args
        keywords = trading_series.keywords

        # Validate first positional argument
        if len(args) > 0:
            first_arg = args[0]
            is_const = True if trading_series_id == 'CONST' else False

            if is_const:
                validate_result, ticker, new_changes = validate_int(first_arg, changes, logs, buy, param_name, parent_name)
            else:
                validate_result, ticker, new_changes = validate_ticker(first_arg, changes, logs)

            if not validate_result:
                message = f"Invalid {'integer' if is_const else 'ticker'} argument in trading series '{trading_series_id}' of {parent_name}."
                raise Exception(message)

        else:
            # Use global ticker fallback if necessary
            if trading_series_id != 'CONST' and global_ticker != '':
                ticker = global_ticker
                changes[f'ticker_{parent_name}_{param_name}'] = f"Using global ticker '{global_ticker.value}' in trading series '{trading_series_id}' of {parent_name}."
            else:
                message = f"Missing first argument in trading series '{trading_series_id}' of {parent_name}."
                raise Exception(message)

        used_args = []

        # Validate keyword parameters
        for keyword in keywords:
            arg_name = keyword.arg
            arg_value = keyword.value

            if arg_name in param and arg_name not in used_args:
                used_args.append(arg_name)
                arg_type = get_expected_type(arg_name, param, param_type)

                if arg_type == 'SourceType':
                    validation_result, _, new_changes = validate_source(arg_value, changes, logs, buy, arg_name, trading_series_id)
                elif arg_type == 'SmoothingType':
                    validation_result, _, new_changes = validate_smoothing_type(arg_value, changes, logs, buy, arg_name, trading_series_id)
                elif arg_type == 'int':
                    validation_result, _, new_changes = validate_int(arg_value, changes, logs, buy, arg_name, trading_series_id)
                elif arg_type == 'float':
                    validation_result, _, new_changes = validate_float(arg_value, changes, logs, buy, arg_name, trading_series_id)
                elif arg_type == 'bool':
                    validation_result, _, new_changes = validate_bool(arg_value, changes, logs, buy, arg_name, trading_series_id)
                else:
                    message = f"Invalid trading series parameter '{arg_name}'."
                    raise Exception(message)

                changes = merge_dicts(changes, new_changes)

                if validation_result:
                    keywords_res.append(ast.keyword(arg_name, arg_value))

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes_name = f'{"buy_condition" if buy else "sell_condition"}_{parent_name}_{param_name}'
        changes[changes_name] = message
        return False, None, changes

    # Reconstruct validated trading series
    new_trading_series = ast.Call(
        func=ast.Name(id=trading_series_id, ctx=ast.Load()),
        args=[ticker],
        keywords=keywords_res
    )

    return True, new_trading_series, changes

# Validation for source types
def validate_source(source, changes: dict, logs: bool, buy: bool, param_name, parent_name) -> (bool, str, dict):
    """
    Validate if the source type is valid (SourceType enum).
    """
    not_valid = False
    message = f'Invalid source type in parameter {param_name} of {parent_name}. Using defined default value.'

    try:
        value = source.value
        if value.id != 'SourceType':
            raise Exception(message)

        attr = source.attr
        valid_source_types = ['CLOSE', 'OPEN', 'HIGH', 'LOW', 'HLC3', 'HL2', 'OHLC4', 'HLCC4', 'VOLUME']

        if attr not in valid_source_types:
            message += f' Valid source types are: {", ".join(valid_source_types)}.'
            raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes_name = f'{"buy_condition" if buy else "sell_condition"}_{parent_name}_{param_name}'
        changes[changes_name] = message
        return False, None, changes

    return True, None, changes

# Validation for smoothing types
def validate_smoothing_type(smoothing_type, changes: dict, logs: bool, buy: bool, param_name, parent_name) -> (bool, str, dict):
    """
    Validate if the smoothing type is valid (SmoothingType enum).
    """
    not_valid = False
    message = f'Invalid smoothing type in parameter {param_name} of {parent_name}. Using defined default value.'

    try:
        value = smoothing_type.value
        if value.id != 'SmoothingType':
            raise Exception(message)

        attr = smoothing_type.attr
        valid_smoothing_types = ['RMA', 'SMA', 'EMA', 'WMA']

        if attr not in valid_smoothing_types:
            message += f' Valid smoothing types are: {", ".join(valid_smoothing_types)}.'
            raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes_name = f'{"buy_condition" if buy else "sell_condition"}_{parent_name}_{param_name}'
        changes[changes_name] = message
        return False, None, changes

    return True, None, changes

# Validation for boolean type
def validate_bool(bool_value, changes: dict, logs: bool, buy: bool, param_name, parent_name) -> (bool, str, dict):
    """
    Validate if the boolean parameter is of correct type.
    """
    not_valid = False
    message = f'Invalid boolean value in parameter {param_name} of {parent_name}. Using defined default value.'

    try:
        bool_value = bool_value.value
        if not isinstance(bool_value, bool):
            raise Exception(message)
    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes_name = f'{"buy_condition" if buy else "sell_condition"}_{parent_name}_{param_name}'
        changes[changes_name] = message
        return False, None, changes

    return True, None, changes

# Validation for Fibonacci levels
def validate_fibonacci_levels(fibonacci_levels, changes: dict, logs: bool, buy: bool, param_name: str, parent_name: str) -> (bool, str, dict):
    """
    Validate if the Fibonacci level is valid (FibonacciLevels enum).
    """
    not_valid = False
    message = f'Invalid Fibonacci levels in parameter {param_name} of {parent_name}. Using defined default level 38.2%.'

    try:
        value = fibonacci_levels.value
        if value.id != 'FibonacciLevels':
            raise Exception(message)

        attr = fibonacci_levels.attr
        valid_fibonacci_levels = ['LEVEL_0', 'LEVEL_23_6', 'LEVEL_38_2', 'LEVEL_50', 'LEVEL_61_8', 'LEVEL_100']

        if attr not in valid_fibonacci_levels:
            message += f' Valid Fibonacci levels are: {", ".join(valid_fibonacci_levels)}.'
            raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes_name = f'{"buy_condition" if buy else "sell_condition"}_{parent_name}_{param_name}'
        changes[changes_name] = message

        # Use default value
        default_ast_attribute = ast.Attribute(
            value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
            attr='LEVEL_38_2',
            ctx=ast.Load()
        )
        return True, default_ast_attribute, changes

    return True, fibonacci_levels, changes

# Validation for integer type
def validate_int(int_value, changes: dict, logs: bool, buy: bool, param_name, parent_name) -> (bool, str, dict):
    """
    Validate if the parameter is an integer.
    """
    not_valid = False
    message = f'Invalid integer value in parameter {param_name} of {parent_name}.'
    if not parent_name.endswith('Condition'):
        message += f' Using defined default value.'

    try:
        int_value_value = int_value.value
        if not isinstance(int_value_value, int):
            raise Exception(message)
    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes_name = f'{"buy_condition" if buy else "sell_condition"}_{parent_name}_{param_name}'
        changes[changes_name] = message
        return False, None, changes

    return True, int_value, changes

# Validation for float type
def validate_float(float_value, changes: dict, logs: bool, buy: bool, param_name, parent_name) -> (bool, str, dict):
    """
    Validate if the parameter is a float.
    """
    not_valid = False
    message = f'Invalid float value in parameter {param_name} of {parent_name}. Using defined default value.'

    try:
        float_value_value = float_value.value
        if not isinstance(float_value_value, (float, int)):
            raise Exception(message)
    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes_name = f'{"buy_condition" if buy else "sell_condition"}_{parent_name}_{param_name}'
        changes[changes_name] = message
        return False, None, changes

    return True, float_value, changes

# Validation for condition AST expressions
def validate_condition(condition, changes: dict, logs: bool, buy: bool, global_ticker: str) -> (bool, str, dict):
    '''
    Validate a logical or simple condition recursively, ensuring all parameters and sub-conditions are correct.
    '''
    not_valid = False
    message = 'Invalid condition.'
    new_condition = condition

    try:
        condition_id = condition.func.id

        if condition_id not in implemented_conditions['Class_name'].values:
            message = f"Condition '{condition_id}' does not exist."
            raise Exception(message)

        expected_condition_params = implemented_conditions.loc[implemented_conditions['Class_name'] == condition_id, 'Parameters'].values[0].split(' ')
        param, param_type = zip(*[item.split(':') for item in expected_condition_params])

        args_res = []
        used_args = []

        if condition_id in ['AND', 'OR']:
            # Logical grouping
            for arg in condition.args:
                validation_result, validation_new_condition, new_changes = validate_condition(arg, changes, logs, buy, global_ticker)
                changes = merge_dicts(changes, new_changes)

                if validation_result:
                    args_res.append(validation_new_condition)

            if len(args_res) > 0:
                new_condition = ast.Call(
                    func=ast.Name(id=condition_id, ctx=ast.Load()),
                    args=args_res,
                    keywords=[]
                )
            else:
                message = f"Condition '{condition_id}' is missing the arguments."
                raise Exception(message)
        else:
            # Simple condition with keyword parameters
            for arg in condition.keywords:
                arg_name = arg.arg
                arg_value = arg.value

                if arg_name in param and arg_name not in used_args:
                    used_args.append(arg_name)
                    arg_type = get_expected_type(arg_name, param, param_type)

                    if arg_type == 'Condition':
                        validation_result, new_object, new_changes = validate_condition(arg_value, changes, logs, buy, global_ticker)
                    elif arg_type == 'TradingSeries':
                        validation_result, new_object, new_changes = validate_trading_series(arg_value, changes, logs, buy, arg_name, condition_id, global_ticker)
                    elif arg_type == 'FibonacciLevels':
                        validation_result, new_object, new_changes = validate_fibonacci_levels(arg_value, changes, logs, buy, arg_name, condition_id)
                    elif arg_type == 'int':
                        validation_result, new_object, new_changes = validate_int(arg_value, changes, logs, buy, arg_name, condition_id)
                    elif arg_type == 'float':
                        validation_result, new_object, new_changes = validate_float(arg_value, changes, logs, buy, arg_name, condition_id)
                    else:
                        message = f"Invalid condition parameter '{arg_name}'."
                        raise Exception(message)

                    changes = merge_dicts(changes, new_changes)

                    if validation_result:
                        args_res.append(ast.keyword(arg_name, new_object))

            if len(args_res) == len(param):
                new_condition = ast.Call(
                    func=ast.Name(id=condition_id, ctx=ast.Load()),
                    args=[],
                    keywords=args_res
                )
            else:
                not_used = set(param) - set(used_args)
                not_used = list(not_used)
                not_used.sort()

                if len(not_used) < 1:
                    return False, None, changes

                message = f"Condition '{condition_id}' is missing the following parameters: {', '.join(not_used)}."
                raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['buy_condition' if buy else 'sell_condition'] = message
        return False, None, changes

    return True, new_condition, changes
