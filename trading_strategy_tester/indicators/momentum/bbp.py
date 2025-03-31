import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def bbp(high: pd.Series, low: pd.Series, close: pd.Series, length: int = 13) -> pd.Series:
    """
    Calculate the Bull and Bear Power (BBP) indicator.

    The BBP indicator combines the bull and bear power to provide insights into the strength and direction
    of market trends. Bull Power is calculated as the difference between the high price and the smoothed
    close price, while Bear Power is calculated as the difference between the low price and the smoothed
    close price.

    :param high: Series of high prices.
    :type high: pd.Series
    :param low: Series of low prices.
    :type low: pd.Series
    :param close: Series of close prices.
    :type close: pd.Series
    :param length: The smoothing period for calculating the exponential moving average (EMA), default is 13.
    :type length: int, optional
    :return: Bull and Bear Power (BBP) indicator as a Pandas Series.
    :rtype: pd.Series
    """
    # Validate the smoothing period length; set to default if invalid
    length = get_length(length, 13)

    # Calculate Bull Power as the difference between high price and smoothed close price
    bull_power = high - smooth(close, length, SmoothingType.EMA)

    # Calculate Bear Power as the difference between low price and smoothed close price
    bear_power = low - smooth(close, length, SmoothingType.EMA)

    # Combine Bull Power and Bear Power to form the BBP series
    bbp_series = bull_power + bear_power

    # Return the BBP series as a Pandas Series with an appropriate name
    return pd.Series(bbp_series, name=f'BBP_{length}')
