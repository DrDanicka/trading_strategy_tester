import ast

from trading_strategy_tester.validation.implemented_objects import implemented_conditions, implemented_trading_series

def validate_trading_series(trading_series, changes: dict, logs: bool, buy: bool) -> (bool, str, dict):
    pass

def validate_condition(condition, changes: dict, logs: bool, buy: bool) -> (bool, str, dict):
    not_valid = False
    message = 'Invalid condition.'

    try:
        # Get condition id
        condition_id = condition.func.id

        if condition_id not in implemented_conditions['Class_name'].values:
            message = f"Condition '{condition_id}' is not implemented."
            raise Exception(message)

        condition_params = condition.args
        expected_condition_params = implemented_conditions.loc[implemented_conditions['Class_name'] == condition_id, 'Parameters'].values[0].split(' ')

        param, param_type = zip(*[item.split(':') for item in expected_condition_params])

        for i, (p, pt) in enumerate(zip(param, param_type)):
            if p.startswith('*'):
                for p_condition in condition_params:
                    # TODO validate recursive conditions
                    validate_condition(p_condition, changes, logs, buy)
            else:
                if pt == 'Condition':
                    # TODO validate condition
                    validate_condition(condition_params[i], changes, logs, buy)
                elif pt == 'TradingSeries':
                    # TODO validate trading series
                    validate_trading_series(condition_params[i], changes, logs, buy)
                elif pt == 'FibonacciLevels':
                    # TODO validate fibonacci levels
                    pass
                elif pt == 'int':
                    message = f"Parameter '{p}' should be an integer."
                    # Check if not int
                    if not isinstance(condition_params[i].value, int):
                        raise Exception(message)
                    message = 'Invalid condition'
                elif pt == 'float':
                    message = f"Parameter '{p}' should be a float."
                    # Check if not float
                    if not isinstance(condition_params[i].value, float):
                        raise Exception(message)
                    message = 'Invalid condition'
                else:
                    message = f'Invalid parameter type {pt} for parameter {p}.'
                    raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['buy_condition' if buy else 'sell_condition'] = message

        return False, message, changes

    return True, None, changes