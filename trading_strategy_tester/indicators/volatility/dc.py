import pandas as pd

from trading_strategy_tester.utils.parameter_validations import get_length, get_offset

def dc_upper(high: pd.Series, length: int = 20, offset: int = 0) -> pd.Series:
    """
    Calculate the upper band of the Donchian Channel.

    The upper band is determined by taking the highest high over a specified rolling window (length).
    It helps identify resistance levels or the upper boundary of price movement.

    :param high: A pandas Series representing the high prices of a financial instrument.
    :param length: The window length for calculating the highest high. Default is 20.
    :param offset: The number of periods by which to offset the upper band. Default is 0.
    :return: A pandas Series containing the upper band of the Donchian Channel.
    """
    # Validate arguments
    length = get_length(length=length, default=20)
    offset = get_offset(offset=offset)

    # Calculate the upper band of the Donchian Channel
    dc_upper_series = high.rolling(window=length).max()

    # Apply offset if specified
    if offset > 0:
        dc_upper_series = dc_upper_series.shift(offset)

    return pd.Series(dc_upper_series, name=f'DCUPPER_{length}_{offset}')

def dc_lower(low: pd.Series, length: int = 20, offset: int = 0) -> pd.Series:
    """
    Calculate the lower band of the Donchian Channel.

    The lower band is determined by taking the lowest low over a specified rolling window (length).
    It helps identify support levels or the lower boundary of price movement.

    :param low: A pandas Series representing the low prices of a financial instrument.
    :param length: The window length for calculating the lowest low. Default is 20.
    :param offset: The number of periods by which to offset the lower band. Default is 0.
    :return: A pandas Series containing the lower band of the Donchian Channel.
    """
    # Validate arguments
    length = get_length(length=length, default=20)
    offset = get_offset(offset=offset)

    # Calculate the lower band of the Donchian Channel
    dc_lower_series = low.rolling(window=length).min()

    # Apply offset if specified
    if offset > 0:
        dc_lower_series = dc_lower_series.shift(offset)

    return pd.Series(dc_lower_series, name=f'DCLOWER_{length}_{offset}')

def dc_basis(high: pd.Series, low: pd.Series, length: int = 20, offset: int = 0) -> pd.Series:
    """
    Calculate the basis (midpoint) of the Donchian Channel.

    The basis is the average of the upper and lower bands, which represents the midpoint of price movement
    over the specified rolling window (length).

    :param high: A pandas Series representing the high prices of a financial instrument.
    :param low: A pandas Series representing the low prices of a financial instrument.
    :param length: The window length for calculating the Donchian Channel bands. Default is 20.
    :param offset: The number of periods by which to offset the basis. Default is 0.
    :return: A pandas Series containing the basis of the Donchian Channel.
    """
    # Validate arguments
    length = get_length(length=length, default=20)
    offset = get_offset(offset=offset)

    # Calculate the upper and lower bands of the Donchian Channel
    dc_upper_series = dc_upper(high, length=length, offset=offset)
    dc_lower_series = dc_lower(low, length=length, offset=offset)

    # Calculate the basis as the average of the upper and lower bands
    dc_basis_series = (dc_upper_series + dc_lower_series) / 2

    return pd.Series(dc_basis_series, name=f'DCBASIS_{length}_{offset}')
