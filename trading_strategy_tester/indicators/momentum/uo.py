import pandas as pd
import numpy as np


def uo(close: pd.Series, low: pd.Series, high: pd.Series, fast_length: int = 7, middle_length: int = 14,
       slow_length: int = 28) -> pd.Series:
    """
    Calculate the Ultimate Oscillator (UO) for a given financial instrument.

    The Ultimate Oscillator is a momentum oscillator that uses weighted averages of three different periods
    (fast, middle, and slow) to identify potential overbought or oversold conditions and track price trends.
    It considers the relationship between the current closing price and the true range over varying time frames.

    :param close: Series of closing prices.
    :type close: pd.Series
    :param low: Series of the lowest prices.
    :type low: pd.Series
    :param high: Series of the highest prices.
    :type high: pd.Series
    :param fast_length: The number of periods for the fast component of the UO calculation. Default is 7.
    :type fast_length: int, optional
    :param middle_length: The number of periods for the middle component of the UO calculation. Default is 14.
    :type middle_length: int, optional
    :param slow_length: The number of periods for the slow component of the UO calculation. Default is 28.
    :type slow_length: int, optional
    :return: A pandas Series containing the Ultimate Oscillator values, labeled with the appropriate name.
    :rtype: pd.Series
    """

    # Calculate the highest and lowest adjusted for the previous close
    high_ = np.maximum(close.shift(1), high)  # True high over the specified period
    low_ = np.minimum(close.shift(1), low)  # True low over the specified period

    # Calculate Buying Pressure (BP) and True Range (TR)
    bp = close - low_  # Buying Pressure is the difference between the close and the true low
    tr = high_ - low_  # True Range is the difference between the true high and true low

    # Calculate average BP/TR ratios over fast, middle, and slow lengths
    avg_fast = bp.rolling(fast_length).sum() / tr.rolling(fast_length).sum()  # Fast average BP/TR
    avg_middle = bp.rolling(middle_length).sum() / tr.rolling(middle_length).sum()  # Middle average BP/TR
    avg_slow = bp.rolling(slow_length).sum() / tr.rolling(slow_length).sum()  # Slow average BP/TR

    # Calculate the Ultimate Oscillator as a weighted average of the three averages
    uo_series = 100 * (4 * avg_fast + 2 * avg_middle + avg_slow) / 7

    return pd.Series(uo_series, name=f'UO_{fast_length}_{middle_length}_{slow_length}')
