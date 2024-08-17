import pandas as pd

def rsi(series: pd.Series, length: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI) for a given series.

    The RSI is a momentum oscillator that measures the speed and change of price movements.
    It oscillates between 0 and 100 and is typically used to identify overbought or oversold conditions in a market.

    Parameters:
    -----------
    series : pd.Series
        A pandas Series representing the series data (e.g., closing prices) for which the RSI is to be calculated.
    length : int, optional, default=14
        The number of periods to use for calculating the RSI. The default is 14 periods, which is a common standard.

    Returns:
    --------
    pd.Series
        A pandas Series containing the RSI values for the input time series, with the same index as the input series.
    """
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=length).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=length).mean()
    rs = gain / loss
    return pd.Series(100 - (100 / (1 + rs)), name=f'RSI_{length}')
