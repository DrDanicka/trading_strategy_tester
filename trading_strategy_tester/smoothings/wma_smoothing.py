import pandas as pd
import numpy as np

def wma_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculate the Weighted Moving Average (WMA) of a given series.

    Parameters:
    -----------
    series : pd.Series
        The data series to calculate the WMA on.
    length : int
        The window length to calculate the WMA.

    Returns:
    --------
    pd.Series
        The WMA of the given series.
    """
    weights = np.arange(1, length + 1)
    wma = series.rolling(window=length).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
    return wma
