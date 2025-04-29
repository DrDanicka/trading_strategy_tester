from trading_strategy_tester.trade.order_size.contracts import Contracts


def validate_order_size(order_size, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validates the order size parameter.

    :param order_size: The order size to validate.
    :type order_size: ast.Call
    :param changes: A dictionary to store changes made during validation.
    :type changes: dict
    :param logs: A boolean indicating whether to log messages.
    :type logs: bool
    :return: A tuple containing a boolean indicating validity, a message, and the updated `changes` dictionary.
    :rtype: (bool, str, dict)

    The function ensures:
    1. The `order_size` argument is a valid type (`'Contracts'`, `'USD'`, or `'PercentOfEquity'`).
    2. The `order_size` argument is a valid number (int or float).
    3. If validation fails, it uses a default order size and logs an error message.
    """
    default_order_size = Contracts(1)
    not_valid = False
    message = f"order_size argument should of type OrderSize. Available order sizes are: 'Contracts', 'USD', 'PercentOfEquity'. Using default order size 'Contracts(1)'."

    try:
        order_size_id = order_size.func.id

        if order_size_id not in ['Contracts', 'USD', 'PercentOfEquity']:
            raise Exception("Invalid order size type")

        if len(order_size.args) == 1 and len(order_size.keywords) == 0:
            order_size_value = order_size.args[0].value
        elif len(order_size.args) == 0 and len(order_size.keywords) == 1:
            if 'value' != order_size.keywords[0].arg:
                message = f"Missing 'value' keyword in order_size function call. Defaulting to 'Contracts(1)'."
                raise Exception(message)
            else:
                order_size_value = order_size.keywords[0].value.value
        else:
            message = f"Invalid number of arguments in order_size function call. Defaulting to 'Contracts(1)'."
            raise Exception(message)

        if not isinstance(order_size_value, (int, float)):
            message = f"order_size argument should be a number. Defaulting to 'Contracts(1)'."
            raise Exception("Order size value not a number")
    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['order_size'] = message

        return False, default_order_size, changes

    return True, None, changes