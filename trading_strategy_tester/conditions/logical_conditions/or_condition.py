import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class OR(Condition):
    """
    A condition that combines multiple conditions with a logical OR operation.

    This class takes multiple conditions as input and evaluates them simultaneously, returning
    True when any of the conditions are True for the given data points. It also combines
    the signal series from the individual conditions.
    """

    def __init__(self, *conditions: Condition):
        """
        Initialize the OrCondition with one or more conditions to be combined.

        :param conditions: A list of conditions to be evaluated with an OR logic.
        :type conditions: Condition
        """
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the OR combination of the provided conditions.

        This method evaluates each condition on the given data and combines their boolean results
        using the logical OR operation. It also keeps the signals from the first condition where
        the result is True.

        :param downloader: Module to download necessary data for evaluation.
        :type downloader: DownloadModule
        :param df: The data frame containing the data on which the conditions are evaluated.
        :type df: pd.DataFrame
        :return: A tuple of two Pandas Series:
            - result: A boolean series where True indicates at least one condition is met.
            - signal_series: A series containing the first non-null signal from the conditions.
        :rtype: (pd.Series, pd.Series)
        """
        result = pd.Series([False] * len(df), index=df.index)
        signal_series = pd.Series([None] * len(df), index=df.index).astype(object)

        # Evaluate each condition and combine results
        for condition in self.conditions:
            cond_result, signal_result = condition.evaluate(downloader, df)
            result |= cond_result  # Logical OR operation on results
            # Keep the first non-null signal from previous conditions
            signal_series = signal_series.combine_first(signal_result)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Get the graphs representing the OR combination of the conditions.

        This method retrieves the graphs from each condition and combines them into a list.

        :param downloader: Module to download necessary data for plotting the graphs.
        :type downloader: DownloadModule
        :param df: The data frame containing the data for plotting.
        :type df: pd.DataFrame
        :return: A list of TradingPlot objects representing the conditions.
        :rtype: list[TradingPlot]
        """
        graphs = []

        # Collect all graphs from the conditions
        for condition in self.conditions:
            graphs += condition.get_graphs(downloader, df)

        return graphs

    def to_string(self) -> str:
        """
        Return a string representation of the OrCondition.

        This provides a textual description of the condition, including the string
        representations of the individual conditions combined with OR logic.

        :return: A string representing the OR combination of conditions.
        :rtype: str
        """
        signals = []
        for condition in self.conditions:
            signals.append(condition.to_string())

        return f"OrCondition({', '.join(signals)})"

    def to_dict(self) -> dict:
        """
        Convert the OR condition to a dictionary representation.

        This method provides a way to serialize the condition into a dictionary format,
        which can be useful for saving or transmitting the condition's configuration.

        :return: A dictionary representation of the OR condition.
        :rtype: dict
        """
        return {
            'type': 'OR',
            'conditions': [condition.to_dict() for condition in self.conditions]
        }