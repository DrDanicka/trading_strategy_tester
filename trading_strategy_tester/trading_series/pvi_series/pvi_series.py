import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volume.pvi import pvi


class PVI(TradingSeries):
    """
    A class for calculating and managing the Positive Volume Index (PVI) for a given ticker symbol.
    The PVI tracks cumulative price changes on days when volume increases, potentially highlighting
    the actions of "uninformed" investors.
    """

    def __init__(self, ticker: str):
        """
        Initialize the PVI class with the specified ticker symbol.

        :param ticker: The ticker symbol of the asset for which the PVI will be calculated.
        :type ticker: str
        """
        super().__init__(ticker)
        # Define the name of the PVI series with the ticker for easy identification
        self.name = f'{self._ticker}_PVI'

    @property
    def ticker(self) -> str:
        """
        Retrieve the ticker symbol associated with this PVI instance.

        :return: The ticker symbol for this PVI instance.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Generate the PVI data series for the specified ticker. If the series does not
        exist in the provided DataFrame, download the price and volume data, and calculate the PVI.

        :param downloader: The download module to fetch the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame where the PVI series will be added if absent.
        :type df: pd.DataFrame
        :return: A pandas Series containing the calculated PVI values, indexed by date.
        :rtype: pd.Series
        """
        # Check if PVI series is already in the DataFrame; if not, calculate and add it
        if self.name not in df.columns:
            # Download the historical price and volume data for the given ticker
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the PVI series using the close price and volume data
            pvi_series = pvi(
                close=new_df[SourceType.CLOSE.value],
                volume=new_df[SourceType.VOLUME.value]
            )

            # Add the calculated PVI series to the DataFrame
            df[self.name] = pvi_series

        # Return the PVI series as a pandas Series with appropriate naming
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Retrieve the name of the PVI series, including ticker details.

        :return: A string representing the PVI series name for this instance.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the PVI signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'PVI',
            'ticker': self._ticker
        }