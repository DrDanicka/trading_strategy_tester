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
        self.name = f'{self._ticker}_SMA_{self.target}_{self.length}_{self.offset}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name in df.columns:
            return pd.Series(df[self.name], name=self.name)
        else:
            new_df = downloader.download_ticker(self._ticker)
            sma_series = sma(series=new_df[self.target], length=self.length, offset=self.offset)

            # Adding indicators to global DataFrame
            df[self.name] = sma_series

            return sma_series