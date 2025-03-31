import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length, get_std_dev, get_offset


def bb_middle(series: pd.Series, length: int = 20, ma_type: SmoothingType = SmoothingType.SMA, std_dev: float = 2,
              offset: int = 0) -> pd.Series:
    """
    Calculate the middle band (moving average) for Bollinger Bands.

    The middle band is a moving average of the input series, used as the centerline for the Bollinger Bands.

    :param series: A pandas Series representing the input time series (e.g., closing prices).
    :type series: pd.Series
    :param length: The number of periods to use for calculating the moving average. Default is 20 periods.
    :type length: int, optional
    :param ma_type: The type of moving average to use. Can be 'SMA', 'EMA', 'WMA', or 'RMA'. Default is SmoothingType.SMA.
    :type ma_type: SmoothingType, optional
    :param std_dev: The number of standard deviations to use for calculating the upper and lower bands (not used in this function). Default is 2.
    :type std_dev: float, optional
    :param offset: The number of periods to offset the resulting series. Default is 0.
    :type offset: int, optional
    :return: A pandas Series containing the middle band (moving average) with the specified offset.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=20)
    std_dev = get_std_dev(std_dev=std_dev, default=2)
    offset = get_offset(offset=offset)

    # Calculate the middle band (moving average) using the selected smoothing method
    middle_band = smooth(series, length, ma_type)

    # Apply the offset
    if offset != 0:
        middle_band = middle_band.shift(offset)

    return pd.Series(middle_band, name=f'BBMIDDLE_{length}_{ma_type.value}_{std_dev}_{offset}')


def bb_upper(series: pd.Series, length: int = 20, ma_type: SmoothingType = SmoothingType.SMA, std_dev: float = 2,
             offset: int = 0) -> pd.Series:
    """
    Calculate the upper band for Bollinger Bands.

    The upper band is calculated as the middle band plus a multiple of the rolling standard deviation.

    :param series: A pandas Series representing the input time series (e.g., closing prices).
    :type series: pd.Series
    :param length: The number of periods to use for calculating the moving average. Default is 20 periods.
    :type length: int, optional
    :param ma_type: The type of moving average to use. Can be 'SMA', 'EMA', 'WMA', or 'RMA'. Default is SmoothingType.SMA.
    :type ma_type: SmoothingType, optional
    :param std_dev: The number of standard deviations to use for calculating the upper band. Default is 2.
    :type std_dev: float, optional
    :param offset: The number of periods to offset the resulting series. Default is 0.
    :type offset: int, optional
    :return: A pandas Series containing the upper band with the specified offset.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=20)
    std_dev = get_std_dev(std_dev=std_dev, default=2)
    offset = get_offset(offset=offset)

    # Calculate the standard deviation of the series
    rolling_std = series.rolling(window=length).std(ddof=0)

    # Apply the offset
    if offset != 0:
        rolling_std = rolling_std.shift(offset)

    # Calculate the upper band
    upper_band = bb_middle(series, length, ma_type, std_dev, offset) + (std_dev * rolling_std)

    return pd.Series(upper_band, name=f'BBUPPER_{length}_{ma_type.value}_{std_dev}_{offset}')


def bb_lower(series: pd.Series, length: int = 20, ma_type: SmoothingType = SmoothingType.SMA, std_dev: float = 2,
             offset: int = 0) -> pd.Series:
    """
    Calculate the lower band for Bollinger Bands.

    The lower band is calculated as the middle band minus a multiple of the rolling standard deviation.

    :param series: A pandas Series representing the input time series (e.g., closing prices).
    :type series: pd.Series
    :param length: The number of periods to use for calculating the moving average. Default is 20 periods.
    :type length: int, optional
    :param ma_type: The type of moving average to use. Can be 'SMA', 'EMA', 'WMA', or 'RMA'. Default is SmoothingType.SMA.
    :type ma_type: SmoothingType, optional
    :param std_dev: The number of standard deviations to use for calculating the lower band. Default is 2.
    :type std_dev: float, optional
    :param offset: The number of periods to offset the resulting series. Default is 0.
    :type offset: int, optional
    :return: A pandas Series containing the lower band with the specified offset.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=20)
    std_dev = get_std_dev(std_dev=std_dev, default=2)
    offset = get_offset(offset=offset)

    # Calculate the standard deviation of the series
    rolling_std = series.rolling(window=length).std(ddof=0)

    # Apply the offset
    if offset != 0:
        rolling_std = rolling_std.shift(offset)

    # Calculate the lower band
    lower_band = bb_middle(series, length, ma_type, std_dev, offset) - (std_dev * rolling_std)

    return pd.Series(lower_band, name=f'BBLOWER_{length}_{ma_type.value}_{std_dev}_{offset}')
