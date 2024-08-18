import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.atr import atr

class ATR(TradingSeries):
    def __init__(self, ticker: str, length: int = 14, smoothing: SmoothingType = SmoothingType.RMA):
        super().__init__(ticker)
        self.length = length
        self.smoothing = smoothing

    @property
    def ticker(self) -> str:
        return self.ticker

    def get_data(self, downloader: DownloadModule) -> pd.Series:
        df = downloader.download_ticker(self._ticker)

        atr_series = atr(high=df['High'], low=df['Low'], close=df['Close'], length=self.length, smoothing=self.smoothing)
        atr_series.name = f'{self._ticker}_{atr_series.name}'

        return atr_series