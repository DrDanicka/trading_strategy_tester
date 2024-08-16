import pandas as pd
from abc import ABC, abstractmethod
from trading_strategy_tester.download.download_module import DownloadModule


class TradingSeries(ABC):
    def __init__(self, ticker: str):
        self._ticker = ticker

    @property
    @abstractmethod
    def ticker(self) -> str:
        pass

    @abstractmethod
    def get_data(self, downloader: DownloadModule) -> pd.Series:
        pass