import pandas as pd
import numpy as np

def obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Calculate the On-Balance Volume (OBV) indicator, which accumulates volume based on price direction.
    The OBV helps to identify buying and selling pressure by comparing volume flow with price movements.

    :param close: A pandas Series representing the closing prices of the asset.
    :type close: pd.Series
    :param volume: A pandas Series representing the volume traded.
    :type volume: pd.Series
    :param length: The period over which the OBV is smoothed (optional). Default is 5.
    :type length: int, optional
    :return: A pandas Series containing the OBV values, smoothed over the specified period.
    :rtype: pd.Series
    """

    # Calculate the daily change in price and get its sign
    price_change = close.diff()
    direction = np.sign(price_change)

    # Calculate OBV by cumulatively summing volume based on the direction of price changes
    obv_values = (direction * volume).fillna(0).cumsum()

    # Return the OBV series with a descriptive name
    return pd.Series(obv_values, name="OBV")
