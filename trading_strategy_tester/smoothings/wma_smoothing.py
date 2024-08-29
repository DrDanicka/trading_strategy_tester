import pandas as pd
import numpy as np

def wma_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculates the Weighted Moving Average (WMA) of a given series.

    :param series: The pandas Series representing the data to smooth.
    :type series: pd.Series
    :param length: The window length to use for the WMA calculation.
    :type length: int
    :return: A pandas Series containing the WMA of the given series.
    :rtype: pd.Series
    """
    weights = np.arange(1, length + 1)
    wma = series.rolling(window=length).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
    return wma
