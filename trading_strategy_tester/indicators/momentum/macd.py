import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def macd(series: pd.Series, fast_length: int = 12, slow_length: int = 26, ma_type: SmoothingType = SmoothingType.EMA):
    """
    Calculate the Moving Average Convergence Divergence (MACD) for a given price series.
    MACD is a momentum indicator that is derived by subtracting a slow-moving average
    from a fast-moving average.

    :param series: A pandas Series representing the price data (e.g., close prices) on which to calculate MACD.
    :type series: pd.Series
    :param fast_length: The number of periods for the fast moving average. Default is 12.
    :type fast_length: int, optional
    :param slow_length: The number of periods for the slow moving average. Default is 26.
    :type slow_length: int, optional
    :param ma_type: The type of moving average to use (e.g., EMA). Default is SmoothingType.EMA.
    :type ma_type: SmoothingType, optional
    :return: A pandas Series containing the MACD values for the specified series, indexed by the same index as the input series.
    :rtype: pd.Series
    """
    # Validate the fast and slow lengths for the moving averages
    fast_length = get_length(length=fast_length, default=12)
    slow_length = get_length(length=slow_length, default=26)

    # Calculate the MACD by subtracting the slow moving average from the fast moving average
    macd_series = smooth(series, fast_length, ma_type) - smooth(series, slow_length, ma_type)

    # Return the MACD series with an appropriate name
    return pd.Series(macd_series, name=f'MACD_{fast_length}_{slow_length}_{ma_type.value}')


def macd_signal(series: pd.Series, fast_length: int = 12, slow_length: int = 26,
                oscillator_ma_type: SmoothingType = SmoothingType.EMA,
                signal_ma_type: SmoothingType = SmoothingType.EMA, signal_length: int = 9):
    """
    Calculate the MACD Signal line, which is a smoothed average of the MACD and is commonly used
    to identify buy/sell signals.

    :param series: A pandas Series representing the price data (e.g., close prices) for which the MACD signal line is calculated.
    :type series: pd.Series
    :param fast_length: The period for the fast moving average used in the MACD calculation. Default is 12.
    :type fast_length: int, optional
    :param slow_length: The period for the slow moving average used in the MACD calculation. Default is 26.
    :type slow_length: int, optional
    :param oscillator_ma_type: The type of moving average for the MACD oscillator calculation. Default is SmoothingType.EMA.
    :type oscillator_ma_type: SmoothingType, optional
    :param signal_ma_type: The type of moving average for the MACD signal line calculation. Default is SmoothingType.EMA.
    :type signal_ma_type: SmoothingType, optional
    :param signal_length: The period for the moving average applied to the MACD to create the signal line. Default is 9.
    :type signal_length: int, optional
    :return: A pandas Series containing the MACD signal values, indexed by the same index as the input series.
    :rtype: pd.Series
    """
    # Validate the signal length for the moving average
    signal_length = get_length(length=signal_length, default=9)

    # Calculate the MACD series
    macd_series = macd(series, fast_length, slow_length, oscillator_ma_type)

    # Calculate the signal line by smoothing the MACD series
    macd_signal = smooth(macd_series, signal_length, signal_ma_type)

    # Return the MACD signal line with an appropriate name
    return pd.Series(macd_signal, name=f'MACD-SIGNAL_{fast_length}_{slow_length}_{oscillator_ma_type.value}_{signal_ma_type.value}_{signal_length}')
