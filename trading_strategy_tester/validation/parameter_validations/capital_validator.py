def validate_initial_capital(initial_capital, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validates the initial capital parameter.

    :param initial_capital: The initial capital amount.
    :type initial_capital: ast.Constant
    :param changes: A dictionary to store any changes made during validation.
    :type changes: dict
    :param logs: A boolean indicating whether to log messages.
    :type logs: bool
    :return: A tuple containing a boolean indicating validity, a message, and the updated `changes` dictionary.
    :rtype: (bool, str, dict)

    This function ensures:
    1. The `initial_capital` parameter is a valid number (int or float).
    2. If validation fails, it uses a default initial capital and logs an error message.
    """
    default_initial_capital = 1_000_000
    not_valid = False
    message = f"initial_capital argument should be a number. Using default initial capital '{default_initial_capital}'."

    try:
        initial_capital_value = initial_capital.value

        if not isinstance(initial_capital_value, (int, float)):
            not_valid = True
    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['initial_capital'] = message

        return False, default_initial_capital, changes

    return True, None, changes