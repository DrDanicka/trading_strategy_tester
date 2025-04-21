import pandas as pd

from trading_strategy_tester.conditions.parameterized_conditions.change_of_x_percent_per_y_days_condition import ChangeOfXPercentPerYDaysCondition
from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.change_of_x_percent_per_y_days_plot import ChangeOfXPercentPerYDaysPlot
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries

class IntraIntervalChangeOfXPercentCondition(Condition):

    def __init__(self, series: TradingSeries, percent: float):
        """
        Initialize the IntraIntervalChangeOfXPercentCondition with the given series and percent.

        :param series: The TradingSeries object containing the data series to evaluate.
        :type series: TradingSeries
        :param percent: The percentage change threshold to use for condition evaluation.
        :type percent: float
        """
        self.series = series
        self.percent = percent
        # Initialize a ChangeOfXPercentPerYDaysCondition with a window of 1 day
        self.change_of_x_percent_on_y_days_condition = ChangeOfXPercentPerYDaysCondition(series, percent, 1)

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the condition over the given dataframe and return the result series and signal series.

        :param downloader: The DownloadModule used to fetch the data.
        :type downloader: DownloadModule
        :param df: The dataframe containing the data to evaluate.
        :type df: pd.DataFrame
        :return: A tuple containing the result series and signal series.
        :rtype: tuple(pd.Series, pd.Series)
        """
        result, _ = self.change_of_x_percent_on_y_days_condition.evaluate(downloader, df)

        # Create a signal series with a description of the condition
        signal_series = result.apply(
            lambda x: f'IntraIntervalChangeOfXPercentSignal({self.percent}, {self.series.get_name()})' if x else None
        )

        return result, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Generate the plots for the condition.

        :param downloader: The DownloadModule used to fetch the data.
        :type downloader: DownloadModule
        :param df: The dataframe containing the data to plot.
        :type df: pd.DataFrame
        :return: A list containing the ChangeOfXPercentPerYDaysPlot.
        :rtype: list[TradingPlot]
        """
        return [ChangeOfXPercentPerYDaysPlot(
            self.series.get_data(downloader, df),
            self.percent,
            1
        )]

    def to_string(self) -> str:
        """
        Provide a string representation of the condition for debugging or logging.

        :return: A string representation of the IntraIntervalChangeOfXPercentCondition.
        :rtype: str
        """
        return f'IntraIntervalChangeOfXPercentCondition({self.percent}, {self.series.get_name()})'

    def to_dict(self) -> dict:
        """
        Convert the condition to a dictionary representation.

        :return: A dictionary containing the condition parameters.
        :rtype: dict
        """
        return {
            'type': 'IntraIntervalChangeOfXPercentCondition',
            'series': self.series.to_dict(),
            'percent': self.percent,
        }
