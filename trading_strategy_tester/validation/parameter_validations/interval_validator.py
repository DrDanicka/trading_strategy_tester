from trading_strategy_tester.enums.interval_enum import Interval

def validate_interval(interval, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validates the interval parameter to ensure it is of a valid type and value. If the validation fails,
    it defaults to a pre-defined valid interval (Interval.ONE_DAY) and logs the error message.

    :param interval: The interval to be validated. This is expected to be an AST Attribute node representing an enum.
    :type interval: ast.Attribute
    :param changes: A dictionary to store any changes or messages made during validation.
    :type changes: dict
    :param logs: A boolean indicating whether to log messages when validation fails.
    :type logs: bool
    :return: A tuple containing a boolean indicating validity, a message, and the updated `changes` dictionary.
    :rtype: (bool, str, dict)

    The function ensures:
    1. The `interval` parameter is of type `Interval`.
    2. The `interval.attr` corresponds to a valid interval value (`'ONE_DAY'`, `'FIVE_DAYS'`, `'ONE_WEEK'`, `'ONE_MONTH'`, or `'THREE_MONTHS'`).
    3. If validation fails, it uses the default interval (`Interval.ONE_DAY`) and logs the error message if `logs` is `True`.
    """
    default_interval = Interval.ONE_DAY
    message = f"interval argument should be of type Interval. Defaulting to {default_interval}."
    not_valid = False

    try:
        interval_enum = interval.value.id
        interval_attr = interval.attr

        if interval_enum != 'Interval':
            raise Exception("Invalid interval enum")

        valid_intervals = ['ONE_DAY', 'FIVE_DAYS', 'ONE_WEEK', 'ONE_MONTH', 'THREE_MONTHS']

        if interval_attr not in valid_intervals:
            message = f"Valid intervals are: {', '.join(valid_intervals)}. Defaulting to {default_interval}."
            raise Exception("Invalid interval attr")

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['interval'] = message

        return False, default_interval, changes

    return True, None, changes