import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.adx import adx


class ADX(TradingSeries):
    def __init__(self, ticker:str, adx_smoothing: int = 14, DI_length: int = 14):
        super().__init__(ticker)
        self.adx_smoothing = adx_smoothing
        self.DI_length = DI_length

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule) -> pd.Series:
        df = downloader.download_ticker(self._ticker)

        adx_series = adx(high=df['High'], low=df['Low'], close=df['Close'], adx_smoothing=self.adx_smoothing,
                         DI_length=self.DI_length)
        adx_series.name = f'{self._ticker}_{adx_series.name}'

        return adx_series