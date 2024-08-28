import pandas as pd

from trading_strategy_tester.utils.validations import get_length


def cmf(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, length: int = 20) -> pd.Series:
    """
    Calculates the Chaikin Money Flow (CMF) indicator for a given period.

    The Chaikin Money Flow is a technical analysis indicator that measures the buying and selling pressure
    over a specified period, typically using volume and price data.

    Parameters:
    -----------
    high : pd.Series
        A pandas Series containing the high prices for each period.

    low : pd.Series
        A pandas Series containing the low prices for each period.

    close : pd.Series
        A pandas Series containing the closing prices for each period.

    volume : pd.Series
        A pandas Series containing the volume data for each period.

    length : int, optional
        The number of periods over which to calculate the CMF (default is 20).

    Returns:
    --------
    pd.Series
        A pandas Series representing the Chaikin Money Flow (CMF) values for the given period.
    """

    # Validate arguments
    length = get_length(length=length, default=20)

    # Calculate the Money Flow Multiplier
    # The multiplier measures the position of the close price relative to the high-low range
    money_flow_multiplier = ((close - low) - (high - close)) / (high - low)

    # Replace division by zero cases and missing values with 0 to avoid errors
    money_flow_multiplier.replace([float('inf'), -float('inf')], 0, inplace=True)
    money_flow_multiplier.fillna(0, inplace=True)

    # Calculate the Money Flow Volume by multiplying the Money Flow Multiplier with the volume
    money_flow_volume = money_flow_multiplier * volume

    # Calculate the Chaikin Money Flow (CMF) by taking the rolling sum of Money Flow Volume and Volume over the specified period
    cmf_series = (money_flow_volume.rolling(window=length).sum() / volume.rolling(window=length).sum())

    # Return the CMF values as a pandas Series, with an appropriate name
    return pd.Series(cmf_series, name=f'CMF_{length}')
