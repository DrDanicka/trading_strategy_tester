import pandas as pd


def pvt(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Calculate the Price-Volume Trend (PVT) of a given time series of closing prices and volume.

    The PVT is a cumulative indicator that adjusts volume based on the percentage change in closing price.
    It provides insight into the direction of price movements combined with volume, helping to identify the
    strength of market trends. Positive PVT values suggest accumulation, while negative values indicate distribution.

    :param close: A pandas Series representing the closing prices for the time series data.
    :type close: pd.Series
    :param volume: A pandas Series representing the trading volume corresponding to each closing price.
    :type volume: pd.Series
    :return: A pandas Series containing the cumulative PVT values for the input series, with the same index as the input series.
    :rtype: pd.Series
    """

    # Calculate percentage change
    pct_change = close.pct_change()

    # Multiply percentage change by volume to get PVT increment
    pvt_increment = pct_change * volume

    # Calculate cumulative PVT
    pvt_series = pvt_increment.cumsum().fillna(0)

    return pd.Series(pvt_series, name='PVT')