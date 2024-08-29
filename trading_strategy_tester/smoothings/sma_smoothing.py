import pandas as pd

def sma_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculates the Simple Moving Average (SMA) of a given series.

    :param series: The pandas Series representing the data to smooth.
    :type series: pd.Series
    :param length: The window length to use for the SMA calculation.
    :type length: int
    :return: A pandas Series containing the SMA of the given series.
    :rtype: pd.Series
    """
    return series.rolling(window=length).mean()
