import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.momentum import momentum
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.sources import get_source_series


class MOMENTUM(TradingSeries):
    """
    A class for calculating and managing the Momentum indicator for a given ticker symbol.
    The Momentum indicator measures the rate of price change over a specified period,
    helping to identify trend strength and potential reversals.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 10):
        """
        Initialize the MOMENTUM class with the specified ticker, data source, and calculation length.

        :param ticker: The ticker symbol of the asset for which the Momentum will be calculated.
        :type ticker: str
        :param source: The source data type used in the Momentum calculation (e.g., closing price).
        :type source: SourceType, optional
        :param length: The period length used for the Momentum calculation. Default is 10.
        :type length: int, optional
        """
        super().__init__(ticker)
        self.source = source
        self.length = length
        # Define the name of the Momentum series with the ticker, source, and length for easy identification
        self.name = f'{ticker}_MOMENTUM_{self.source.value}_{self.length}'

    @property
    def ticker(self) -> str:
        """
        Retrieve the ticker symbol associated with this Momentum instance.

        :return: The ticker symbol for this Momentum instance.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Generate the Momentum data series for the specified ticker. If the series does not
        exist in the provided DataFrame, download the price data and calculate the Momentum.

        :param downloader: The download module to fetch the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame where the Momentum series will be added if absent.
        :type df: pd.DataFrame
        :return: A pandas Series containing the calculated Momentum values, indexed by date.
        :rtype: pd.Series
        """
        # Check if the Momentum series is already in the DataFrame; if not, calculate and add it
        if self.name not in df.columns:
            # Download the historical price data for the given ticker
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the Momentum series using the specified data source and length
            momentum_series = momentum(
                series=get_source_series(new_df, source=self.source),
                length=self.length
            )

            # Add the calculated Momentum series to the DataFrame
            df[self.name] = momentum_series

        # Return the Momentum series as a pandas Series with appropriate naming
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Retrieve the name of the Momentum series, including ticker and parameter details.

        :return: A string representing the Momentum series name for this instance.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the MOMENTUM signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'MOMENTUM',
            'ticker': self._ticker,
            'source': self.source,
            'length': self.length
        }