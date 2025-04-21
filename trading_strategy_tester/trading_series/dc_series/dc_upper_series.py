import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volatility.dc import dc_upper
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class DC_UPPER(TradingSeries):
    """
    The DC_UPPER class calculates and retrieves the upper band of the Donchian Channel for a given financial instrument.

    The Donchian Channel's upper band is determined by the highest high over a specified period (length).
    It is used in technical analysis to identify potential resistance levels or the upper boundary of price movements.
    """

    def __init__(self, ticker: str, length: int = 20, offset: int = 0):
        """
        Initializes the DCUpper series with the specified ticker symbol, length, and offset.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The window length for calculating the highest high. Default is 20.
        :type length: int, optional
        :param offset: The number of periods by which to offset the upper band. Default is 0.
        :type offset: int, optional
        """
        super().__init__(ticker)
        self.length = length  # Set the length (number of periods) for the calculation
        self.offset = offset  # Set the offset (number of periods) for the calculation
        self.name = f'{self._ticker}_DCUPPER_{self.length}_{self.offset}'  # Define the name for the DCUpper series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this DCUpper series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the DCUpper data series for the specified ticker.

        This method checks if the DCUpper series for the given ticker and configuration (length, offset)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates the
        DCUpper, and adds it to the DataFrame. It returns a pandas Series containing the DCUpper values.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the DCUpper does not exist in this
                   DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the DCUpper values for the specified ticker and configuration,
                 labeled with the appropriate name.
        :rtype: pd.Series
        """
        # Check if the DCUpper series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the DCUpper using the specified high column, length, and offset
            dc_upper_series = dc_upper(high=new_df[SourceType.HIGH.value], length=self.length, offset=self.offset)

            # Add the DCUpper series to the DataFrame
            df[self.name] = dc_upper_series

        # Return the DCUpper series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series.

        :return: The name of the DCUpper series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Converts the DCUpper series to a dictionary representation.

        :return: A dictionary containing the series name and its values.
        :rtype: dict
        """
        return {
            'type': 'DC_UPPER',
            'ticker': self._ticker,
            'length': self.length,
            'offset': self.offset
        }