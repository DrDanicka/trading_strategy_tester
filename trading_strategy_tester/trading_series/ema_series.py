import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.ema import ema


class EMA(TradingSeries):
    def __init__(self, ticker: str, target: str = 'Close', length: int = 9, offset: int = 0):
        super().__init__(ticker)
        self.target = target
        self.length = length
        self.offset = offset
        self.name = f'{self._ticker}_EMA_{self.target}_{self.length}_{self.offset}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name not in df.columns:
            new_df = downloader.download_ticker(self._ticker)
            ema_series = ema(series=new_df[self.target], length=self.length, offset=self.offset)

            # Adding indicator to global DataFrame
            df[self.name] = ema_series

        return pd.Series(df[self.name], name=self.name)