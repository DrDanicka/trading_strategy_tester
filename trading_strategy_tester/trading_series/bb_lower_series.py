import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.bb import bb_lower


class BBLower(TradingSeries):
    def __init__(self, ticker: str, target: str = 'Close', length: int = 20, ma_type: SmoothingType = SmoothingType.SMA,
                 std_dev: int = 2, offset: int = 0):
        super().__init__(ticker)
        self.target = target
        self.length = length
        self.ma_type = ma_type
        self.std_dev = std_dev
        self.offset = offset
        self.name = f'{self._ticker}_BBLOWER_{self.target}_{self.length}_{self.ma_type.value}_{self.std_dev}_{self.offset}'

    @property
    def ticker(self) -> str:
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        if self.name not in df.columns:
            new_df = downloader.download_ticker(self._ticker)
            bb_lower_series = bb_lower(
                series=new_df[self.target],
                length=self.length,
                ma_type=self.ma_type,
                std_dev=self.std_dev,
                offset=self.offset
            )

            # Adding indicator to global DataFrame
            df[self.name] = bb_lower_series

        return pd.Series(df[self.name], name=self.name)
