import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.momentum.cmo import cmo
from trading_strategy_tester.utils.parameter_validations import get_base_sources


class CMO(TradingSeries):
    """
    The CMO (Chande Momentum Oscillator) class retrieves the specified price data (e.g., 'Close') for a given ticker
    and calculates the CMO based on the specified length.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 9):
        """
        Initialize the CMO series with the specified ticker symbol, target column, and CMO length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param source: The column in the DataFrame on which the CMO is calculated (e.g., 'Close'). Default is 'Close'.
        :type source: SourceType, optional
        :param length: The number of periods over which to calculate the CMO. Default is 9.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the CMO calculation
        self.name = f'{self._ticker}_CMO_{self.source}_{self.length}'  # Define the name for the CMO series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this CMO series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the CMO data series for the specified ticker.

        If the CMO data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the CMO indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the CMO values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the CMO series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self.ticker)
            # Calculate the CMO using the specified target column and length
            cmo_series = cmo(series=new_df[self.source], length=self.length)

            # Add the CMO series to the DataFrame
            df[self.name] = cmo_series

        # Return the CMO series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the CMO series.

        :return: The name of the CMO series, formatted with the ticker, source, and CMO length.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the CMO series to a dictionary representation.

        :return: A dictionary containing the CMO series data.
        :rtype: dict
        """
        return {
            'type': 'CMO',
            'ticker': self._ticker,
            'source': self.source,
            'length': self.length,
        }