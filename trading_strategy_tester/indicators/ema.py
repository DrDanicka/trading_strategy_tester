import pandas as pd


def ema(series: pd.Series, length: int = 14, offset: int = 0) -> pd.Series:
    """
    Calculate the Exponential Moving Average (EMA) of a given series.

    The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent data points,
    making it more responsive to new information compared to the Simple Moving Average (SMA). It is commonly used
    in technical analysis to identify trends and to smooth out price data.

    Parameters:
    -----------
    series : pd.Series
        A pandas Series representing the series data (e.g., closing prices) for which the EMA is to be calculated.
    length : int
        The window length to calculate the EMA.
    offset : int
        The number of periods by which to offset the EMA.

    Returns:
    --------
    pd.Series
        The EMA of the given series.
    """
    ema_series = series.ewm(span=length, adjust=False).mean()

    if offset != 0:
        ema_series = ema_series.shift(offset)

    return pd.Series(ema_series, name=f'EMA_{length}_{offset}')