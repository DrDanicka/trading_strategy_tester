from trading_strategy_tester.trade.order_size.contracts import Contracts


def validate_order_size(order_size, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validates the order size parameter.

    :param order_size: The order size to validate.
    :param changes: A dictionary to store changes made during validation.
    :param logs: A boolean indicating whether to log messages.
    :return: A tuple containing a boolean indicating validity, an error message (if any), and the updated changes dictionary.
    """
    default_order_size = Contracts(1)
    not_valid = False
    message = f"order_size argument should of type OrderSize. Available order sizes are: 'Contracts', 'USD', 'PercentOfEquity'. Using default order size '{default_order_size}'."

    try:
        order_size_id = order_size.func.id
        order_size_value = order_size.args[0].value

        if order_size_id not in ['Contracts', 'USD', 'PercentOfEquity']:
            not_valid = True

        if not isinstance(order_size_value, (int, float)):
            message = f"order_size argument should be a number. Defaulting to {default_order_size}."
            not_valid = True
    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['order_size'] = message

        return False, default_order_size, changes

    return True, None, changes