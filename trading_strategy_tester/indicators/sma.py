import pandas as pd

from trading_strategy_tester.utils.validations import get_length, get_offset


def sma(series: pd.Series, length: int = 9, offset: int = 0) -> pd.Series:
    """
    Calculate the Simple Moving Average (SMA) of a given series.

    The Simple Moving Average (SMA) is a widely-used technical indicator that smooths out price data by creating
    a constantly updated average price over a specified number of periods. It is commonly used to identify
    trends in the data by filtering out the "noise" of short-term fluctuations.

    Parameters:
    -----------
    series : pd.Series
        A pandas Series representing the series data (e.g., closing prices) for which the SMA is to be calculated.
    length : int
        The window length to calculate the SMA.
    offset : int
        The number of periods by which to offset the SMA.

    Returns:
    --------
    pd.Series
        The SMA of the given series.
    """

    # Validate arguments
    length = get_length(length=length, default=9)
    offset = get_offset(offset=offset)

    sma_series = series.rolling(window=length).mean()

    if offset != 0:
        sma_series = sma_series.shift(offset)

    return pd.Series(sma_series, name=f'SMA_{length}_{offset}')