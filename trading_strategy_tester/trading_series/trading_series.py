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

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        """
        self._ticker = ticker  # Store the ticker symbol as a protected attribute

    @property
    @abstractmethod
    def ticker(self) -> str:
        """
        Abstract property to get the ticker symbol.

        Subclasses must implement this property to return the ticker symbol associated with the trading series.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        pass

    @abstractmethod
    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Abstract method to obtain a data series from a DataFrame.

        The method could, for example, return a series of closing prices, volume data, or any other relevant data series.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download or retrieve additional data if needed.

        df : pd.DataFrame
            A DataFrame containing the trading data from which the series will be extracted.

        Returns:
        --------
        pd.Series
            A pandas Series containing the specific trading data.
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass