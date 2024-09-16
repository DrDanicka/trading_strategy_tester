import pandas as pd

def rma_smoothing(series: pd.Series, length: int) -> pd.Series:
    """
    Calculates the Wilder's Moving Average (RMA), also known as the Rolling Moving Average.

    :param series: The pandas Series representing the data to smooth.
    :type series: pd.Series
    :param length: The smoothing period for the RMA.
    :type length: int
    :return: A pandas Series containing the RMA of the given series.
    :rtype: pd.Series
    """
    return series.ewm(alpha=1 / length, adjust=False, min_periods=length).mean()
