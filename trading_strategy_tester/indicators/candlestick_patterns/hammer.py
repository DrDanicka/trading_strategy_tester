import pandas as pd
import numpy as np


def hammer(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """
    Identifies the hammer candlestick pattern in a financial dataset.
    A hammer candlestick pattern is typically a bullish reversal pattern,
    characterized by a small real body (open-close difference) near the top of the candle
    with a long lower shadow.

    :param pd.Series high: Series representing the high prices for each period.
    :param pd.Series low: Series representing the low prices for each period.
    :param pd.Series open: Series representing the opening prices for each period.
    :param pd.Series close: Series representing the closing prices for each period.

    :return: A Series where True indicates the occurrence of a hammer pattern,
             and False otherwise. The Series is named 'HAMMER-CANDLESTICK-PATTERN'.
    :rtype: pd.Series
    """

    # Calculate differences of series
    open_close_diff = np.abs(open - close)
    min_low_diff = np.abs(np.minimum(close, open) - low)

    # Prepare result series
    hammer_series = pd.Series(False, index=high.index)

    # Create hammer condition with 1.8 multiplier
    hammer_condition = ((open == high) | (close == high)) & (1.8 * open_close_diff <= min_low_diff)
    hammer_series[hammer_condition] = True

    return pd.Series(hammer_series, name='HAMMER-CANDLESTICK-PATTERN')

