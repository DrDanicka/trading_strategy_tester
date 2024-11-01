import pandas as pd


def pvi(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Calculate the Positive Volume Index (PVI), which tracks price changes on days
    when volume increases. The PVI is often used to measure the behavior of "uninformed"
    investors, as it is believed they are more likely to trade during high-volume days.

    :param close: A pandas Series representing the closing prices of the asset.
    :type close: pd.Series
    :param volume: A pandas Series representing the volume traded.
    :type volume: pd.Series
    :return: A pandas Series containing the cumulative PVI values, indexed by the same index as the input series.
    :rtype: pd.Series
    """
    # Calculate the price change factor, multiplying percentage change in close by volume.
    # Fill missing values with 0 to handle NaNs from percentage change and use cumulative sum to get PVI.
    vt = (close.pct_change() * volume).fillna(0).cumsum()

    # Return the PVI series
    return pd.Series(vt, name='PVI')
