def validate_take_profit(take_profit, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validates the take profit parameter to ensure it is of the correct type and value.
    If the validation fails, it defaults to no take profit and logs an error message.

    :param take_profit: The take profit object to validate. This is expected to be an AST `Call` node representing a `TakeProfit`.
    :type take_profit: ast.Call
    :param changes: A dictionary to store any changes or messages made during validation.
    :type changes: dict
    :param logs: A boolean indicating whether to log messages when validation fails.
    :type logs: bool
    :return: A tuple containing a boolean indicating validity, a message, and the updated `changes` dictionary.
    :rtype: (bool, str, dict)

    The function ensures:
    1. The `take_profit` argument is of type `TakeProfit`.
    2. The `take_profit` object has a valid `percentage` attribute.
    3. The `percentage` value should be a numeric type (int or float).
    4. If validation fails, it defaults to no take profit (`None`) and logs an error message.
    """

    default_take_profit = None
    message = f"take_profit argument should be of type TakeProfit. Defaulting to no take profit."
    not_valid = False

    try:
        take_profit_type = take_profit.func.id

        if take_profit_type == 'TakeProfit':
            take_profit_percentage = take_profit.keywords[0]

            if take_profit_percentage.arg != 'percentage':
                message = f"take_profit argument percentage is missing. Defaulting to no take profit."
                raise Exception("percentage not found")

            if not isinstance(take_profit_percentage.value.value, (int, float)):
                message = f"take_profit argument percentage should be a number. Defaulting to no take profit."
                raise Exception("percentage not found")

        else:
            not_valid = True
    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['take_profit'] = message

        return False, default_take_profit, changes

    return True, None, changes