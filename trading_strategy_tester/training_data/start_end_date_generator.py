import random
from trading_strategy_tester.training_data.prompt_data.string_options import dates, periods
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.training_data.prompt_data.condition_dicts import period_to_text

def get_random_start_end_dates(rng: random.Random=None, start: bool = True):
    '''
    This function returns a random start and end date for a strategy.

    :param rng: A random number generator.
    :type rng: random.Random
    :param start: A boolean indicating whether to generate a start date (True) or an end date (False).
    :type start: bool
    :return: A tuple containing the start and end date.
    :rtype: tuple
    '''

    start_year = rng.randint(2000, 2019)
    start_month = rng.randint(1, 12)
    start_day = rng.randint(1, 28)

    end_year = rng.randint(2020, 2024)
    end_month = rng.randint(1, 12)
    end_day = rng.randint(1, 28)

    if start:
        date_text = rng.choice(dates).format(type='start', year=start_year, month=start_month, day=start_day)
        date_param = f'datetime({start_year}, {start_month}, {start_day})'
    else:
        date_text = rng.choice(dates).format(type='end', year=end_year, month=end_month, day=end_day)
        date_param = f'datetime({end_year}, {end_month}, {end_day})'

    return date_text, date_param


def get_random_period(rng: random.Random=None):
    '''
    This function returns a random period for a strategy.

    :param rng: A random number generator.
    :type rng: random.Random
    :return: A tuple containing the period.
    :rtype: tuple
    '''

    random_period = rng.choice([
        Period.ONE_DAY,
        Period.FIVE_DAYS,
        Period.ONE_MONTH,
        Period.THREE_MONTHS,
        Period.SIX_MONTHS,
        Period.ONE_YEAR,
        Period.TWO_YEARS,
        Period.FIVE_YEARS,
        Period.TEN_YEARS,
        Period.YEAR_TO_DATE,
        Period.MAX
    ])

    period_text = rng.choice(periods).format(period=period_to_text[random_period])
    period_param = str(random_period)

    return period_text, period_param

