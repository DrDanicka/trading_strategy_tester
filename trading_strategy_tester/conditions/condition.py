import pandas as pd
from abc import ABC, abstractmethod
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class Condition(ABC):
    """
    Abstract base class representing a trading condition.

    A trading condition encapsulates logic for evaluating specific market conditions
    based on provided data and generating visualizations (graphs) to represent the condition.

    Classes that inherit from `Condition` must implement the following abstract methods:
    - `evaluate`
    - `get_graphs`
    - `to_string`
    """

    @abstractmethod
    def evaluate(self, downloader: DownloadModule, df: pd.DataFrame) -> (pd.Series, pd.Series):
        """
        Evaluate the condition based on the downloaded data and the dataframe provided.

        This method should return two pandas Series objects that represent the results of the condition evaluation.
        The exact purpose and content of these Series objects will depend on the specific condition being implemented.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: The dataframe containing relevant market data (e.g., price, volume, indicators).
        :type df: pd.DataFrame
        :return: Two pandas Series representing the condition's evaluation result.
        :rtype: (pd.Series, pd.Series)
        """
        pass

    @abstractmethod
    def get_graphs(self, downloader: DownloadModule, df: pd.DataFrame) -> [TradingPlot]:
        """
        Generate visualizations (trading plots) based on the evaluated condition.

        This method should return a list of `TradingPlot` objects, each of which contains a plot that visualizes
        some aspect of the condition.

        :param downloader: The module responsible for downloading and providing market data.
        :type downloader: DownloadModule
        :param df: The dataframe containing relevant market data.
        :type df: pd.DataFrame
        :return: A list of `TradingPlot` objects representing visualizations of the condition.
        :rtype: [TradingPlot]
        """
        pass

    @abstractmethod
    def to_string(self) -> str:
        """
        Return a string representation of the condition.

        This method should generate a human-readable description of the condition,
        which can be useful for logging, debugging, or providing insights to users.

        :return: A string describing the condition.
        :rtype: str
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Convert the condition to a dictionary representation.

        This method should return a dictionary that captures the essential parameters
        and settings of the condition, which can be useful for serialization or configuration.

        :return: A dictionary representing the condition.
        :rtype: dict
        """
        pass