import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.aroon import aroon_down


class AroonDown(TradingSeries):
    def __init__(self, ticker: str, target: str = 'Low', length: int = 14):
        super().__init__(ticker)
        self.target = target
        self.length = length

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule) -> pd.Series:
        df = downloader.download_ticker(self._ticker)

        aroon_down_series = aroon_down(df[self.target], self.length)
        aroon_down_series.name = f'{self._ticker}_{aroon_down_series.name}'

        return aroon_down_series