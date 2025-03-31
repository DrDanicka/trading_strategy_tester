import numpy as np
import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def trix(close: pd.Series, length: int = 18) -> pd.Series:
    """
    Calculate the TRIX (Triple Exponential Average) indicator for a given financial instrument.

    TRIX is a momentum oscillator that measures the rate of change of a triple-smoothed exponential
    moving average (EMA) of the logarithm of the closing prices. It is commonly used to identify
    overbought and oversold conditions, as well as potential price reversals in a time series.

    :param close: Series of closing prices for the financial instrument.
    :type close: pd.Series
    :param length: The number of periods over which to calculate each EMA. Default is 18.
    :type length: int, optional
    :return: A pandas Series containing the TRIX values, labeled with the appropriate name.
    :rtype: pd.Series
    """

    # Validate the length argument to ensure it is correctly set
    length = get_length(length=length, default=18)

    # Calculate the first EMA of the logarithmic closing prices
    ema1 = smooth(series=np.log(close), length=length, smoothing_type=SmoothingType.EMA)

    # Calculate the second EMA of the first EMA
    ema2 = smooth(series=ema1, length=length, smoothing_type=SmoothingType.EMA)

    # Calculate the third EMA of the second EMA
    ema3 = smooth(series=ema2, length=length, smoothing_type=SmoothingType.EMA)

    # Calculate the TRIX as 10,000 times the percentage rate of change of the third EMA
    trix_series = 10_000 * ema3.diff()

    return pd.Series(trix_series, name=f'TRIX_{length}')
