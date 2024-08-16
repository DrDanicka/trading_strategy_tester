import pandas as pd


def sma(series: pd.Series, length: int = 14, offset: int = 0) -> pd.Series:
    """
    Calculate the Simple Moving Average (SMA) of a given series.

    Parameters:
    series (pd.Series): The data series (e.g., closing prices) for which to calculate the SMA.
    length (int): The window length to calculate the SMA.
    offset (int): The number of periods by which to offset the SMA.

    Returns:
    pd.Series: The SMA of the given series.
    """
    sma_series = series.rolling(window=length).mean()

    if offset != 0:
        sma_series = sma_series.shift(offset)

    return sma_series