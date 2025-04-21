import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.momentum.bbp import bbp


class BBP(TradingSeries):
    """
    Class representing the Bull and Bear Power (BBP) indicator for a given ticker symbol.

    This class calculates the BBP indicator for a specified ticker symbol by downloading the relevant
    market data and applying the BBP calculation. The results can then be accessed and used for trading strategies.
    """

    def __init__(self, ticker: str, length: int = 13):
        """
        Initialize the BBP indicator object.

        :param ticker: The ticker symbol for which the BBP indicator is to be calculated.
        :type ticker: str
        :param length: The smoothing period for the BBP calculation, default is 13.
        :type length: int, optional
        """
        super().__init__(ticker)
        self.length = length
        self.name = f'{self._ticker}_BBP_{self.length}' # Define the name for the BBP series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol for the BBP indicator.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the BBP data for the specified ticker.

        If the BBP data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the BBP indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the BBP values.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the BBP
            bbp_series = bbp(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                close=new_df[SourceType.CLOSE.value],
                length=self.length
            )

            # Add the BBP series to the DataFrame
            df[self.name] = bbp_series

        # Return the BBP series as pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the BBP indicator.

        :return: The name of the BBP indicator, formatted with the ticker and length.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the BBP series to a dictionary representation.

        :return: A dictionary representation of the BBP series.
        :rtype: dict
        """
        return {
            'type': 'BBP',
            'ticker': self._ticker,
            'length': self.length
        }