import pandas as pd

from .condition import Condition
from ..download.download_module import DownloadModule


class TradeConditions:
    def __init__(self, buy_condition: Condition, sell_condition: Condition, downloader: DownloadModule):
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.downloader = downloader

    def evaluate_conditions(self, df: pd.DataFrame) -> pd.DataFrame:
        df['BUY'] = self.buy_condition.evaluate(self.downloader)
        df['SELL'] = self.sell_condition.evaluate(self.downloader)
        return df