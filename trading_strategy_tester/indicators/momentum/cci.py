import pandas as pd
import numpy as np

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.sma_smoothing import sma_smoothing
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def cci(series: pd.Series, length: int = 20, smoothing_type: SmoothingType = SmoothingType.SMA, smoothing_length: int = 1) -> pd.Series:
    """
    Calculate the Commodity Channel Index (CCI) for a given financial instrument.

    The Commodity Channel Index is a versatile indicator that measures the deviation of the price from its average.
    High values indicate overbought conditions, and low values indicate oversold conditions.

    :param series: A pandas Series containing the price data (e.g., 'Typical Price' which is (high + low + close) / 3).
    :type series: pd.Series
    :param length: The number of periods to use for the calculation of the CCI. Default is 20.
    :type length: int, optional
    :param smoothing_type: The type of smoothing to apply to the CCI calculation. Can be 'SMA', 'EMA', etc. Default is SmoothingType.SMA.
    :type smoothing_type: SmoothingType, optional
    :param smoothing_length: The number of periods for the smoothing calculation. Default is 1.
    :type smoothing_length: int, optional
    :return: A pandas Series containing the CCI values.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=20)
    smoothing_length = get_length(length=smoothing_length, default=1)

    # Calculate the Simple Moving Average (SMA) of the Typical Price
    sma_typical_price = sma_smoothing(series, length)

    # Calculate the Mean Deviation
    mean_deviation = series.rolling(window=length).apply(lambda x: np.mean(np.abs(x - np.mean(x))), raw=True)

    # Calculate the CCI
    cci = (series - sma_typical_price) / (0.015 * mean_deviation)

    # Optional Smoothing
    cci_smoothed = smooth(cci, length=smoothing_length, smoothing_type=smoothing_type)

    # Return the smoothed CCI as a pandas Series with a descriptive name
    return pd.Series(cci_smoothed, name=f'CCI_{length}_{smoothing_type.value}_{smoothing_length}')