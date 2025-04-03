from trading_strategy_tester.enums.period_enum import Period


def validate_period(period, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validates the period parameter to ensure it is of a valid type and value. If the validation fails,
    it defaults to a pre-defined valid period (`Period.NOT_PASSED`) and logs an error message.

    :param period: The period to validate. This is expected to be an AST `Attribute` node representing an enum.
    :type period: ast.Attribute
    :param changes: A dictionary to store any changes or messages made during validation.
    :type changes: dict
    :param logs: A boolean indicating whether to log messages when validation fails.
    :type logs: bool
    :return: A tuple containing a boolean indicating validity, a message, and the updated `changes` dictionary.
    :rtype: (bool, str, dict)

    The function ensures:
    1. The `period` argument is a valid `Period` enum type.
    2. The `period` argument is a valid value (e.g., `'ONE_DAY'`, `'FIVE_DAYS'`, `'ONE_MONTH'`).
    3. If validation fails, it uses the default period (`Period.NOT_PASSED`) and logs the error message.
    """

    default_period = Period.NOT_PASSED
    message = f"period argument should be of type Period. Defaulting to no period."
    not_valid = False

    try:
        period_enum = period.value.id
        period_attr = period.attr

        if period_enum != 'Period':
            raise Exception("Invalid period enum")

        valid_periods = ['ONE_DAY', 'FIVE_DAYS', 'ONE_MONTH', 'THREE_MONTHS', 'SIX_MONTHS', 'ONE_YEAR',
                           'TWO_YEARS', 'FIVE_YEARS', 'TEN_YEARS', 'YEAR_TO_DATE', 'MAX', 'NOT_PASSED']

        if period_attr not in valid_periods:
            message = f"Valid periods are: {', '.join(valid_periods)}. Defaulting to no period."
            raise Exception("Invalid period attr")

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['period'] = message

        return False, default_period, changes

    return True, None, changes