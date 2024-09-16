import pandas as pd

def ema_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculates the Exponential Moving Average (EMA) for a given series.

    :param series: The pandas Series representing the data to smooth.
    :type series: pd.Series
    :param length: The smoothing period for the EMA.
    :type length: int
    :return: A pandas Series containing the EMA of the given series.
    :rtype: pd.Series
    """
    return series.ewm(span=length, adjust=False, min_periods=length).mean()
