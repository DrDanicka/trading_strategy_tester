import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.rma_smoothing import rma_smoothing
from trading_strategy_tester.smoothings.sma_smoothing import sma_smoothing
from trading_strategy_tester.smoothings.ema_smoothing import ema_smoothing
from trading_strategy_tester.smoothings.wma_smoothing import wma_smoothing

def bb_middle(series: pd.Series, length: int = 20, ma_type: SmoothingType = SmoothingType.SMA, std_dev: int = 2, offset: int = 0) -> pd.Series:
    """
    Calculate the middle band (moving average) for Bollinger Bands.

    Parameters:
    -----------
    series : pd.Series
        A pandas Series representing the input time series (e.g., closing prices).
    length : int, optional, default=20
        The number of periods to use for calculating the moving average.
    ma_type : SmoothingType, optional, default=SmoothingType.SMA
        The type of moving average to use (SMA, EMA, WMA, RMA).
    std_dev : int, optional, default=2
        The number of standard deviations to use for calculating the upper and lower bands (not used in this function).
    offset : int, optional, default=0
        The number of periods to offset the resulting series.

    Returns:
    --------
    pd.Series
        A pandas Series containing the middle band (moving average) with the specified offset.
    """

    # Calculate the middle band (moving average) using the selected smoothing method
    if ma_type == SmoothingType.SMA:
        middle_band = sma_smoothing(series, length)
    elif ma_type == SmoothingType.EMA:
        middle_band = ema_smoothing(series, length)
    elif ma_type == SmoothingType.WMA:
        middle_band = wma_smoothing(series, length)
    elif ma_type == SmoothingType.RMA:
        middle_band = rma_smoothing(series, length)
    else:
        raise ValueError("Invalid moving average type selected.")

    # Apply the offset
    if offset != 0:
        middle_band = middle_band.shift(offset)

    return pd.Series(middle_band, name=f'BBMIDDLE_{length}_{ma_type.value}_{std_dev}_{offset}')

def bb_upper(series: pd.Series, length: int = 20, ma_type: SmoothingType = SmoothingType.SMA, std_dev: int = 2, offset: int = 0) -> pd.Series:
    """
    Calculate the upper band for Bollinger Bands.

    Parameters:
    -----------
    series : pd.Series
        A pandas Series representing the input time series (e.g., closing prices).
    length : int, optional, default=20
        The number of periods to use for calculating the moving average.
    ma_type : SmoothingType, optional, default=SmoothingType.SMA
        The type of moving average to use (SMA, EMA, WMA, RMA).
    std_dev : int, optional, default=2
        The number of standard deviations to use for calculating the upper band.
    offset : int, optional, default=0
        The number of periods to offset the resulting series.

    Returns:
    --------
    pd.Series
        A pandas Series containing the upper band with the specified offset.
    """

    # Calculate the standard deviation of the series
    rolling_std = series.rolling(window=length).std(ddof=0)

    # Apply the offset
    if offset != 0:
       rolling_std = rolling_std.shift(offset)

    # Calculate the upper band
    upper_band = bb_middle(series, length, ma_type, std_dev, offset) + (std_dev * rolling_std)

    return pd.Series(upper_band, name=f'BBUPPER_{length}_{ma_type.value}_{std_dev}_{offset}')


def bb_lower(series: pd.Series, length: int = 20, ma_type: SmoothingType = SmoothingType.SMA, std_dev: int = 2, offset: int = 0) -> pd.Series:
    """
    Calculate the lower band for Bollinger Bands.

    Parameters:
    -----------
    series : pd.Series
        A pandas Series representing the input time series (e.g., closing prices).
    length : int, optional, default=20
        The number of periods to use for calculating the moving average.
    ma_type : SmoothingType, optional, default=SmoothingType.SMA
        The type of moving average to use (SMA, EMA, WMA, RMA).
    std_dev : int, optional, default=2
        The number of standard deviations to use for calculating the lower band.
    offset : int, optional, default=0
        The number of periods to offset the resulting series.

    Returns:
    --------
    pd.Series
        A pandas Series containing the lower band with the specified offset.
    """

    # Calculate the standard deviation of the series
    rolling_std = series.rolling(window=length).std(ddof=0)

    # Apply the offset
    if offset != 0:
       rolling_std = rolling_std.shift(offset)

    # Calculate the lower band
    lower_band = bb_middle(series, length, ma_type, std_dev, offset) - (std_dev * rolling_std)

    return pd.Series(lower_band, name=f'BBLOWER_{length}_{ma_type.value}_{std_dev}_{offset}')