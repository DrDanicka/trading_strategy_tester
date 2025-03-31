import pandas as pd

from trading_strategy_tester.utils.parameter_validations import get_length


def aroon_up(series: pd.Series, length: int = 14) -> pd.Series:
    """
    Calculate the Aroon Up indicator for a given series.

    The Aroon Up indicator measures the number of periods since the highest high within a specified window length.
    It helps identify the strength and direction of an uptrend.

    :param series: A pandas Series containing the series data (e.g., closing prices) for which the Aroon Up is calculated.
    :type series: pd.Series
    :param length: The window length over which to calculate the Aroon Up. Default is 14.
    :type length: int, optional
    :return: A pandas Series containing the Aroon Up values.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=14)

    # Calculate rolling window's highest high index
    rolling_high_idx = series.rolling(window=length + 1).apply(lambda x: x[::-1].argmax(), raw=True)

    # Aroon Up calculation
    aroon_up_series = 100 * (length - rolling_high_idx) / length

    return pd.Series(aroon_up_series, name=f'AROONUP_{length}')


def aroon_down(series: pd.Series, length: int = 14) -> pd.Series:
    """
    Calculate the Aroon Down indicator for a given series.

    The Aroon Down indicator measures the number of periods since the lowest low within a specified window length.
    It helps identify the strength and direction of a downtrend.

    :param series: A pandas Series containing the series data (e.g., closing prices) for which the Aroon Down is calculated.
    :type series: pd.Series
    :param length: The window length over which to calculate the Aroon Down. Default is 14.
    :type length: int, optional
    :return: A pandas Series containing the Aroon Down values.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=14)

    # Calculate rolling window's lowest low index
    rolling_low_idx = series.rolling(window=length + 1).apply(lambda x: x[::-1].argmin(), raw=True)

    # Aroon Down calculation
    aroon_down_series = 100 * (length - rolling_low_idx) / length

    return pd.Series(aroon_down_series, name=f'AROONDOWN_{length}')
