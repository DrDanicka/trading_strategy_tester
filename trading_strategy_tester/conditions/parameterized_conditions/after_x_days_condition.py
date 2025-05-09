import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class AfterXDaysCondition(Condition):
    """
    A condition that shifts the evaluation of another condition by a specified number of days.

    This class wraps around another condition and modifies its evaluation by shifting it forward
    in time by a given number of days. It is useful when you want to check if a condition holds
    true after a certain number of days.
    """

    def __init__(self, condition: Condition, number_of_days: int):
        """
        Initialize the AfterXDaysCondition with a base condition and a shift in days.

        :param condition: The underlying condition to be shifted.
        :type condition: Condition
        :param number_of_days: The number of days to shift the condition.
        :type number_of_days: int
        """
        self.condition = condition
        self.number_of_days = number_of_days

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the condition after shifting it by the specified number of days.

        This method first evaluates the base condition, then shifts the resulting boolean series
        and signal series by the given number of days.

        :param downloader: Module to download necessary data for evaluation.
        :type downloader: DownloadModule
        :param df: The data frame containing the data on which the condition is evaluated.
        :type df: pd.DataFrame
        :return: A tuple of two Pandas Series:
            - after_x_days: A boolean series indicating if the condition is met after the given number of days.
            - signal_series: A series of signals indicating where the condition was triggered.
        :rtype: (pd.Series, pd.Series)
        """
        after_x_days, signal_series = self.condition.evaluate(downloader, df)

        # Shift the after_x_days series by the given number of days, and fill any missing values with False
        after_x_days = after_x_days.shift(self.number_of_days).astype(bool)
        after_x_days[:self.number_of_days] = False  # Set the initial 'number_of_days' to False
        after_x_days.name = None

        # Shift the signal series by the given number of days and apply a custom signal label
        signal_series = pd.Series(signal_series.shift(self.number_of_days))
        signal_series.name = None
        signal_series = signal_series.apply(
            lambda x: f'AfterXDaysSignal({self.number_of_days}, {x})' if x is not None else None)

        return after_x_days, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Get the graphs representing the condition after being shifted by the specified number of days.

        This method shifts the graphs generated by the base condition and returns the updated graphs.

        :param downloader: Module to download necessary data for plotting the graphs.
        :type downloader: DownloadModule
        :param df: The data frame containing the data for plotting.
        :type df: pd.DataFrame
        :return: A list of TradingPlot objects representing the shifted condition.
        :rtype: list[TradingPlot]
        """
        graphs = self.condition.get_graphs(downloader, df)

        # Shift each graph by the specified number of days
        for graph in graphs:
            graph.shift(self.number_of_days)

        return graphs

    def to_string(self) -> str:
        """
        Return a string representation of the AfterXDaysCondition.

        This provides a textual description of the condition, including the number of days shifted
        and the underlying condition.

        :return: A string representing the condition.
        :rtype: str
        """
        return f'AfterXDaysCondition({self.number_of_days}, {self.condition.to_string()})'

    def to_dict(self) -> dict:
        """
        Convert the condition to a dictionary representation.

        This method provides a way to serialize the condition into a dictionary format.

        :return: A dictionary representation of the condition.
        :rtype: dict
        """
        return {
            'type': 'AfterXDaysCondition',
            'number_of_days': self.number_of_days,
            'condition': self.condition.to_dict()
        }