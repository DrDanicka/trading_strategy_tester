import pandas as pd

def ema_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculate the Exponential Moving Average (EMA) of a given series.

    Parameters:
    -----------
    series : pd.Series
        The data series to calculate the EMA on.
    length : int
        The smoothing period for the EMA.

    Returns:
    --------
    pd.Series
        The EMA of the given series.
    """
    return series.ewm(span=length, adjust=False).mean()
