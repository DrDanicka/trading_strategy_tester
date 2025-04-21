import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.sources import get_source_series
from trading_strategy_tester.indicators.momentum.macd import macd


class MACD(TradingSeries):
    """
    The MACD class calculates the Moving Average Convergence Divergence (MACD) for a specified ticker symbol.
    MACD is a technical indicator used to assess the momentum of an asset by examining the difference
    between two moving averages of its price.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, fast_length: int = 12, slow_length: int = 26,
                 ma_type: SmoothingType = SmoothingType.EMA):
        """
        Initialize the MACD class with the provided ticker, price source, moving average lengths, and type.

        :param ticker: The ticker symbol of the asset for which MACD will be calculated.
        :type ticker: str
        :param source: The source data type used in the MACD calculation (e.g., closing price).
        :type source: SourceType, optional
        :param fast_length: Length of the fast moving average for MACD. Default is 12.
        :type fast_length: int, optional
        :param slow_length: Length of the slow moving average for MACD. Default is 26.
        :type slow_length: int, optional
        :param ma_type: The type of moving average (e.g., EMA). Default is SmoothingType.EMA.
        :type ma_type: SmoothingType, optional
        """
        super().__init__(ticker)
        self.source = source
        self.fast_length = fast_length
        self.slow_length = slow_length
        self.ma_type = ma_type
        # Define the name of the MACD series with relevant parameters for easy identification
        self.name = f'{self._ticker}_MACD_{self.fast_length}_{self.slow_length}_{self.ma_type.value}'

    @property
    def ticker(self) -> str:
        """
        Retrieve the ticker symbol of the asset associated with this MACD instance.

        :return: The ticker symbol for the MACD instance.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Generate the MACD data series for the specified ticker. If the series does not exist
        in the provided DataFrame, download the price data and calculate MACD.

        :param downloader: The download module to fetch the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame where the MACD series will be added if absent.
        :type df: pd.DataFrame
        :return: A pandas Series containing the calculated MACD values, indexed by date.
        :rtype: pd.Series
        """
        # If MACD is not already in the DataFrame, calculate and add it
        if self.name not in df.columns:
            # Download the historical price data for the given ticker
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the MACD series using the specified parameters
            macd_series = macd(
                series=get_source_series(new_df, source=self.source),
                fast_length=self.fast_length,
                slow_length=self.slow_length,
                ma_type=self.ma_type
            )

            # Add the calculated MACD series to the DataFrame
            df[self.name] = macd_series

        # Return the MACD series as a pandas Series with appropriate naming
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Retrieve the name of the MACD series, including ticker and parameters.

        :return: The name of the MACD series for the given configuration.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the MACD series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'MACD',
            'ticker': self._ticker,
            'source': self.source,
            'fast_length': self.fast_length,
            'slow_length': self.slow_length,
            'ma_type': self.ma_type
        }