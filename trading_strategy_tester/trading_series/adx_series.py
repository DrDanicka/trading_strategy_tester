import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.adx import adx


class ADX(TradingSeries):
    def __init__(self, ticker:str, adx_smoothing: int = 14, DI_length: int = 14):
        super().__init__(ticker)
        self.adx_smoothing = adx_smoothing
        self.DI_length = DI_length
        self.name = f'{self._ticker}_ADX_{self.adx_smoothing}_{self.DI_length}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name not in df.columns:
            new_df = downloader.download_ticker(self._ticker)
            adx_series = adx(high=new_df['High'], low=new_df['Low'], close=new_df['Close'],
                             adx_smoothing=self.adx_smoothing, DI_length=self.DI_length)

            # Adding indicator to global DataFrame
            df[self.name] = adx_series

        return pd.Series(df[self.name], name=self.name)