import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule
from ..trading_plot.price_plot import PricePlot
from ..trading_plot.trading_plot import TradingPlot


class TradeConditions:
    def __init__(self, buy_condition: Condition, sell_condition: Condition, downloader: DownloadModule):
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.downloader = downloader


    def evaluate_conditions(self, df: pd.DataFrame) -> pd.DataFrame:
        buy, buy_signal_series = self.buy_condition.evaluate(self.downloader, df)
        df['BUY'] = buy
        df['BUY_Signals'] = buy_signal_series

        sell, sell_signal_series = self.sell_condition.evaluate(self.downloader, df)
        df['SELL'] = sell
        df['SELL_Signals'] = sell_signal_series

        return df

    def get_graphs(self, df: pd.DataFrame) -> dict[str, [TradingPlot]]:
        graphs = dict()

        graphs['BUY'] = self.buy_condition.get_graphs(self.downloader, df)
        graphs['SELL'] = self.sell_condition.get_graphs(self.downloader, df)

        graphs['PRICE'] = PricePlot(df)

        return graphs