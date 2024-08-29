import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.ema_smoothing import ema_smoothing
from trading_strategy_tester.smoothings.rma_smoothing import rma_smoothing
from trading_strategy_tester.smoothings.sma_smoothing import sma_smoothing
from trading_strategy_tester.smoothings.wma_smoothing import wma_smoothing

def smooth(series: pd.Series, length: int, smoothing_type: SmoothingType) -> pd.Series:
    """
    Applies the specified smoothing technique to a given price series.

    This function smooths the input data using one of the following methods:
    Simple Moving Average (SMA), Exponential Moving Average (EMA),
    Running Moving Average (RMA), or Weighted Moving Average (WMA).

    :param series: The pandas Series containing the price data to be smoothed.
    :type series: pd.Series
    :param length: The number of periods to use for the smoothing calculation.
    :type length: int
    :param smoothing_type: The type of smoothing to apply, defined in the `SmoothingType` enum.
    :type smoothing_type: SmoothingType
    :return: A pandas Series with the smoothed data.
    :rtype: pd.Series
    """
    if smoothing_type == SmoothingType.SMA:
        # Apply Simple Moving Average smoothing
        return sma_smoothing(series, length)
    elif smoothing_type == SmoothingType.EMA:
        # Apply Exponential Moving Average smoothing
        return ema_smoothing(series, length)
    elif smoothing_type == SmoothingType.RMA:
        # Apply Running Moving Average smoothing
        return rma_smoothing(series, length)
    else:
        # Apply Weighted Moving Average smoothing
        return wma_smoothing(series, length)
