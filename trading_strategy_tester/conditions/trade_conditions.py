import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule
from ..trading_plot.trading_plot import TradingPlot


class TradeConditions:
    def __init__(self, buy_condition: Condition, sell_condition: Condition, downloader: DownloadModule):
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.downloader = downloader

    def evaluate_conditions(self, df: pd.DataFrame) -> pd.DataFrame:
        df['BUY'] = self.buy_condition.evaluate(self.downloader, df)
        df['SELL'] = self.sell_condition.evaluate(self.downloader, df)
        return df

    def get_graphs(self, df: pd.DataFrame) -> dict[str, [TradingPlot]]:
        graphs = {}

        graphs['BUY'] = self.buy_condition.get_graphs(self.downloader, df)
        graphs['SELL'] = self.sell_condition.get_graphs(self.downloader, df)

        return graphs