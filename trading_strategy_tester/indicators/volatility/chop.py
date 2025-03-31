import pandas as pd
import numpy as np

from trading_strategy_tester.utils.parameter_validations import get_length, get_offset

def chop(high: pd.Series, low: pd.Series, close: pd.Series, length: int = 14, offset: int = 0) -> pd.Series:
    """
    Calculate the Choppiness Index for a given financial instrument.

    The Choppiness Index is a technical indicator that measures the market's tendency to trend or to move
    sideways (range). A high Choppiness Index indicates a choppy, sideways market, while a low value suggests
    a strong trending market.

    :param high: A pandas Series containing the high prices of the instrument over a period of time.
    :type high: pd.Series
    :param low: A pandas Series containing the low prices of the instrument over a period of time.
    :type low: pd.Series
    :param close: A pandas Series containing the close prices of the instrument over a period of time.
    :type close: pd.Series
    :param length: The number of periods to use for the calculation of the Choppiness Index. Default is 14.
    :type length: int, optional
    :param offset: The number of periods to shift the resulting series. Default is 0.
    :type offset: int, optional
    :return: A pandas Series containing the Choppiness Index values.
    :rtype: pd.Series
    """

    # Validate the input parameters for length and offset
    length = get_length(length=length, default=14)
    offset = get_offset(offset=offset)

    # Calculate True Range (TR) components
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Compute the sum of True Range over the specified length
    sum_tr = true_range.rolling(window=length).sum()

    # Find the maximum high and minimum low over the specified length
    max_high = high.rolling(window=length).max()
    min_low = low.rolling(window=length).min()

    # Calculate the Choppiness Index using a logarithmic scale
    chop_index = 100 * np.log10(sum_tr / (max_high - min_low)) / np.log10(length)

    # Apply the offset to the resulting series, if specified
    if offset != 0:
        chop_index = chop_index.shift(offset)

    # Return the Choppiness Index as a pandas Series with a descriptive name
    return pd.Series(chop_index, name=f'CHOP_{length}_{offset}')
