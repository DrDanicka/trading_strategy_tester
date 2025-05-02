import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class AND(Condition):
    """
    A condition that combines multiple conditions with a logical AND operation.

    This class takes multiple conditions as input and evaluates them simultaneously, returning
    True only when all the conditions are True for the given data points. It also combines
    the signal series from the individual conditions.
    """

    def __init__(self, *conditions: Condition):
        """
        Initialize the AndCondition with one or more conditions to be combined.

        :param conditions: A list of conditions to be evaluated with an AND logic.
        :type conditions: Condition
        """
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the AND combination of the provided conditions.

        This method evaluates each condition on the given data and combines their boolean results
        using the logical AND operation. It also concatenates the signal strings from each condition.

        :param downloader: Module to download necessary data for evaluation.
        :type downloader: DownloadModule
        :param df: The data frame containing the data on which the conditions are evaluated.
        :type df: pd.DataFrame
        :return: A tuple of two Pandas Series:
            - result: A boolean series where True indicates all conditions are met.
            - signal_series: A series of concatenated signals from the conditions.
        :rtype: (pd.Series, pd.Series)
        """
        result = pd.Series([True] * len(df), index=df.index)
        signal_series = pd.Series([''] * len(df), index=df.index)

        # Evaluate each condition and combine results
        for i, condition in enumerate(self.conditions):
            cond_result, signal_result = condition.evaluate(downloader, df)
            result &= cond_result  # Logical AND operation on results
            signal_series += signal_result.astype(str)  # Concatenate signal strings

            if i != len(self.conditions) - 1:
                # Add a separator between signals for all but the last condition
                signal_series += pd.Series([', '] * len(df), index=df.index)

        # If the combined result is False, replace signal with None
        signal_series = signal_series.where(result, None)
        # Wrap the signal in 'And()' to indicate AND logic
        signal_series = signal_series.apply(lambda x: f'And({x})' if x is not None else None)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Get the graphs representing the AND combination of the conditions.

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
        Return a string representation of the AndCondition.

        This provides a textual description of the condition, including the string
        representations of the individual conditions combined with AND logic.

        :return: A string representing the AND combination of conditions.
        :rtype: str
        """
        signals = []
        for condition in self.conditions:
            signals.append(condition.to_string())

        return f"AndCondition({', '.join(signals)})"

    def to_dict(self) -> dict:
        """
        Convert the AndCondition to a dictionary representation.

        This method provides a way to serialize the condition for storage or transmission.

        :return: A dictionary containing the type and parameters of the condition.
        :rtype: dict
        """
        return {
            'type': 'AND',
            'conditions': [condition.to_dict() for condition in self.conditions]
        }