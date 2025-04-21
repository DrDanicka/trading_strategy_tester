import pandas as pd

from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot
from trading_strategy_tester.trading_plot.uptrend_plot import UptrendPlot
from trading_strategy_tester.trading_series.trading_series import TradingSeries

class UptrendForXDaysCondition(Condition):
    def __init__(self, series: TradingSeries, number_of_days: int):
        """
        Initialize the UptrendForXDaysCondition with the given series and number of days.

        :param series: The TradingSeries object containing the data series to evaluate.
        :type series: TradingSeries
        :param number_of_days: The number of days over which the uptrend should be evaluated.
        :type number_of_days: int
        """
        self.series = series
        self.number_of_days = number_of_days

    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the condition over the given dataframe and return the result series and signal series.

        The condition checks whether the series has been in an uptrend for the specified number of days.

        :param downloader: The DownloadModule used to fetch the data.
        :type downloader: DownloadModule
        :param df: The dataframe containing the data to evaluate.
        :type df: pd.DataFrame
        :return: A tuple containing:
            - is_uptrend: A pandas Series where True indicates that the series has been in an uptrend for the specified number of days.
            - signal_series: A pandas Series with descriptive strings where the condition is True, otherwise None.
        :rtype: tuple(pd.Series, pd.Series)
        """
        series: pd.Series = self.series.get_data(downloader, df)

        # Apply rolling window to check for uptrend
        is_uptrend = series.rolling(window=self.number_of_days).apply(
            lambda x: (x.diff().fillna(0) >= 0).all(), raw=False
        )
        is_uptrend = is_uptrend.fillna(0).astype(bool)
        is_uptrend.name = None

        # Generate signal series with descriptive strings
        signal_series = is_uptrend.apply(
            lambda x: f'UptrendForXDaysSignal({self.number_of_days}, {self.series.get_name()})' if x else None
        )

        return is_uptrend, signal_series

    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Generate the plot for the condition.

        :param downloader: The DownloadModule used to fetch the data.
        :type downloader: DownloadModule
        :param df: The dataframe containing the data to plot.
        :type df: pd.DataFrame
        :return: A list containing the UptrendPlot.
        :rtype: [TradingPlot]
        """
        return [UptrendPlot(
            self.series.get_data(downloader, df),
            self.number_of_days
        )]

    def to_string(self) -> str:
        """
        Provide a string representation of the condition for debugging or logging.

        :return: A string representation of the UptrendForXDaysCondition.
        :rtype: str
        """
        return f'UptrendForXDaysCondition({self.number_of_days}, {self.series.get_name()})'

    def to_dict(self) -> dict:
        """
        Convert the condition to a dictionary representation.

        :return: A dictionary containing the condition parameters.
        :rtype: dict
        """
        return {
            'type': 'UptrendForXDaysCondition',
            'series': self.series.to_dict(),
            'number_of_days': self.number_of_days,
        }