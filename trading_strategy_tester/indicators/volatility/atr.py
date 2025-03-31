import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def atr(high: pd.Series, low: pd.Series, close: pd.Series, length: int = 14,
        smoothing: SmoothingType = SmoothingType.RMA) -> pd.Series:
    """
    Calculate the Average True Range (ATR) of a given series using a specified smoothing method.

    The ATR is a measure of volatility that considers the greatest of the following for each period:
    - The difference between the current high and low.
    - The difference between the previous close and the current high.
    - The difference between the previous close and the current low.

    :param high: A pandas Series representing the high prices.
    :type high: pd.Series
    :param low: A pandas Series representing the low prices.
    :type low: pd.Series
    :param close: A pandas Series representing the closing prices.
    :type close: pd.Series
    :param length: The window length to calculate the ATR. Default is 14 periods.
    :type length: int, optional
    :param smoothing: The smoothing method to use. Can be 'RMA', 'SMA', 'EMA', or 'WMA'. Default is SmoothingType.RMA.
    :type smoothing: SmoothingType, optional
    :return: A pandas Series containing the ATR values for the given series.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=14)

    # Calculate True Range (TR)
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Calculate ATR using the specified smoothing method
    atr_series = smooth(true_range, length, smoothing)

    return pd.Series(atr_series, name=f'ATR_{length}_{smoothing.value}')
