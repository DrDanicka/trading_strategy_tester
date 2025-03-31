import pandas as pd
from trading_strategy_tester.indicators.momentum.dmi import di_plus, di_minus
from trading_strategy_tester.smoothings.rma_smoothing import rma_smoothing
from trading_strategy_tester.utils.parameter_validations import get_length


def adx(high: pd.Series, low: pd.Series, close: pd.Series, adx_smoothing: int = 14, di_length: int = 14) -> pd.Series:
    """
    Calculate the Average Directional Index (ADX) and the Directional Indicators (+DI and -DI).

    The ADX is a trend strength indicator used to quantify the strength of a trend by analyzing
    the expansion of the price range over a specified period. It also calculates the Directional Indicators
    (+DI and -DI) which help in identifying the direction of the trend.

    :param high: A pandas Series containing the high prices of the financial instrument.
    :type high: pd.Series
    :param low: A pandas Series containing the low prices of the financial instrument.
    :type low: pd.Series
    :param close: A pandas Series containing the closing prices of the financial instrument.
    :type close: pd.Series
    :param adx_smoothing: The period for smoothing the ADX calculation. Default is 14.
    :type adx_smoothing: int, optional
    :param di_length: The period for calculating the Directional Indicators (+DI and -DI). Default is 14.
    :type di_length: int, optional
    :return: A pandas Series containing the ADX values.
    :rtype: pd.Series
    """

    # Validate arguments
    adx_smoothing = get_length(length=adx_smoothing, default=14)
    di_length = get_length(length=di_length, default=14)

    # Calculate Directional Indicators (+DI and -DI)
    plus_di = di_plus(high=high, low=low, close=close, di_length=di_length)
    minus_di = di_minus(high=high, low=low, close=close, di_length=di_length)

    # Calculate the Directional Index (DX)
    dx = 100 * (abs(plus_di - minus_di) / (plus_di + minus_di))

    # Calculate the ADX (Average Directional Index) using Wilder's Moving Average
    adx_series = rma_smoothing(dx, adx_smoothing)

    return pd.Series(adx_series, name=f'ADX_{adx_smoothing}_{di_length}')
