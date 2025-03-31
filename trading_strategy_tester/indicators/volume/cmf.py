import pandas as pd

from trading_strategy_tester.utils.parameter_validations import get_length

def cmf(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, length: int = 20) -> pd.Series:
    """
    Calculate the Chaikin Money Flow (CMF) indicator for a given period.

    The Chaikin Money Flow (CMF) measures the accumulation and distribution of a security over a specified period
    by analyzing both price and volume. It provides insights into the buying and selling pressure.

    :param high: A pandas Series containing the high prices for each period.
    :type high: pd.Series
    :param low: A pandas Series containing the low prices for each period.
    :type low: pd.Series
    :param close: A pandas Series containing the closing prices for each period.
    :type close: pd.Series
    :param volume: A pandas Series containing the volume data for each period.
    :type volume: pd.Series
    :param length: The number of periods over which to calculate the CMF. Default is 20.
    :type length: int, optional
    :return: A pandas Series representing the Chaikin Money Flow (CMF) values for the given period.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=20)

    # Calculate the Money Flow Multiplier
    money_flow_multiplier = ((close - low) - (high - close)) / (high - low)

    # Handle division by zero and missing values
    money_flow_multiplier.replace([float('inf'), -float('inf')], 0, inplace=True)
    money_flow_multiplier.fillna(0, inplace=True)

    # Calculate the Money Flow Volume
    money_flow_volume = money_flow_multiplier * volume

    # Calculate the Chaikin Money Flow (CMF)
    cmf_series = (money_flow_volume.rolling(window=length).sum() / volume.rolling(window=length).sum())

    return pd.Series(cmf_series, name=f'CMF_{length}')
