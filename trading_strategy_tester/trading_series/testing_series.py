import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class TestingSeries(TradingSeries):

    def __init__(self, ticker: str, series: pd.Series, test_parameter: int):
        super().__init__(ticker)
        self.series = series
        self.test_parameter = test_parameter
        self.name = f'{self._ticker}_TEST_{self.test_parameter}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        return pd.Series(self.series, name=self.name)

    def get_name(self) -> str:
        return self.name

    def to_dict(self) -> dict:
        return {}