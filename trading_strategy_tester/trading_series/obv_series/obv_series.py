import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volume.obv import obv


class OBV(TradingSeries):
    """
    Class representing the On-Balance Volume (OBV) indicator for a given ticker symbol.

    This class calculates the OBV for a specified ticker symbol by downloading the relevant market data
    and applying the OBV calculation. The results can then be accessed and used for trading strategies.
    """

    def __init__(self, ticker: str):
        """
        Initialize the OBV indicator object.

        :param ticker: The ticker symbol for which the OBV indicator is to be calculated.
        :type ticker: str
        """
        super().__init__(ticker)
        self.name = f'{self._ticker}_OBV'  # Define the name for the OBV series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol for the OBV indicator.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the OBV data for the specified ticker.

        If the OBV data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the OBV indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the OBV values.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the OBV indicator using the closing price and volume data
            obv_series = obv(
                close=new_df[SourceType.CLOSE.value],
                volume=new_df[SourceType.VOLUME.value]
            )

            # Add the OBV series to the DataFrame
            df[self.name] = obv_series

        # Return the OBV series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the OBV indicator.

        :return: The name of the OBV indicator, formatted with the ticker.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the OBV signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'OBV',
            'ticker': self._ticker
        }