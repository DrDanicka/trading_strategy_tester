import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule
from ..trading_plot.trading_plot import TradingPlot


class TradeConditions:
    def __init__(self, buy_condition: Condition, sell_condition: Condition, downloader: DownloadModule):
        self.buy_condition = buy_condition
        self.sell_condition = sell_condition
        self.downloader = downloader

    def clean_BUY_SELL_columns(self, df: pd.DataFrame):
        bought = False

        for index, row in df.iterrows():
            # If there is only True value to BUY
            if not bought and row['BUY'] and not row['SELL']:
                bought = True
            # If there is True value to SELL
            elif bought and row['SELL']:
                bought = False
                df.at[index, 'BUY'] = False
            else:
                df.at[index, 'BUY'] = False
                df.at[index, 'SELL'] = False

        if bought:
            if not df.loc[df.index[-1], 'BUY']:
                df.loc[df.index[-1], 'SELL'] = True
            else:
                # Set  last index of BUY to False
                df.loc[df.index[-1], 'BUY'] = False


    def evaluate_conditions(self, df: pd.DataFrame) -> pd.DataFrame:
        df['BUY'] = self.buy_condition.evaluate(self.downloader, df)
        df['SELL'] = self.sell_condition.evaluate(self.downloader, df)

        return df

    def get_graphs(self, df: pd.DataFrame) -> dict[str, [TradingPlot]]:
        graphs = {}

        graphs['BUY'] = self.buy_condition.get_graphs(self.downloader, df)
        graphs['SELL'] = self.sell_condition.get_graphs(self.downloader, df)

        return graphs