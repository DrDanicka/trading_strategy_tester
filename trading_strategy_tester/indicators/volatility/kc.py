import pandas as pd
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length
from trading_strategy_tester.indicators.volatility.atr import atr

def kc(high: pd.Series, low: pd.Series, close: pd.Series, series: pd.Series, upper: bool = True, length: int = 20,
       multiplier: int = 2, use_exp_ma: bool = True, atr_length: int = 10) -> pd.Series:
    """
    Calculate the Keltner Channel (KC) upper or lower band.

    The Keltner Channel is a volatility-based envelope set above and below an exponential or simple moving average.
    The width of the channel is determined by a multiple of the Average True Range (ATR).

    :param high: Series of high prices.
    :type high: pd.Series
    :param low: Series of low prices.
    :type low: pd.Series
    :param close: Series of close prices.
    :type close: pd.Series
    :param series: The input price series (e.g., close prices) used to calculate the moving average (basis).
    :type series: pd.Series
    :param upper: If True, returns the upper Keltner Channel; if False, returns the lower channel. Default is True.
    :type upper: bool
    :param length: Lookback period for calculating the moving average. Default is 20.
    :type length: int
    :param multiplier: Multiplier applied to the ATR to adjust the channel width. Default is 2.
    :type multiplier: int
    :param use_exp_ma: If True, uses an exponential moving average (EMA); if False, uses a simple moving average (SMA). Default is True.
    :type use_exp_ma: bool
    :param atr_length: Lookback period for calculating the ATR. Default is 10.
    :type atr_length: int

    :return: The upper or lower Keltner Channel line as a pandas Series.
    :rtype: pd.Series
    """

    # Validate the lookback periods
    length = get_length(length, 20)
    atr_length = get_length(atr_length, 10)

    # Calculate the moving average (basis)
    basis = smooth(series, length, SmoothingType.EMA if use_exp_ma else SmoothingType.SMA)

    # Calculate the ATR and apply the multiplier
    multiple_of_atr = multiplier * atr(high, low, close, atr_length)

    # Return the upper or lower Keltner Channel band
    if upper:
        return pd.Series(basis + multiple_of_atr, name=f'KC-UPPER_{length}_{multiplier}_{use_exp_ma}_{atr_length}')
    else:
        return pd.Series(basis - multiple_of_atr, name=f'KC-LOWER_{length}_{multiplier}_{use_exp_ma}_{atr_length}')
