from trading_strategy_tester.enums.period_enum import Period



def validate_period(period, changes: dict, logs: bool) -> (bool, str, dict):
    default_period = Period.NOT_PASSED
    message = f"period argument should be of type Period. Defaulting to {default_period}."
    not_valid = False

    try:
        period_enum = period.value.id
        period_attr = period.attr

        if period_enum != 'Period':
            raise Exception("Invalid period enum")

        valid_periods = ['ONE_DAY', 'FIVE_DAYS', 'ONE_MONTH', 'THREE_MONTHS', 'SIX_MONTHS', 'ONE_YEAR',
                           'TWO_YEARS', 'FIVE_YEARS', 'TEN_YEARS', 'YEAR_TO_DATE', 'MAX', 'NOT_PASSED']

        if period_attr not in valid_periods:
            message = f"Valid periods are: {', '.join(valid_periods)}. Defaulting to {default_period}."
            raise Exception("Invalid period attr")

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['period'] = message

        return False, default_period, changes

    return True, None, changes