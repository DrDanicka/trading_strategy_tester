import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.candlestick_patterns.hammer import hammer
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class HAMMER(TradingSeries):

    def __init__(self, ticker: str):
        super().__init__(ticker)
        self.name = f'{self._ticker}_HAMMER'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name not in df.columns:
            new_df = downloader.download_ticker(self._ticker)
            hammer_series = hammer(
                high=new_df[SourceType.HIGH],
                low=new_df[SourceType.LOW],
                open=new_df[SourceType.OPEN],
                close=new_df[SourceType.CLOSE]
            )

            df[self.name] = hammer_series

        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        return self.name