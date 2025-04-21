import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volatility.chop import chop
from trading_strategy_tester.enums.source_enum import SourceType

class CHOP(TradingSeries):
    """
    The CHOP class calculates the Choppiness Index for a given ticker symbol.

    The Choppiness Index is a technical analysis indicator that quantifies the market's tendency to trend
    or to consolidate. A high Choppiness Index indicates a choppy, sideways market, while a low value indicates
    a strong trending market.
    """

    def __init__(self, ticker: str, length: int = 14, offset: int = 0):
        """
        Initializes the CHOP series with the specified ticker symbol, length, and offset.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate the Choppiness Index. Default is 14.
        :type length: int
        :param offset: The number of periods to shift the resulting series. Default is 0.
        :type offset: int
        """
        super().__init__(ticker)
        self.length = length
        self.offset = offset
        self.name = f'{self._ticker}_CHOP_{self.length}_{self.offset}'

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this CHOP series.

        This property provides access to the ticker symbol that was specified when the CHOP instance was created.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the Choppiness Index data series for the specified ticker.

        This method checks if the Choppiness Index for the given ticker and configuration (length, offset)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates
        the Choppiness Index, and adds it to the DataFrame. It returns a pandas Series containing the
        Choppiness Index values.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the Choppiness Index does not exist in
                   this DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the Choppiness Index values for the specified ticker and configuration,
                 labeled with the appropriate name.
        :rtype: pd.Series
        """
        # Check if the CHOP series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the Choppiness Index using the specified high, low, close prices, length, and offset
            chop_series = chop(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                close=new_df[SourceType.CLOSE.value],
                length=self.length,
                offset=self.offset
            )

            # Add the Choppiness Index series to the DataFrame
            df[self.name] = chop_series

        # Return the Choppiness Index series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the Choppiness Index series.

        This method returns a string that includes the ticker symbol, length, and offset, which uniquely
        identifies the Choppiness Index series.

        :return: The name of the Choppiness Index series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Converts the CHOP series to a dictionary representation.

        This method provides a dictionary representation of the CHOP series, including its type,
        ticker symbol, length, and offset.

        :return: A dictionary representation of the CHOP series.
        :rtype: dict
        """
        return {
            'type': 'CHOP',
            'ticker': self._ticker,
            'length': self.length,
            'offset': self.offset
        }