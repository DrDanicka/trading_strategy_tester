import pandas as pd

from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels
from trading_strategy_tester.enums.source_enum import SourceType


def is_in_fib_interval(high: float, low: float, row: pd.Series, fib_level: FibonacciLevels, uptrend: bool) -> bool:
    """
    Checks if the current price is within a specified Fibonacci retracement level.

    This function determines whether the current price (from `row`) falls within the
    calculated Fibonacci level range based on the provided `high` and `low` values.
    The calculation is adjusted depending on whether the trend is an uptrend or downtrend.

    :param high: The highest price in the evaluated range.
    :type high: float
    :param low: The lowest price in the evaluated range.
    :type low: float
    :param row: A pandas Series containing the current price data (including 'High' and 'Low').
    :type row: pd.Series
    :param fib_level: The Fibonacci level to evaluate against.
    :type fib_level: FibonacciLevels
    :param uptrend: A boolean indicating if the trend is uptrend (True) or downtrend (False).
    :type uptrend: bool
    :return: True if the price is within the specified Fibonacci interval, False otherwise.
    :rtype: bool
    """
    # Calculate the price range (difference between high and low)
    diff = high - low

    if uptrend:
        # For uptrend, calculate the Fibonacci retracement value based on the high price
        if fib_level == FibonacciLevels.LEVEL_0:
            fib_value = high
        elif fib_level == FibonacciLevels.LEVEL_23_6:
            fib_value = high - 0.236 * diff
        elif fib_level == FibonacciLevels.LEVEL_38_2:
            fib_value = high - 0.382 * diff
        elif fib_level == FibonacciLevels.LEVEL_50:
            fib_value = high - 0.5 * diff
        elif fib_level == FibonacciLevels.LEVEL_61_8:
            fib_value = high - 0.618 * diff
        else:
            return low < row[SourceType.LOW.value]

        # Check if the current low price is within the Fibonacci retracement level
        return low < row[SourceType.LOW.value] < fib_value

    else:
        # For downtrend, calculate the Fibonacci retracement value based on the low price
        if fib_level == FibonacciLevels.LEVEL_0:
            fib_value = low
        elif fib_level == FibonacciLevels.LEVEL_23_6:
            fib_value = low + 0.236 * diff
        elif fib_level == FibonacciLevels.LEVEL_38_2:
            fib_value = low + 0.382 * diff
        elif fib_level == FibonacciLevels.LEVEL_50:
            fib_value = low + 0.5 * diff
        elif fib_level == FibonacciLevels.LEVEL_61_8:
            fib_value = low + 0.618 * diff
        else:
            return high > row[SourceType.HIGH.value]

        # Check if the current high price is within the Fibonacci retracement level
        return high > row[SourceType.HIGH.value] > fib_value
