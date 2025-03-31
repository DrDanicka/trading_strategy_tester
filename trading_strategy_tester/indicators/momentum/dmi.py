import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length
from trading_strategy_tester.indicators.volatility.atr import atr


def di_plus(high: pd.Series, low: pd.Series, close: pd.Series, di_length: int = 14) -> pd.Series:
    """
    Calculate the Positive Directional Indicator (+DI) for a given price series.

    The Positive Directional Indicator (+DI) is part of the Directional Movement System
    developed by J. Welles Wilder. It measures the presence of an uptrend in a financial market
    by comparing the current high price to the previous high price, normalized by the Average True Range (ATR).

    :param high: A pandas Series representing the high prices for each period.
    :type high: pd.Series
    :param low: A pandas Series representing the low prices for each period.
    :type low: pd.Series
    :param close: A pandas Series representing the closing prices for each period.
    :type close: pd.Series
    :param di_length: The number of periods over which to calculate the +DI. Default is 14.
    :type di_length: int, optional
    :return: A pandas Series containing the +DI values.
    :rtype: pd.Series
    """
    # Validate arguments
    di_length = get_length(di_length, 14)

    # Calculate the Average True Range (ATR)
    atr_series = atr(high, low, close, di_length)

    # Calculate the Positive Directional Movement (+DM)
    plus_dm = high.diff()
    minus_dm = -low.diff()

    # Keep only positive +DM values where +DM is greater than -DM
    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0.0)

    # Smooth the Positive Directional Movement using Wilder's Smoothing (RMA)
    plus_dm_smoothed = smooth(plus_dm, di_length, SmoothingType.RMA)

    # Calculate the Positive Directional Indicator (+DI)
    plus_di = 100 * (plus_dm_smoothed / atr_series)

    # Return the +DI values as a pandas Series
    return pd.Series(plus_di, name=f'DIPLUS_{di_length}')


def di_minus(high: pd.Series, low: pd.Series, close: pd.Series, di_length: int = 14) -> pd.Series:
    """
    Calculate the Negative Directional Indicator (-DI) for a given price series.

    The Negative Directional Indicator (-DI) is part of the Directional Movement System
    developed by J. Welles Wilder. It measures the presence of a downtrend in a financial market
    by comparing the current low price to the previous low price, normalized by the Average True Range (ATR).

    :param high: A pandas Series representing the high prices for each period.
    :type high: pd.Series
    :param low: A pandas Series representing the low prices for each period.
    :type low: pd.Series
    :param close: A pandas Series representing the closing prices for each period.
    :type close: pd.Series
    :param di_length: The number of periods over which to calculate the -DI. Default is 14.
    :type di_length: int, optional
    :return: A pandas Series containing the -DI values.
    :rtype: pd.Series
    """
    # Validate arguments
    di_length = get_length(di_length, 14)

    # Calculate the Average True Range (ATR)
    atr_series = atr(high, low, close, di_length)

    # Calculate the Negative Directional Movement (-DM)
    plus_dm = high.diff()
    minus_dm = -low.diff()

    # Keep only positive -DM values where -DM is greater than +DM
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0.0)

    # Smooth the Negative Directional Movement using Wilder's Smoothing (RMA)
    minus_dm_smoothed = smooth(minus_dm, di_length, SmoothingType.RMA)

    # Calculate the Negative Directional Indicator (-DI)
    minus_di = 100 * (minus_dm_smoothed / atr_series)

    # Return the -DI values as a pandas Series
    return pd.Series(minus_di, name=f'DIMINUS_{di_length}')
