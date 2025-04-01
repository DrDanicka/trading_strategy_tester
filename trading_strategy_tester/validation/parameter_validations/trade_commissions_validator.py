def validate_trade_commissions(trade_commissions, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validate the trade_commissions parameter.

    :param trade_commissions: The trade_commissions parameter to validate.
    :param changes: A dictionary to store changes made during validation.
    :param logs: A boolean indicating whether to log messages.
    :return: A tuple containing a boolean indicating validity, a message, and the updated changes dictionary.
    """
    message = f"trade_commissions argument should be of type TradeCommissions. Available commissions are: MoneyCommissions, PercentageCommissions. Defaulting to no commissions."
    not_valid = False

    try:
        trade_commission_type = trade_commissions.func.id

        if trade_commission_type not in ['MoneyCommissions', 'PercentageCommissions']:
            message = f"Invalid trade_commissions type. Available commissions are: MoneyCommissions, PercentageCommissions. Defaulting to no commissions."
            raise Exception('Invalid trade_commissions type')

        trade_commissions_value = trade_commissions.args[0].value

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