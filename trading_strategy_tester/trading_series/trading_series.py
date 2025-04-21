import pandas as pd
from abc import ABC, abstractmethod
from trading_strategy_tester.download.download_module import DownloadModule


class TradingSeries(ABC):
    """
    An abstract base class for creating trading data series.

    The TradingSeries class serves as a template for defining trading data series associated with a specific ticker.
    It enforces the implementation of methods for retrieving the ticker symbol and for obtaining data from a DataFrame.
    """

    def __init__(self, ticker: str):
        """
        Initializes the TradingSeries with the specified ticker symbol.

        :param ticker: The ticker symbol to retrieve data from.
        :type ticker: str
        """
        self._ticker = ticker  # Store the ticker symbol as a protected attribute

    @property
    @abstractmethod
    def ticker(self) -> str:
        """
        Abstract property to get the ticker symbol.

        Subclasses must implement this property to return the ticker symbol associated with the trading series.

        :return: The ticker symbol associated with the trading series.
        :rtype: str
        """
        pass

    @abstractmethod
    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Abstract method to obtain a data series from a DataFrame.

        The method could, for example, return a series of closing prices, volume data, or any other relevant data series.

        :param downloader: Download module to use.
        :type downloader: DownloadModule
        :param df: DataFrame containing the data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the data for the specified ticker.
        :rtype: pd.Series
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        Abstract method to get the name of the trading series.

        Subclasses must implement this method to return a string representing the name of the trading series.

        :return: The name of the trading series.
        :rtype: str
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Abstract method to convert the trading series to a dictionary representation.

        :return: A dictionary representation of the trading series.
        :rtype: dict
        """
        pass