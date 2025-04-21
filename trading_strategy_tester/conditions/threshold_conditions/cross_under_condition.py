import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_plot.cross_under_plot import CrossUnderPlot


class CrossUnderCondition(Condition):
    """
    Represents a cross-under condition between two trading series.

    This class evaluates when one series crosses under another (i.e., when the first series crosses from above the second),
    and provides visualizations to plot the cross-under points.
    """

    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        """
        Initialize the CrossUnderCondition with two trading series.

        :param first_series: The first trading series (e.g., price or indicator) used in the cross-under condition.
        :type first_series: TradingSeries
        :param second_series: The second trading series to compare against.
        :type second_series: TradingSeries
        """
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the cross-under condition using the provided data.

        This method checks if the first series crosses below the second series. A cross-under is detected
        when the first series is above the second series on the previous day and below it on the current day.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data (e.g., prices, indicators).
        :type df: pd.DataFrame
        :return: Two pandas Series: one indicating whether a cross-under has occurred (boolean), and another
                 providing a signal description string for cross-under points.
        :rtype: (pd.Series, pd.Series)
        """
        # Retrieve data from both trading series
        series1: pd.Series = self.first_series.get_data(downloader, df)
        series2: pd.Series = self.second_series.get_data(downloader, df)

        # Detect cross-unders: True if series1 crosses from above series2
        cross_under = pd.Series((series1.shift(1) > series2.shift(1)) & (series1 < series2))
        cross_under.fillna(False, inplace=True)

        # Create a signal string for detected cross-under points
        signal_series = cross_under.apply(
            lambda x: f'CrossUnderSignal({self.first_series.get_name()}, {self.second_series.get_name()})' if x else None)

        return cross_under, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Generate graphs to visualize the cross-under condition.

        This method creates a plot showing the two series and highlights the cross-under points.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data (e.g., prices, indicators).
        :type df: pd.DataFrame
        :return: A list of TradingPlot objects representing the cross-under plots.
        :rtype: [TradingPlot]
        """
        return [CrossUnderPlot(
            series1=self.first_series.get_data(downloader, df),
            series2=self.second_series.get_data(downloader, df)
        )]

    def to_string(self) -> str:
        """
        Return a string representation of the cross-under condition.

        The string representation includes the names of the two series involved in the cross-under condition.

        :return: A string representation of the cross-under condition.
        :rtype: str
        """
        return f"CrossUnderCondition({self.first_series.get_name()}, {self.second_series.get_name()})"

    def to_dict(self) -> dict:
        """
        Convert the cross-under condition to a dictionary representation.

        This method provides a structured representation of the condition, including the types and names of the series.

        :return: A dictionary representation of the cross-under condition.
        :rtype: dict
        """
        return {
            'type': 'CrossUnderCondition',
            'first_series': self.first_series.to_dict(),
            'second_series': self.second_series.to_dict(),
        }