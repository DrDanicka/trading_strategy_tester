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
        self.name = f'{self._ticker}_ATR_{self.length}_{self.smoothing.value}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name not in df.columns:
            new_df = downloader.download_ticker(self._ticker)
            atr_series = atr(high=new_df['High'], low=new_df['Low'], close=new_df['Close'],
                             length=self.length, smoothing=self.smoothing)

            # Adding indicator to global DataFrame
            df[self.name] = atr_series

        return pd.Series(df[self.name], name=self.name)