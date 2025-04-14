from trading_strategy_tester.training_data.prompt_data.string_options import *
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.enums.interval_enum import Interval

conditions_with_2_trading_series = {
    1: (crossover_conditions, 'CrossOverCondition'),
    2: (crossunder_conditions, 'CrossUnderCondition'),
    3: (greater_than_conditions, 'GreaterThanCondition'),
    4: (less_than_conditions, 'LessThanCondition'),
}

conditions_with_trading_series_and_number = {
    1: (uptrend_for_x_days_conditions, 'UptrendForXDaysCondition'),
    2: (downtrend_for_x_days_conditions, 'DowntrendForXDaysCondition'),
}

conditions_with_trading_series_and_2_numbers = {
    1: (change_of_x_percent_per_y_days_conditions, 'ChangeOfXPercentPerYDaysCondition')
}

conditions_with_trading_series_and_percentage = {
    1: (intra_interval_change_of_x_percent_conditions, 'IntraIntervalChangeOfXPercentCondition')
}

conditions_with_fib_levels = {
    1: (downtrend_fibonacci_retracement_conditions, 'DowntrendFibRetracementLevelCondition'),
    2: (uptrend_fibonacci_retracement_conditions, 'UptrendFibRetracementLevelCondition')
}

conditions_dict = {
    1: conditions_with_2_trading_series,
    2: conditions_with_trading_series_and_number,
    3: conditions_with_trading_series_and_2_numbers,
    4: conditions_with_trading_series_and_percentage,
    5: conditions_with_fib_levels
}

period_to_text = {
    Period.ONE_DAY: '1 day',
    Period.FIVE_DAYS: '5 days',
    Period.ONE_MONTH: '1 month',
    Period.THREE_MONTHS: '3 months',
    Period.SIX_MONTHS: '6 months',
    Period.ONE_YEAR: '1 year',
    Period.TWO_YEARS: '2 years',
    Period.FIVE_YEARS: '5 years',
    Period.TEN_YEARS: '10 years',
    Period.YEAR_TO_DATE: 'year to date',
    Period.MAX: 'maximum'
}

interval_to_text = {
    Interval.ONE_DAY: '1 day',
    Interval.FIVE_DAYS: '5 days',
    Interval.ONE_WEEK: '1 week',
    Interval.ONE_MONTH: '1 month',
    Interval.THREE_MONTHS: '3 months'
}