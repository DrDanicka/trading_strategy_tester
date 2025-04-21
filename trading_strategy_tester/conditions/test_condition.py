import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class TestCondition(Condition):
    """
    A test condition used for development or debugging purposes.

    This condition simply returns the values of the given trading series as the evaluation result,
    without applying any actual trading logic. It is useful for verifying data flow and visualization
    integration within the trading strategy testing framework.
    """

    def __init__(self, series: TradingSeries):
        """
        Initialize the TestCondition with a single trading series.

        :param series: A trading series (e.g., price or indicator) used for testing.
        :type series: TradingSeries
        """
        self.series = series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the test condition using the provided trading series.

        This method fetches the series data and returns it directly as the evaluation result.
        A string signal is applied where the series value is truthy (non-zero, non-null).

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data.
        :type df: pd.DataFrame
        :return: A tuple containing the series data and a signal string where the data is truthy.
        :rtype: (pd.Series, pd.Series)
        """
        result = self.series.get_data(downloader, df)
        signal_series = result.apply(lambda x: self.to_string() if x else None)

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Return any trading plot visualizations for this condition.

        Since this is a test condition, no visual plots are returned.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data.
        :type df: pd.DataFrame
        :return: An empty list as no plots are associated with this test condition.
        :rtype: [TradingPlot]
        """
        return []

    def to_string(self) -> str:
        """
        Return a string representation of the test condition.

        :return: A string describing the test condition with the name of the series.
        :rtype: str
        """
        return f'TestCondition({self.series.get_name()})'

    def to_dict(self) -> dict:
        """
        Convert the TestCondition to a dictionary representation.

        :return: A dictionary containing the class name and series name.
        :rtype: dict
        """
        return {
            'type': 'TestCondition',
            'series_name': self.series.get_name()
        }
