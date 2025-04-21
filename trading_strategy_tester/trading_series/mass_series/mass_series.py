import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.trend.mass import mass_index
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class MASS_INDEX(TradingSeries):
    """
    A class for calculating and managing the Mass Index indicator for a given ticker symbol.
    The Mass Index is a trend reversal indicator that highlights potential changes in trend
    based on price volatility, without indicating direction.
    """

    def __init__(self, ticker: str, length: int = 10):
        """
        Initialize the MASS_INDEX class with the specified ticker and calculation length.

        :param ticker: The ticker symbol of the asset for which the Mass Index will be calculated.
        :type ticker: str
        :param length: The period length used for the Mass Index calculation. Default is 10.
        :type length: int, optional
        """
        super().__init__(ticker)
        self.length = length
        # Define the name of the Mass Index series, including parameters for easy identification
        self.name = f'{self._ticker}_MASS-INDEX_{length}'

    def ticker(self) -> str:
        """
        Retrieve the ticker symbol associated with this Mass Index instance.

        :return: The ticker symbol for this Mass Index instance.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Generate the Mass Index data series for the specified ticker. If the series does not
        exist in the provided DataFrame, download the price data and calculate the Mass Index.

        :param downloader: The download module to fetch the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame where the Mass Index series will be added if absent.
        :type df: pd.DataFrame
        :return: A pandas Series containing the calculated Mass Index values, indexed by date.
        :rtype: pd.Series
        """
        # Check if Mass Index series is already in the DataFrame; if not, calculate and add it
        if self.name not in df.columns:
            # Download the historical price data for the given ticker
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the Mass Index series using high and low price data
            mass_index_series = mass_index(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                length=self.length
            )

            # Add the calculated Mass Index series to the DataFrame
            df[self.name] = mass_index_series

        # Return the Mass Index series as a pandas Series with appropriate naming
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Retrieve the name of the Mass Index series, including ticker and parameter details.

        :return: A string representing the Mass Index series name for this instance.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the MASS_INDEX signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'MASS_INDEX',
            'ticker': self._ticker,
            'length': self.length
        }