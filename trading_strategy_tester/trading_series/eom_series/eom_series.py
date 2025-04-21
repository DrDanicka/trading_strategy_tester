import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volume.eom import eom


class EOM(TradingSeries):
    """
    Class representing the Ease of Movement (EOM) indicator for a given ticker symbol.

    This class calculates the EOM for a specified ticker symbol by downloading the relevant market data
    and applying the EOM calculation. The results can then be accessed and used for trading strategies.
    """

    def __init__(self, ticker: str, length: int = 14, divisor: int = 10_000):
        """
        Initialize the EOM indicator object.

        :param ticker: The ticker symbol for which the EOM indicator is to be calculated.
        :type ticker: str
        :param length: The smoothing period for the EOM calculation, default is 14.
        :type length: int, optional
        :param divisor: Divisor to scale the EOM values, default is 10,000.
        :type divisor: int, optional
        """
        super().__init__(ticker)
        self.length = length
        self.divisor = divisor
        self.name = f'{self._ticker}_EOM_{self.length}_{self.divisor}' # Define the name for the EOM series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol for the EOM indicator.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the EOM data for the specified ticker.

        If the EOM data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the EOM indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the EOM values.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the EOM using the specified target column and length
            eom_series = eom(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                volume=new_df[SourceType.VOLUME.value],
                length=self.length,
                divisor=self.divisor
            )

            # Add the EOM series to the DataFrame
            df[self.name] = eom_series

        # Return the EOM series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the EOM indicator.

        :return: The name of the EOM indicator, formatted with the ticker, length, and divisor.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the EOM series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'EOM',
            'ticker': self._ticker,
            'length': self.length,
            'divisor': self.divisor
        }