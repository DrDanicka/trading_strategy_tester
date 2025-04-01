from trading_strategy_tester.enums.interval_enum import Interval

def validate_interval(interval, changes: dict, logs: bool) -> (bool, str, dict):
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