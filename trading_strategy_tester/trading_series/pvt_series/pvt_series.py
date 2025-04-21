import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volume.pvt import pvt


class PVT(TradingSeries):
    """
    A class to represent the Price-Volume Trend (PVT) indicator for a specific asset.

    This class extends the TradingSeries base class and calculates the PVT based on the
    asset's historical closing prices and trading volume. The calculated PVT is used to
    understand the directional strength of the asset by combining price movements and volume data.
    """

    def __init__(self, ticker: str):
        """
        Initialize the PVT class with the specified ticker symbol.

        :param ticker: The ticker symbol of the asset for which the PVT will be calculated.
        :type ticker: str
        """
        super().__init__(ticker)
        # Define the name of the PVT series with the ticker for easy identification
        self.name = f'{self._ticker}_PVT'

    @property
    def ticker(self) -> str:
        """
        Retrieve the ticker symbol associated with this PVT instance.

        :return: The ticker symbol for this PVT instance.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the PVT series for the specified ticker.

        This method checks if the PVT series already exists in the provided DataFrame.
        If not, it downloads the necessary historical data, calculates the PVT using the
        closing price and volume, and adds the result to the DataFrame.

        :param downloader: An instance of DownloadModule to fetch historical data.
        :type downloader: DownloadModule
        :param df: A pandas DataFrame containing historical data for the ticker.
        :type df: pd.DataFrame
        :return: A pandas Series representing the PVT values with the same index as the input DataFrame.
        :rtype: pd.Series
        """

        # Check if the PVT series is already in the DataFrame; if not, calculate and add it
        if self.name not in df.columns:
            # Download the historical price and volume data for the given ticker
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the PVT series using the close price and volume data
            pvi_series = pvt(
                close=new_df[SourceType.CLOSE.value],  # Access the closing prices
                volume=new_df[SourceType.VOLUME.value]  # Access the volume data
            )

            # Add the calculated PVT series to the DataFrame for persistent storage
            df[self.name] = pvi_series

        # Return the PVT series as a pandas Series with the appropriate name
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Retrieve the name of the PVT series, including ticker details.

        :return: A string representing the PVT series name for this instance.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the PVT signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'PVT',
            'ticker': self._ticker
        }