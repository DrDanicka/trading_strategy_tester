import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.candlestick_patterns.hammer import hammer
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class HAMMER(TradingSeries):
    """
    Class representing the Hammer candlestick pattern indicator for a given ticker symbol.

    This class calculates the Hammer candlestick pattern for a specified ticker symbol by downloading
    the relevant market data and applying the Hammer pattern detection. The results can be accessed
    and used for trading strategies.
    """

    def __init__(self, ticker: str):
        """
        Initialize the HAMMER indicator object.

        :param ticker: The ticker symbol for which the Hammer pattern is to be detected.
        :type ticker: str
        """
        super().__init__(ticker)
        self.name = f'{self._ticker}_HAMMER'  # Define the name for the Hammer pattern series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol for the HAMMER indicator.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Hammer pattern data for the specified ticker.

        If the Hammer pattern data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the Hammer pattern, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the Hammer pattern values.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the Hammer pattern detection based on OHLC data
            hammer_series = hammer(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                open=new_df[SourceType.OPEN.value],
                close=new_df[SourceType.CLOSE.value]
            )

            # Add the Hammer pattern series to the DataFrame
            df[self.name] = hammer_series

        # Return the Hammer pattern series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the HAMMER indicator.

        :return: The name of the HAMMER indicator, formatted with the ticker.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the HAMMER series to a dictionary representation.

        :return: A dictionary representation of the HAMMER series.
        :rtype: dict
        """
        return {
            'type': 'HAMMER',
            'ticker': self._ticker
        }