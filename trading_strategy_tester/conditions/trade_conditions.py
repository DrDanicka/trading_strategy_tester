import pandas as pd
from trading_strategy_tester.conditions.condition import Condition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_plot.price_plot import PricePlot
from trading_strategy_tester.trading_plot.trading_plot import TradingPlot


class TradeConditions:
    def __init__(self, buy_condition: Condition, sell_condition: Condition, downloader: DownloadModule):
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.downloader = downloader


    def evaluate_conditions(self, df: pd.DataFrame) -> pd.DataFrame:
        buy, buy_signal_series = self.buy_condition.evaluate(self.downloader, df)
        # Shift by one because the execution of the trade happens on the next day after the signal
        buy = buy.astype('boolean')
        buy = buy.shift(1).fillna(False)
        df['BUY'] = buy

        buy_signal_series = buy_signal_series.shift(1)
        df['BUY_Signals'] = buy_signal_series

        sell, sell_signal_series = self.sell_condition.evaluate(self.downloader, df)
        # Shift by one because the execution of the trade happens on the next day after the signal
        sell = sell.astype('boolean')
        sell = sell.shift(1).fillna(False)
        df['SELL'] = sell

        sell_signal_series = sell_signal_series.shift(1)
        df['SELL_Signals'] = sell_signal_series

        return df

    def get_graphs(self, df: pd.DataFrame, trades: list) -> dict[str, [TradingPlot]]:
        graphs = dict()

        graphs['BUY'] = self.buy_condition.get_graphs(self.downloader, df)
        graphs['SELL'] = self.sell_condition.get_graphs(self.downloader, df)

        graphs['PRICE'] = PricePlot(df, trades)

        return graphs