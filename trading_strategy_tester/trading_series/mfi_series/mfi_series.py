import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.sources import get_source_series
from trading_strategy_tester.indicators.volume.mfi import mfi


class MFI(TradingSeries):
    """
    A class for calculating and managing the Money Flow Index (MFI) for a given ticker symbol.
    The MFI is a momentum indicator that uses both price and volume to identify overbought or
    oversold conditions, assisting in detecting potential trend reversals.
    """

    def __init__(self, ticker: str, length: int = 14):
        """
        Initialize the MFI class with the specified ticker and calculation length.

        :param ticker: The ticker symbol of the asset for which the MFI will be calculated.
        :type ticker: str
        :param length: The period length used for the MFI calculation. Default is 14.
        :type length: int, optional
        """
        super().__init__(ticker)
        self.length = length
        # Define the name of the MFI series with the ticker and parameters for easy identification
        self.name = f'{ticker}_MFI_{length}'

    @property
    def ticker(self) -> str:
        """
        Retrieve the ticker symbol associated with this MFI instance.

        :return: The ticker symbol for this MFI instance.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Generate the MFI data series for the specified ticker. If the series does not
        exist in the provided DataFrame, download the price data and calculate the MFI.

        :param downloader: The download module to fetch the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame where the MFI series will be added if absent.
        :type df: pd.DataFrame
        :return: A pandas Series containing the calculated MFI values, indexed by date.
        :rtype: pd.Series
        """
        # Check if MFI series is already in the DataFrame; if not, calculate and add it
        if self.name not in df.columns:
            # Download the historical price data for the given ticker
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the MFI series using the typical price (HLC3) and volume data
            mfi_series = mfi(
                hlc3=get_source_series(new_df, SourceType.HLC3),
                volume=new_df[SourceType.VOLUME.value],
                length=self.length
            )

            # Add the calculated MFI series to the DataFrame
            df[self.name] = mfi_series

        # Return the MFI series as a pandas Series with appropriate naming
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Retrieve the name of the MFI series, including ticker and parameter details.

        :return: A string representing the MFI series name for this instance.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the MFI signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'MFI',
            'ticker': self._ticker,
            'length': self.length
        }