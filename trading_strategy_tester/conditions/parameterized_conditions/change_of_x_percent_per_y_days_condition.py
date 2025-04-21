import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.change_of_x_percent_per_y_days_plot import ChangeOfXPercentPerYDaysPlot
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class ChangeOfXPercentPerYDaysCondition(Condition):

    def __init__(self, series: TradingSeries, percent: float, number_of_days: int):
        """
        Initialize the ChangeOfXPercentPerYDaysCondition with a series, percentage change, and number of days.

        :param series: The TradingSeries object containing the data to evaluate.
        :type series: TradingSeries
        :param percent: The percentage change to check against.
        :type percent: float
        :param number_of_days: The number of days over which to calculate the change.
        :type number_of_days: int
        """
        self.series = series
        self.percent = percent
        self.number_of_days = number_of_days

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the condition to determine where the percentage change in the series meets the specified criteria.

        :param downloader: The DownloadModule used to fetch the required data.
        :type downloader: DownloadModule
        :param df: The DataFrame containing the data.
        :type df: pd.DataFrame
        :return: A tuple of two pandas Series. The first Series indicates where the condition is met (True/False).
                 The second Series contains descriptive signals where the condition is met.
        :rtype: (pd.Series, pd.Series)
        """
        series: pd.Series = self.series.get_data(downloader, df)
        result = pd.Series([False] * len(df), index=df.index)

        for i in range(len(series)):
            if i >= self.number_of_days:
                # Calculate the percentage change compared to the value from 'number_of_days' ago
                current_percent = (100 * series.iloc[i]) / series.iloc[i - self.number_of_days] - 100 if series.iloc[i - self.number_of_days] != 0 else 0
                # Check if the percentage change meets the criteria
                if 0 < self.percent <= current_percent:
                    result.iloc[i] = True
                elif 0 > self.percent >= current_percent:
                    result.iloc[i] = True

        result.name = None

        # Generate signals for the series where the condition is met
        signal_series = result.apply(
            lambda x: f'ChangeOfXPercentPerYDaysSignal({self.percent}, {self.number_of_days}, {self.series.get_name()})' if x else None
        )

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Generate the plot for the condition showing where the percentage change meets the criteria.

        :param downloader: The DownloadModule used to fetch the required data.
        :type downloader: DownloadModule
        :param df: The DataFrame containing the data.
        :type df: pd.DataFrame
        :return: A list containing the ChangeOfXPercentPerYDaysPlot for visualizing the condition.
        :rtype: [TradingPlot]
        """
        return [ChangeOfXPercentPerYDaysPlot(
            self.series.get_data(downloader, df),
            self.percent,
            self.number_of_days,
        )]

    def to_string(self) -> str:
        """
        Provide a string representation of the condition, including the percentage change, number of days, and series name.

        :return: A string representation of the condition.
        :rtype: str
        """
        return f'ChangeOfXPercentPerYDaysCondition({self.percent}, {self.number_of_days}, {self.series.get_name()})'

    def to_dict(self) -> dict:
        """
        Convert the condition to a dictionary representation.

        :return: A dictionary containing the condition parameters.
        :rtype: dict
        """
        return {
            'type': 'ChangeOfXPercentPerYDaysCondition',
            'series': self.series.to_dict(),
            'percent': self.percent,
            'number_of_days': self.number_of_days
        }