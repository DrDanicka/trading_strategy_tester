import pandas as pd
from abc import ABC, abstractmethod
from trading_strategy_tester.download.download_module import DownloadModule


class Condition(ABC):
    @abstractmethod
    def evaluate(self, downloader: DownloadModule) -> pd.Series:
        pass