def validate_take_profit(take_profit, changes: dict, logs: bool) -> (bool, str, dict):
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