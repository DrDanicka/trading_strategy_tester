import pandas as pd

from trading_strategy_tester.utils.parameter_validations import get_length


def conversion_line(high: pd.Series, low: pd.Series, length: int=9) -> pd.Series:
    """
    Calculate the Conversion Line (Tenkan-sen) of the Ichimoku Cloud.

    :param high: Series of high prices.
    :type high: pd.Series
    :param low: Series of low prices.
    :type low: pd.Series
    :param length: Period over which to calculate the Conversion Line (default is 9).
    :type length: int
    :return: The Conversion Line (Tenkan-sen) values.
    :rtype: pd.Series
    """
    # Validate parameters
    length = get_length(length, 9)

    highest_high = high.rolling(window=length).max()
    lowest_low = low.rolling(window=length).min()
    tenkan_sen = (highest_high + lowest_low) / 2
    return pd.Series(tenkan_sen, name=f'ICHIMOKU-CONVERSION-LINE_{length}')


def base_line(high: pd.Series, low: pd.Series, length: int = 26) -> pd.Series:
    """
    Calculate the Base Line (Kijun-sen) of the Ichimoku Cloud.

    :param high: Series of high prices.
    :type high: pd.Series
    :param low: Series of low prices.
    :type low: pd.Series
    :param length: Period over which to calculate the Base Line (default is 26).
    :type length: int
    :return: The Base Line (Kijun-sen) values.
    :rtype: pd.Series
    """
    # Validate parameters
    length = get_length(length, 26)

    highest_high = high.rolling(window=length).max()
    lowest_low = low.rolling(window=length).min()
    kijun_sen = (highest_high + lowest_low) / 2
    return pd.Series(kijun_sen, name=f'ICHIMOKU-BASE-LINE_{length}')


def leading_span_a(high: pd.Series, low: pd.Series, displacement: int = 26) -> pd.Series:
    """
    Calculate the Leading Span A (Senkou Span A) of the Ichimoku Cloud.

    Senkou Span A is the midpoint between the Conversion Line (Tenkan-sen) and Base Line (Kijun-sen),
    shifted forward by the 'displacement' period (default is 26).

    :param high: Series of high prices.
    :type high: pd.Series
    :param low: Series of low prices.
    :type low: pd.Series
    :param displacement: Number of periods to shift forward (default is 26).
    :type displacement: int
    :return: The Senkou Span A values.
    :rtype: pd.Series
    """
    conversion_line_ser = conversion_line(high, low)
    base_line_ser = base_line(high, low)
    span_a = (conversion_line_ser + base_line_ser) / 2
    senkou_span_a = span_a.shift(displacement - 1)
    return pd.Series(senkou_span_a, name=f'ICHIMOKU-SPAN-A_{displacement}')


def leading_span_b(high: pd.Series, low: pd.Series, length: int = 52, displacement: int = 26) -> pd.Series:
    """
    Calculate the Leading Span B (Senkou Span B) of the Ichimoku Cloud.

    Senkou Span B is the midpoint of the highest high and lowest low over 'length' periods,
    shifted forward by the 'displacement' period (default is 26).

    :param high: Series of high prices.
    :type high: pd.Series
    :param low: Series of low prices.
    :type low: pd.Series
    :param length: Period over which to calculate the highest high and lowest low (default is 52).
    :type length: int
    :param displacement: Number of periods to shift forward (default is 26).
    :type displacement: int
    :return: The Senkou Span B values.
    :rtype: pd.Series
    """
    # Validate parameters
    length = get_length(length, 52)

    span_b = base_line(high, low, length)
    senkou_span_b = span_b.shift(displacement - 1)
    return pd.Series(senkou_span_b, name=f'ICHIMOKU-SPAN-B_{length}_{displacement}')


def lagging_span(close: pd.Series, displacement: int = 26) -> pd.Series:
    """
    Calculate the Lagging Span (Chikou Span) of the Ichimoku Cloud.

    The Chikou Span is the closing price shifted backwards by the 'displacement' period (default is 26).

    :param close: Series of closing prices.
    :type close: pd.Series
    :param displacement: Number of periods to shift backwards (default is 26).
    :type displacement: int
    :return: The Chikou Span values.
    :rtype: pd.Series
    """
    chikou_span = close.shift(-displacement + 1)
    return pd.Series(chikou_span, name=f'ICHIMOKU-LAGGING-SPAN_{displacement}')
