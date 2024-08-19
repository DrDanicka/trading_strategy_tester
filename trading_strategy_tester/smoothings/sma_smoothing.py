import pandas as pd

def sma_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculate the Simple Moving Average (SMA) of a given series.

    Parameters:
    -----------
    series : pd.Series
        The data series to calculate the SMA on.
    length : int
        The window length to calculate the SMA.

    Returns:
    --------
    pd.Series
        The SMA of the given series.
    """
    return series.rolling(window=length).mean()
