import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def mass_index(high: pd.Series, low: pd.Series, length: int = 10) -> pd.Series:
    """
    Calculate the Mass Index, a technical indicator used to detect trend reversals based on
    price volatility without indicating the direction of the trend.

    The Mass Index focuses on the range between the high and low prices and applies an EMA-based
    calculation to identify "reversal bulges," suggesting potential trend changes.

    :param high: A pandas Series representing the high prices of the asset.
    :type high: pd.Series
    :param low: A pandas Series representing the low prices of the asset.
    :type low: pd.Series
    :param length: The period over which the Mass Index is calculated. Default is 10, commonly used for detecting reversal bulges.
    :type length: int, optional
    :return: A pandas Series containing the Mass Index values, labeled with the appropriate name.
    :rtype: pd.Series
    """

    # Validate the specified length or assign a default
    length = get_length(length=length, default=10)
    span_length = 9  # Typically, a 9-period EMA is used for smoothing

    # Calculate the price span (difference between high and low)
    span = high - low

    # Apply an EMA smoothing to the span
    span_smooth = smooth(series=span, length=span_length, smoothing_type=SmoothingType.EMA)

    # Calculate the Mass Index by dividing the smoothed span by its EMA and summing over the specified length
    mass_index_series = (
        span_smooth / smooth(series=span_smooth, length=span_length, smoothing_type=SmoothingType.EMA)
    ).rolling(window=length, min_periods=span_length).sum()

    # Return the Mass Index series with an appropriate name for easy identification
    return pd.Series(mass_index_series, name=f'MASS-INDEX_{length}')
