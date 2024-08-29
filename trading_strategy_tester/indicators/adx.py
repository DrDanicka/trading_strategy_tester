import pandas as pd
from trading_strategy_tester.indicators.atr import atr
from trading_strategy_tester.smoothings.rma_smoothing import rma_smoothing
from trading_strategy_tester.utils.validations import get_length


def adx(high: pd.Series, low: pd.Series, close: pd.Series, adx_smoothing: int = 14, DI_length: int = 14) -> pd.Series:
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
    :param DI_length: The period for calculating the Directional Indicators (+DI and -DI). Default is 14.
    :type DI_length: int, optional
    :return: A pandas Series containing the ADX values.
    :rtype: pd.Series
    """

    # Validate arguments
    adx_smoothing = get_length(length=adx_smoothing, default=14)
    DI_length = get_length(length=DI_length, default=14)

    # Calculate Average True Range (ATR)
    atr_series = atr(high, low, close, DI_length)

    # Calculate Directional Movement (+DM and -DM)
    plus_dm = high.diff()
    minus_dm = -low.diff()

    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0.0)
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0.0)

    plus_dm_smoothed = rma_smoothing(plus_dm, DI_length)
    minus_dm_smoothed = rma_smoothing(minus_dm, DI_length)

    # Calculate Directional Indicators (+DI and -DI)
    plus_di = 100 * (plus_dm_smoothed / atr_series)
    minus_di = 100 * (minus_dm_smoothed / atr_series)

    # Calculate the Directional Index (DX)
    dx = 100 * (abs(plus_di - minus_di) / (plus_di + minus_di))

    # Calculate the ADX (Average Directional Index) using Wilder's Moving Average
    adx_series = rma_smoothing(dx, adx_smoothing)

    return pd.Series(adx_series, name=f'ADX_{adx_smoothing}_{DI_length}')
