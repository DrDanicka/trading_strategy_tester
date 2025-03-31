import pandas as pd
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def percent_k(close: pd.Series, low: pd.Series, high: pd.Series, length: int = 14) -> pd.Series:
    """
    Calculate the Stochastic %K indicator for a given financial instrument.

    The Stochastic %K compares the latest closing price to the range of prices over the specified period
    (default is 14). It is used in technical analysis to identify overbought and oversold conditions.

    :param close: Series of closing prices.
    :type close: pd.Series
    :param low: Series of the lowest prices.
    :type low: pd.Series
    :param high: Series of the highest prices.
    :type high: pd.Series
    :param length: The number of periods over which to calculate the %K component. Default is 14.
    :type length: int, optional
    :return: A pandas Series containing the Stochastic %K values labeled with the appropriate name.
    :rtype: pd.Series
    """

    # Validate the length argument
    length = get_length(length=length, default=14)

    # Calculate the lowest low and highest high over the specified period
    lowest_low = low.rolling(window=length).min()
    highest_high = high.rolling(window=length).max()

    # Calculate %K
    cl = close - lowest_low
    hl = highest_high - lowest_low
    percent_k = (cl / hl) * 100

    return pd.Series(percent_k, name=f'STOCH-PERCENT-K_{length}')


def percent_d(close: pd.Series, low: pd.Series, high: pd.Series, length: int = 14,
              d_smooth_length: int = 3) -> pd.Series:
    """
    Calculate the Stochastic %D indicator for a given financial instrument.

    The Stochastic %D is a smoothed version of %K, typically calculated as a simple moving average (SMA)
    of %K over a specified smoothing period. It is used alongside %K in technical analysis for identifying
    trends and potential reversal points.

    :param close: Series of closing prices.
    :type close: pd.Series
    :param low: Series of the lowest prices.
    :type low: pd.Series
    :param high: Series of the highest prices.
    :type high: pd.Series
    :param length: The number of periods over which to calculate the %K component. Default is 14.
    :type length: int, optional
    :param d_smooth_length: The smoothing period for calculating %D from %K. Default is 3.
    :type d_smooth_length: int, optional
    :return: A pandas Series containing the Stochastic %D values labeled with the appropriate name.
    :rtype: pd.Series
    """

    # Calculate the Stochastic %K series
    percent_k_series = percent_k(close, low, high, length=length)

    # Calculate %D as the smoothed %K (SMA by default)
    percent_d = smooth(percent_k_series, d_smooth_length, SmoothingType.SMA)

    return pd.Series(percent_d, name=f'STOCH-PERCENT-D_{length}_{d_smooth_length}')
