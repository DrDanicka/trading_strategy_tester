import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.sma import sma


class SMA(TradingSeries):
    def __init__(self, ticker: str, target: str = 'Close', length: int = 9, offset: int = 0):
        super().__init__(ticker)
        self.target = target
        self.length = length
        self.offset = offset

    @property
    def ticker(self):
        return self._ticker

    def get_data(self, downloader: DownloadModule) -> pd.Series:
        df = downloader.download_ticker(self._ticker)

        return sma(series=df[self.target], length=self.length, offset=self.offset)