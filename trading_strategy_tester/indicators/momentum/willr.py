import pandas as pd
from trading_strategy_tester.utils.parameter_validations import get_length

def willr(source: pd.Series, high: pd.Series, low: pd.Series, length: int = 14) -> pd.Series:
    """
    Calculate the Williams %R (WILLR) momentum indicator.

    Williams %R is a momentum indicator that measures the level of the close relative to the high-low range over a specified period.
    It is typically used to identify overbought and oversold conditions in a market.

    :param source: The price series (e.g., closing prices) to calculate Williams %R.
    :type source: pd.Series
    :param high: The high price series for the specified period.
    :type high: pd.Series
    :param low: The low price series for the specified period.
    :type low: pd.Series
    :param length: The number of periods over which to calculate Williams %R. Default is 14.
    :type length: int, optional
    :return: A pandas Series containing the calculated Williams %R values, labeled with the appropriate length.
    :rtype: pd.Series
    """
    # Validate the length parameter to ensure it is within a reasonable range or fallback to default
    length = get_length(length=length, default=14)

    # Calculate rolling maximum and minimum for the high and low price series
    rolling_max = high.rolling(window=length).max()
    rolling_min = low.rolling(window=length).min()

    # Compute the Williams %R formula: 100 * (close - highest_high) / (highest_high - lowest_low)
    willr_series = 100 * (source - rolling_max) / (rolling_max - rolling_min)

    # Return the calculated series with an appropriate name
    return pd.Series(willr_series, name=f'WILLR_{length}')
