import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.trading_plot.less_than_plot import LessThanPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class LessThanCondition(Condition):
    """
    Represents a condition where the first trading series is less than the second series.

    This class evaluates when one series is less than another and provides visualizations for plotting.
    """

    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        """
        Initialize the LessThanCondition with two trading series.

        :param first_series: The first trading series used in the condition (e.g., price or indicator).
        :type first_series: TradingSeries
        :param second_series: The second trading series to compare against.
        :type second_series: TradingSeries
        """
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the less-than condition using the provided data.

        This method checks if the first series is less than the second series for each data point.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data (e.g., prices, indicators).
        :type df: pd.DataFrame
        :return: Two pandas Series: one indicating where series1 is less than series2 (boolean), and another
                 providing a signal description string where the condition is met.
        :rtype: (pd.Series, pd.Series)
        """
        # Retrieve data from both trading series
        series1 = self.first_series.get_data(downloader, df)
        series2 = self.second_series.get_data(downloader, df)

        # Detect where series1 is less than series2
        less_than = pd.Series(series1 < series2)

        # Create a signal string for detected points where series1 is less than series2
        signal_series = less_than.apply(
            lambda x: f'LessThanSignal({self.first_series.get_name()}, {self.second_series.get_name()})' if x else None)

        return less_than, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Generate trading plot graphs to visualize the less-than condition.

        This method returns a list of `TradingPlot` objects that visualize when the first series is less than the second.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data (e.g., prices, indicators).
        :type df: pd.DataFrame
        :return: A list of `TradingPlot` objects that visualize the less-than condition.
        :rtype: [TradingPlot]
        """
        return [LessThanPlot(
            self.first_series.get_data(downloader, df),
            self.second_series.get_data(downloader, df)
        )]

    def to_string(self) -> str:
        """
        Return a string representation of the less-than condition.

        The string representation includes the names of the two series involved in the comparison.

        :return: A string describing the less-than condition.
        :rtype: str
        """
        return f'LessThanCondition({self.first_series.get_name()}, {self.second_series.get_name()})'

    def to_dict(self) -> dict:
        """
        Convert the condition to a dictionary representation.

        :return: A dictionary containing the condition parameters.
        :rtype: dict
        """
        return {
            'type': 'LessThanCondition',
            'first_series': self.first_series.to_dict(),
            'second_series': self.second_series.to_dict(),
        }