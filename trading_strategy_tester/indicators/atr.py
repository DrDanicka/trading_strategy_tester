import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.rma_smoothing import rma_smoothing
from trading_strategy_tester.smoothings.sma_smoothing import sma_smoothing
from trading_strategy_tester.smoothings.ema_smoothing import ema_smoothing
from trading_strategy_tester.smoothings.wma_smoothing import wma_smoothing
from trading_strategy_tester.utils.validations import get_length


def atr(high: pd.Series, low: pd.Series, close: pd.Series, length: int = 14,
        smoothing: SmoothingType = SmoothingType.RMA) -> pd.Series:
    """
    Calculate the Average True Range (ATR) of a given series with a specified smoothing method.

    The Average True Range (ATR) is a measure of volatility that considers the greatest of the following for each period:
    - The difference between the current high and low.
    - The difference between the previous close and the current high.
    - The difference between the previous close and the current low.

    Parameters:
    -----------
    high : pd.Series
        A pandas Series representing the high prices.
    low : pd.Series
        A pandas Series representing the low prices.
    close : pd.Series
        A pandas Series representing the closing prices.
    length : int
        The window length to calculate the ATR.
    smoothing : SmoothingType
        The smoothing method to use. Can be 'RMA', 'SMA', 'EMA', or 'WMA'.

    Returns:
    --------
    pd.Series
        The ATR of the given series.
    """

    # Validate arguments
    length = get_length(length=length, default=14)

    # Calculate True Range (TR)
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Calculate ATR based on the specified smoothing method
    if smoothing == SmoothingType.RMA:
        atr_series = rma_smoothing(true_range, length)
    elif smoothing == SmoothingType.SMA:
        atr_series = sma_smoothing(true_range, length)
    elif smoothing == SmoothingType.EMA:
        atr_series = ema_smoothing(true_range, length)
    else:
        atr_series = wma_smoothing(true_range, length)

    return pd.Series(atr_series, name=f'ATR_{length}_{smoothing.value}')
