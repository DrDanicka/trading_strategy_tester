import pandas as pd
from trading_strategy_tester.utils.parameter_validations import get_length

def mfi(hlc3: pd.Series, volume: pd.Series, length: int = 14) -> pd.Series:
    """
    Calculate the Money Flow Index (MFI), a momentum indicator that measures the flow of money
    into and out of an asset over a given period. MFI uses both price and volume to identify
    overbought or oversold conditions.

    :param hlc3: A pandas Series representing the typical price of the asset, calculated as
                 (High + Close + Low) / 3.0
    :type hlc3: pd.Series
    :param volume: A pandas Series representing the volume traded.
    :type volume: pd.Series
    :param length: The period over which the MFI is calculated. Default is 14.
    :type length: int, optional
    :return: A pandas Series containing the MFI values.
    :rtype: pd.Series
    """
    # Validate the length parameter
    length = get_length(length=length, default=14)

    # Calculate Money Flow (MF)
    mf = hlc3 * volume

    # Identify Positive and Negative Money Flow based on price changes
    positive_mf = mf.where(hlc3 > hlc3.shift(1), 0)
    negative_mf = mf.where(hlc3 < hlc3.shift(1), 0)

    # Calculate the sum of Positive and Negative Money Flow over the specified length
    positive_mf_sum = positive_mf.rolling(window=length).sum()
    negative_mf_sum = negative_mf.rolling(window=length).sum()

    # Calculate the Money Flow Ratio
    money_flow_ratio = positive_mf_sum / negative_mf_sum

    # Calculate the Money Flow Index (MFI)
    mfi_series = 100 - (100 / (1 + money_flow_ratio))

    # Return the MFI series with a name for easy identification
    return pd.Series(mfi_series, name=f'MFI_{length}')
