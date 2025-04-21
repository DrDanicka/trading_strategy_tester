import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_plot.cross_over_plot import CrossOverPlot


class CrossOverCondition(Condition):
    """
    Represents a crossover condition between two trading series.

    This class evaluates when one series crosses over another (i.e., when the first series crosses from below the second),
    and provides visualizations to plot the crossover points.
    """

    def __init__(self, first_series: TradingSeries, second_series: TradingSeries):
        """
        Initialize the CrossOverCondition with two trading series.

        :param first_series: The first trading series (e.g., price or indicator) used in the crossover condition.
        :type first_series: TradingSeries
        :param second_series: The second trading series to compare against.
        :type second_series: TradingSeries
        """
        self.first_series = first_series
        self.second_series = second_series

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the crossover condition using the provided data.

        This method checks if the first series crosses above the second series. A crossover is detected
        when the first series is below the second series on the previous day and above it on the current day.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data (e.g., prices, indicators).
        :type df: pd.DataFrame
        :return: Two pandas Series: one indicating whether a crossover has occurred (boolean), and another
                 providing a signal description string for crossover points.
        :rtype: (pd.Series, pd.Series)
        """
        # Retrieve data from both trading series
        series1: pd.Series = self.first_series.get_data(downloader, df)
        series2: pd.Series = self.second_series.get_data(downloader, df)

        # Detect crossovers: True if series1 crosses from below series2
        crossover = pd.Series((series1.shift(1) < series2.shift(1)) & (series1 > series2))
        crossover.fillna(False, inplace=True)

        # Create a signal string for detected crossover points
        signal_series = crossover.apply(
            lambda x: f'CrossOverSignal({self.first_series.get_name()}, {self.second_series.get_name()})' if x else None)

        return crossover, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Generate trading plot graphs to visualize the crossover condition.

        This method returns a list of `TradingPlot` objects that visualize the crossover between
        the first and second series.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing relevant market data (e.g., prices, indicators).
        :type df: pd.DataFrame
        :return: A list of `TradingPlot` objects that visualize the crossover condition.
        :rtype: [TradingPlot]
        """
        return [CrossOverPlot(
            self.first_series.get_data(downloader, df),
            self.second_series.get_data(downloader, df)
        )]

    def to_string(self) -> str:
        """
        Return a string representation of the crossover condition.

        The string representation includes the names of the two series involved in the crossover.

        :return: A string describing the crossover condition.
        :rtype: str
        """
        return f'CrossOverCondition({self.first_series.get_name()}, {self.second_series.get_name()})'

    def to_dict(self) -> dict:
        """
        Convert the crossover condition to a dictionary representation.

        This method provides a structured representation of the condition, including the names of the two series.

        :return: A dictionary containing the condition parameters.
        :rtype: dict
        """
        return {
            'type': 'CrossOverCondition',
            'first_series': self.first_series.to_dict(),
            'second_series': self.second_series.to_dict(),
        }