import random
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.training_data.prompt_data.string_options import intervals
from trading_strategy_tester.training_data.prompt_data.condition_dicts import interval_to_text

def get_random_interval():
    '''
    This function returns a random interval for a strategy.
    :return: A tuple containing the interval.
    :rtype: tuple
    '''

    random_interval = random.choice([
        Interval.ONE_MINUTE,
        Interval.TWO_MINUTES,
        Interval.FIVE_MINUTES,
        Interval.FIFTEEN_MINUTES,
        Interval.THIRTY_MINUTES,
        Interval.SIXTY_MINUTES,
        Interval.NINETY_MINUTES,
        Interval.ONE_HOUR,
        Interval.ONE_DAY,
        Interval.FIVE_DAYS,
        Interval.ONE_WEEK,
        Interval.ONE_MONTH,
        Interval.THREE_MONTHS
    ])

    interval_text = random.choice(intervals).format(interval=interval_to_text[random_interval])
    interval_param = str(random_interval)

    return interval_text, interval_param