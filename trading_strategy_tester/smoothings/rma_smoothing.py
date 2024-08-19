import pandas as pd

def rma_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculate the Wilder's Moving Average, also known as RMA (Rolling Moving Average).

    Parameters:
    -----------
    series : pd.Series
        The data series to calculate the RMA on.
    length : int
        The smoothing period for the RMA.

    Returns:
    --------
    pd.Series
        The RMA of the given series.
    """
    return series.ewm(alpha=1 / length, adjust=False).mean()