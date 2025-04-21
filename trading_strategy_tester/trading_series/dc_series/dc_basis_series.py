import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volatility.dc import dc_basis
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class DC_BASIS(TradingSeries):
    """
    The DC_BASIS class calculates and retrieves the middle band (basis) of the Donchian Channel for a given financial instrument.

    The Donchian Channel's basis is determined by the average of the upper and lower bands over a specified period (length).
    It is used in technical analysis to identify the central trend of price movements.
    """

    def __init__(self, ticker: str, length: int = 20, offset: int = 0):
        """
        Initializes the DC_BASIS series with the specified ticker symbol, length, and offset.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The window length for calculating the basis of the Donchian Channel. Default is 20.
        :type length: int, optional
        :param offset: The number of periods by which to offset the basis. Default is 0.
        :type offset: int, optional
        """
        super().__init__(ticker)
        self.length = length  # Set the length (number of periods) for the calculation
        self.offset = offset  # Set the offset (number of periods) for the calculation
        self.name = f'{self._ticker}_DCBASIS_{self.length}_{self.offset}'  # Define the name for the DC_BASIS series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this DC_BASIS series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the DC_BASIS data series for the specified ticker.

        This method checks if the DC_BASIS series for the given ticker and configuration (length, offset)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates the
        DC_BASIS, and adds it to the DataFrame. It returns a pandas Series containing the DC_BASIS values.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the DC_BASIS does not exist in this
                   DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the DC_BASIS values for the specified ticker and configuration,
                 labeled with the appropriate name.
        :rtype: pd.Series
        """
        # Check if the DC_BASIS series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the DC_BASIS using the specified high and low columns, length, and offset
            dc_basis_series = dc_basis(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                length=self.length,
                offset=self.offset
            )

            # Add the DC_BASIS series to the DataFrame
            df[self.name] = dc_basis_series

        # Return the DC_BASIS series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series.

        :return: The name of the DC_BASIS series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Converts the DC_BASIS series to a dictionary representation.

        :return: A dictionary containing the series name and its values.
        :rtype: dict
        """
        return {
            'type': 'DC_BASIS',
            'ticker': self._ticker,
            'length': self.length,
            'offset': self.offset
        }