import pandas as pd
import numpy as np

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.utils.validations import get_length, get_offset
from trading_strategy_tester.indicators.atr import atr

def chop(high: pd.Series, low: pd.Series, close: pd.Series, length: int = 14, offset: int = 0) -> pd.Series:
    """
    Calculates the Choppiness Index for a given financial instrument.

    The Choppiness Index is a volatility indicator that helps determine whether the market is trending or ranging.
    A high Choppiness Index value indicates a choppy, ranging market, while a low value suggests a trending market.

    Parameters:
    -----------
    high : pd.Series
        A pandas Series containing the high prices of the instrument over a period of time.

    low : pd.Series
        A pandas Series containing the low prices of the instrument over a period of time.

    close : pd.Series
        A pandas Series containing the close prices of the instrument over a period of time.

    length : int, optional
        The number of periods to use for the calculation of the Choppiness Index. Default is 14.

    offset : int, optional
        The number of periods to shift the resulting series. Default is 0.

    Returns:
    --------
    pd.Series
        A pandas Series containing the Choppiness Index values.
    """

    # Validate arguments
    length = get_length(length=length, default=14)
    offset = get_offset(offset=offset)

    # Calculate True Range (TR)
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Calculate the sum of the True Range over the specified length
    sum_tr = true_range.rolling(window=length).sum()

    # Calculate the maximum high and minimum low over the specified length
    max_high = high.rolling(window=length).max()
    min_low = low.rolling(window=length).min()

    # Calculate the Choppiness Index
    chop_index = 100 * np.log10(sum_tr / (max_high - min_low)) / np.log10(length)

    # Apply offset if needed
    if offset != 0:
        chop_index = chop_index.shift(offset)

    # Return the Choppiness Index as a pandas Series
    return pd.Series(chop_index, name=f'CHOP_{length}_{offset}')