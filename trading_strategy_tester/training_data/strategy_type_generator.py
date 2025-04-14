import random
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum

def get_random_strategy_type(rng: random.Random=None):
    '''
    This function returns a random strategy type from predefined list of strategy types.
    Default strategy type is 'long' when no strategy type is specified.

    :param rng: A random number generator.
    :type rng: random.Random
    :return: A tuple containing the chosen strategy type and its corresponding PositionTypeEnum.
    :rtype: tuple
    '''

    strategy_type = {
        'long': PositionTypeEnum.LONG,
        'short': PositionTypeEnum.SHORT,
        'long-short combination': PositionTypeEnum.LONG_SHORT_COMBINED,
        '': PositionTypeEnum.LONG  # Default when no strategy type is specified
    }

    chosen_strategy_type_text = rng.choice(list(strategy_type.keys()))
    chosen_strategy_type_param = strategy_type[chosen_strategy_type_text]

    return chosen_strategy_type_text, chosen_strategy_type_param