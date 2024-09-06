import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.dpo import dpo


class DPO(TradingSeries):
    def __init__(self, ticker: str, length = 14):

        super().__init__(ticker)
        self.length = length
        self.name = f'{self._ticker}_DPO_{self.length}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name not in df.columns:
            new_df = downloader.download_ticker(self._ticker)
            dpo_series = dpo(series=new_df[SourceType.CLOSE.value], length=self.length)

            df[self.name] = dpo_series

        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        return self.name