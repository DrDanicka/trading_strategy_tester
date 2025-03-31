import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def dpo(series: pd.Series, length: int = 21) -> pd.Series:
    """
    Calculate the Detrended Price Oscillator (DPO).

    The DPO is used to remove long-term trends from prices to identify shorter-term cycles.

    :param series: The price series (e.g., closing prices).
    :param length: The lookback period for DPO calculation. Default is 21.
    :return: A pandas Series containing the DPO values.
    """

    # Validate arguments
    length = get_length(length=length, default=21)

    # Calculate the Simple Moving Average (SMA)
    sma = smooth(series, length=length, smoothing_type=SmoothingType.SMA)

    # Shift the SMA by (length // 2 + 1) periods
    sma_shifted = sma.shift(length // 2 + 1)

    # Calculate the DPO
    dpo_series = series - sma_shifted

    return pd.Series(dpo_series, name=f'DPO_{length}')