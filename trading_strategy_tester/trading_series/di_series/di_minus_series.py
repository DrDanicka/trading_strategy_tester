import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.dmi import di_minus
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class DI_MINUS(TradingSeries):
    """
    The DI_MINUS class calculates the Negative Directional Indicator (-DI) for a given ticker symbol.

    The Negative Directional Indicator (-DI) measures the presence of a downtrend in a financial market
    by comparing the current low price to the previous low price, normalized by the Average True Range (ATR).
    It is used in technical analysis to identify the strength of a potential downtrend.
    """

    def __init__(self, ticker: str, length: int = 14):
        """
        Initializes the DI_MINUS series with the specified ticker symbol and calculation length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate the -DI. Default is 14.
        :type length: int, optional
        """
        super().__init__(ticker)
        self.length = length  # Set the length for the -DI calculation
        self.name = f'{self._ticker}_DIMINUS_{self.length}'  # Define the name for the DI_MINUS series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this DI_MINUS series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the -DI data series for the specified ticker.

        This method checks if the -DI for the given ticker and configuration already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the -DI,
        and adds it to the DataFrame. It returns a pandas Series containing the -DI values.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the -DI does not exist
                   in this DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the -DI values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the DI_MINUS series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the -DI using the high, low, and close prices and the specified length
            di_minus_series = di_minus(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                close=new_df[SourceType.CLOSE.value],
                di_length=self.length
            )

            # Add the -DI series to the DataFrame
            df[self.name] = di_minus_series

        # Return the -DI series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series.

        :return: The name of the DI_MINUS series.
        :rtype: str
        """
        return self.name