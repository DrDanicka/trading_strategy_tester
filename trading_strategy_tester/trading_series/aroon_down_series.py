import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.aroon import aroon_down


class AroonDown(TradingSeries):
    def __init__(self, ticker: str, length: int = 14):
        super().__init__(ticker)
        self.length = length
        self.name = f'{self.ticker}_AROONDOWN_{self.length}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name in df.columns:
            return pd.Series(df[self.name], name=self.name)
        else:
            new_df = downloader.download_ticker(self._ticker)
            aroon_down_series = aroon_down(new_df['High'], self.length)

            # Adding indicators to global DataFrame
            df[self.name] = aroon_down_series

            return aroon_down_series