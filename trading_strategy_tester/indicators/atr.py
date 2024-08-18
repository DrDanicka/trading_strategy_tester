import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType


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

    # Calculate True Range (TR)
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Calculate ATR based on the specified smoothing method
    if smoothing == SmoothingType.RMA:
        atr_series = true_range.ewm(alpha=1/length, adjust=False).mean()
    elif smoothing == SmoothingType.SMA:
        atr_series = true_range.rolling(window=length).mean()
    elif smoothing == SmoothingType.EMA:
        atr_series = true_range.ewm(span=length, adjust=False).mean()
    elif smoothing == SmoothingType.WMA:
        weights = pd.Series(range(1, length + 1))
        atr_series = true_range.rolling(window=length).apply(lambda x: (x * weights).sum() / weights.sum(), raw=True)
    else:
        raise ValueError("Invalid smoothing method. Choose from SmoothingType enum.")

    return pd.Series(atr_series, name=f'ATR_{length}_{smoothing.value}')
