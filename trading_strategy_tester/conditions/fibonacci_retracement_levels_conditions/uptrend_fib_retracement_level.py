import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.utils.fib_utils import is_in_fib_interval
from trading_strategy_tester.utils.parameter_validations import get_length


class UptrendFibRetracementLevelCondition(Condition):
    """
    Condition to check if the price is in a Fibonacci retracement level during an uptrend.

    This condition evaluates whether the price falls within a specific Fibonacci retracement
    level during an uptrend by analyzing a historical price window of the specified length.
    """

    def __init__(self, fib_level: FibonacciLevels, length: int = 14):
        """
        Initialize the condition with a specified Fibonacci level and length of the price window.

        :param fib_level: The Fibonacci level to check against.
        :type fib_level: FibonacciLevels
        :param length: The length of the price window to evaluate, default is 14.
        :type length: int
        """
        self.fib_level = fib_level
        self.length = get_length(length, 14)

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the condition on the provided DataFrame.

        This method checks whether the price is within the specified Fibonacci level during an uptrend
        based on the lowest low and highest high over the historical window of length `self.length`.

        :param downloader: The module used to download additional data if needed.
        :type downloader: DownloadModule
        :param df: The DataFrame containing the price data, must include 'High' and 'Low' columns.
        :type df: pd.DataFrame
        :return: A tuple of two Series - the first indicating whether the condition is met (boolean),
                 and the second containing signal descriptions where the condition is met.
        :rtype: (pd.Series, pd.Series)
        """
        result = pd.Series([False] * len(df), index=df.index)
        uptrend = True  # Indicate we are looking for uptrend retracement levels
        counter = 0  # Counter to keep track of retracement occurrences

        # Iterate over the data frame to evaluate the condition for each row
        for index, (date, row) in enumerate(df.iterrows()):
            if index >= self.length:
                # Find the min and max indices in the historical window
                min_window_index = df[SourceType.LOW.value][index - self.length:index].argmin()
                max_window_index = df[SourceType.HIGH.value][index - self.length + min_window_index:index].argmax() + min_window_index

                # Ensure we're in an uptrend (min before max)
                if min_window_index < max_window_index:
                    counter += 1
                    low = df[SourceType.LOW.value].iloc[min_window_index]
                    high = df[SourceType.HIGH.value].iloc[max_window_index]

                    # Check if the current row is within the Fibonacci retracement level
                    if is_in_fib_interval(high, low, row, self.fib_level, uptrend):
                        result.iloc[index] = True

        # Create a signal series to describe where the condition is met
        signal_series = result.apply(
            lambda x: f'UptrendFibRetracementLevelSignal({self.fib_level.value}, {self.length})' if x else None
        )

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Return an empty list of graphs since no specific plots are generated for this condition.

        :param downloader: The module used to download additional data if needed.
        :type downloader: DownloadModule
        :param df: The DataFrame containing the price data.
        :type df: pd.DataFrame
        :return: An empty list.
        :rtype: list[TradingPlot]
        """
        return []

    def to_string(self) -> str:
        """
        Return a string representation of the condition for display purposes.

        :return: A string describing the condition with its parameters.
        :rtype: str
        """
        return f'UptrendFibRetracementLevelCondition({self.fib_level.value}, {self.length})'

    def to_dict(self) -> dict:
        """
        Convert the condition to a dictionary representation.

        :return: A dictionary containing the Fibonacci level and length.
        :rtype: dict
        """
        return {
            'type': 'UptrendFibRetracementLevelCondition',
            'fib_level': self.fib_level.value,
            'length': self.length
        }
