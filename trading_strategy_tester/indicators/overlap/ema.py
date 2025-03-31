import pandas as pd

from trading_strategy_tester.utils.parameter_validations import get_length, get_offset

def ema(series: pd.Series, length: int = 9, offset: int = 0) -> pd.Series:
    """
    Calculate the Exponential Moving Average (EMA) of a given series.

    The Exponential Moving Average (EMA) is a type of moving average that gives more weight to recent data points,
    making it more responsive to new information compared to the Simple Moving Average (SMA). It is commonly used
    in technical analysis to identify trends and to smooth out price data.

    :param series: A pandas Series representing the series data (e.g., closing prices) for which the EMA is to be calculated.
    :type series: pd.Series
    :param length: The window length to calculate the EMA. Default is 9.
    :type length: int, optional
    :param offset: The number of periods by which to offset the EMA. Default is 0.
    :type offset: int, optional
    :return: A pandas Series containing the EMA of the given series.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=9)
    offset = get_offset(offset=offset)

    ema_series = series.ewm(span=length, adjust=False).mean()

    if offset != 0:
        ema_series = ema_series.shift(offset)

    return pd.Series(ema_series, name=f'EMA_{length}_{offset}')
