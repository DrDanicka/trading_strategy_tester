import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class IfThenElse(Condition):
    """
    A conditional evaluation that acts like an "if-then-else" statement for trading conditions.

    This class evaluates one condition (`if_condition`) first. If the condition is true, the result
    is true; otherwise, it evaluates a second condition (`else_condition`). The result is based on
    either condition being true and also collects signal data from both conditions.
    """

    def __init__(self, if_condition: Condition, else_condition: Condition):
        """
        Initialize the IfThenElseCondition with an "if" condition and an "else" condition.

        :param if_condition: The condition to evaluate first.
        :type if_condition: Condition
        :param else_condition: The condition to evaluate if the first condition is False.
        :type else_condition: Condition
        """
        self.if_condition = if_condition
        self.else_condition = else_condition

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the IfThenElse logic for the provided conditions.

        This method evaluates the `if_condition` first. If it's true, the result will be true;
        otherwise, the `else_condition` is evaluated. The signals from both conditions are also
        combined into a final signal series.

        :param downloader: Module to download necessary data for evaluation.
        :type downloader: DownloadModule
        :param df: The data frame containing the data on which the conditions are evaluated.
        :type df: pd.DataFrame
        :return: A tuple of two Pandas Series:
            - result: A boolean series indicating if either the `if_condition` or `else_condition` is true.
            - signal_series: A series of signals from both the `if_condition` and `else_condition`.
        :rtype: (pd.Series, pd.Series)
        """
        result = pd.Series([True] * len(df), index=df.index)
        signal_series = pd.Series([None] * len(df), index=df.index)

        # Evaluate both the if-condition and else-condition
        if_cond_result, if_signal_result = self.if_condition.evaluate(downloader, df)
        else_cond_result, else_signal_result = self.else_condition.evaluate(downloader, df)

        # Result is True if the if-condition is True, otherwise it takes the result of the else-condition
        result = (result & if_cond_result) | else_cond_result

        # Combine signal series from both conditions
        signal_series = signal_series.combine_first(if_signal_result).combine_first(else_signal_result)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Retrieve the graphs representing both the `if_condition` and `else_condition`.

        This method returns all the plots from both the if-condition and else-condition.

        :param downloader: Module to download necessary data for plotting the graphs.
        :type downloader: DownloadModule
        :param df: The data frame containing the data for plotting.
        :type df: pd.DataFrame
        :return: A list of TradingPlot objects representing the two conditions.
        :rtype: list[TradingPlot]
        """
        graphs = []

        # Collect graphs from both conditions
        for condition in [self.if_condition, self.else_condition]:
            graphs += condition.get_graphs(downloader, df)

        return graphs

    def to_string(self) -> str:
        """
        Return a string representation of the IfThenElseCondition.

        This provides a textual description of the condition, including the string
        representations of the `if_condition` and the `else_condition`.

        :return: A string representing the IfThenElseCondition.
        :rtype: str
        """
        return f"IfThenElseCondition({self.if_condition.to_string()}, {self.else_condition.to_string()})"

    def to_dict(self) -> dict:
        """
        Convert the IfThenElseCondition to a dictionary representation.

        This method provides a way to serialize the condition into a dictionary format.

        :return: A dictionary containing the condition parameters.
        :rtype: dict
        """
        return {
            'type': 'IfThenElseCondition',
            'if_condition': self.if_condition.to_dict(),
            'else_condition': self.else_condition.to_dict()
        }