import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volume.efi import efi
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class EFI(TradingSeries):
    """
    Class representing the Elder Force Index (EFI) indicator for a given ticker symbol.

    This class calculates the EFI indicator for a specified ticker symbol by downloading
    the relevant market data and applying the EFI calculation. The results can then be accessed
    and used for trading strategies.
    """

    def __init__(self, ticker: str, length: int = 13):
        """
        Initialize the EFI indicator object.

        :param ticker: The ticker symbol for which the EFI indicator is to be calculated.
        :type ticker: str
        :param length: The smoothing period for the EFI calculation, default is 13.
        :type length: int, optional
        """
        super().__init__(ticker)
        self.length = length
        self.name = f'{self._ticker}_EFI_{self.length}' # Define the name for the EFI series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol for the EFI indicator.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the EFI data for the specified ticker.

        If the EFI data is not already present in the provided DataFrame, this method downloads
        the latest market data for the ticker, calculates the EFI indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the EFI values.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the EFI indicator using the downloaded data
            efi_series = efi(
                close=new_df[SourceType.CLOSE.value],
                volume=new_df[SourceType.VOLUME.value],
                length=self.length
            )

            # Add the EFI series to the DataFrame
            df[self.name] = efi_series

        # Return the EFI series as a Pandas Series with an appropriate name
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the EFI indicator.

        :return: The name of the EFI indicator, formatted with the ticker and length.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the EFI series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'EFI',
            'ticker': self._ticker,
            'length': self.length
        }