def validate_trade_commissions(trade_commissions, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validate the trade_commissions parameter.

    :param trade_commissions: The trade_commissions parameter to validate.
    :type trade_commissions: ast.Call
    :param changes: A dictionary to store changes made during validation.
    :type changes: dict
    :param logs: A boolean indicating whether to log messages.
    :type logs: bool
    :return: A tuple containing a boolean indicating validity, a message, and the updated changes dictionary.
    :rtype: (bool, str, dict)
    """

    message = f"trade_commissions argument should be of type TradeCommissions. Available commissions are: MoneyCommissions, PercentageCommissions. Defaulting to no commissions."
    not_valid = False

    try:
        trade_commission_type = trade_commissions.func.id

        if trade_commission_type not in ['MoneyCommissions', 'PercentageCommissions']:
            message = f"Invalid trade_commissions type. Available commissions are: MoneyCommissions, PercentageCommissions. Defaulting to no commissions."
            raise Exception('Invalid trade_commissions type')

        # If there is not 'value=' in the function call
        if len(trade_commissions.args) == 1 and len(trade_commissions.keywords) == 0:
            trade_commissions_value = trade_commissions.args[0].value
        elif len(trade_commissions.args) == 0 and len(trade_commissions.keywords) == 1:
            if 'value' != trade_commissions.keywords[0].arg:
                message = f"Missing 'value' keyword in trade_commissions function call. Defaulting to no commissions."
                raise Exception(message)
            else:
                trade_commissions_value = trade_commissions.keywords[0].value.value
        else:
            message = f"Invalid number of arguments in trade_commissions function call. Defaulting to no commissions."
            raise Exception(message)

        if not isinstance(trade_commissions_value, (int, float)):
            message = f"trade_commissions argument percentage should be a number. Defaulting to no commissions."
            raise Exception('Trade commissions value not a number')

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['trade_commissions'] = message

        return False, None, changes

    return True, None, changes