import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volatility.kc import kc


class KC_LOWER(TradingSeries):
    """
    Represents the lower band of the Keltner Channel (KC) indicator.

    :param ticker: The symbol for the financial asset (e.g., stock or crypto ticker).
    :type ticker: str
    :param source: The source price type (e.g., Close, Open). Default is Close price.
    :type source: SourceType
    :param length: The lookback period for the moving average. Default is 20.
    :type length: int
    :param multiplier: The multiplier applied to the Average True Range (ATR) for adjusting channel width. Default is 2.
    :type multiplier: int
    :param use_exp_ma: If True, use the Exponential Moving Average (EMA); if False, use the Simple Moving Average (SMA). Default is True.
    :type use_exp_ma: bool
    :param atr_length: The lookback period for the ATR calculation. Default is 10.
    :type atr_length: int
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 20, multiplier: int = 2,
                 use_exp_ma: bool = True, atr_length: int = 10):
        super().__init__(ticker)
        self.source = source.value
        self.length = length
        self.multiplier = multiplier
        self.use_exp_ma = use_exp_ma
        self.atr_length = atr_length
        self.name = f'{self._ticker}_KC-LOWER_{self.source}_{self.length}_{self.multiplier}_{self.use_exp_ma}_{self.atr_length}'

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol for the financial asset.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves the Keltner Channel lower band data for the given ticker.

        If the KC lower band data is not already in the DataFrame, it downloads the ticker data and computes
        the KC lower band.

        :param downloader: The module responsible for downloading price data.
        :type downloader: DownloadModule
        :param df: A DataFrame containing the current market data, with columns for High, Low, Close, etc.
        :type df: pd.DataFrame
        :return: A Series representing the KC lower band.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download new data for the specified ticker
            new_df = downloader.download_ticker(self._ticker)

            # Compute the lower band of the Keltner Channel
            kc_upper_series = kc(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                close=new_df[SourceType.CLOSE.value],
                series=new_df[self.source],
                upper=False,  # Specifies the lower band
                length=self.length,
                multiplier=self.multiplier,
                use_exp_ma=self.use_exp_ma,
                atr_length=self.atr_length
            )

            # Add the KC lower band to the DataFrame
            df[self.name] = kc_upper_series

        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the KC lower band indicator.

        :return: The name of the KC lower band indicator.
        :rtype: str
        """
        return self.name