import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.trend.dpo import dpo


class DPO(TradingSeries):
    """
    The DPO (Detrended Price Oscillator) class calculates and retrieves the DPO for a given financial instrument.

    The DPO is used to remove long-term trends from prices, highlighting short-term trends by comparing the price to a
    simple moving average that is shifted by a specified period.
    """

    def __init__(self, ticker: str, length: int = 14):
        """
        Initializes the DPO series with the specified ticker symbol and length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The period length for calculating the Detrended Price Oscillator. Default is 14.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the period length for the DPO calculation
        self.name = f'{self._ticker}_DPO_{self.length}'  # Define the name for the DPO series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this DPO series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the DPO data series for the specified ticker.

        This method checks if the DPO series for the given ticker and configuration (length)
        already exists in the provided DataFrame. If it does not exist, it downloads the data,
        calculates the DPO, and adds it to the DataFrame. It returns a pandas Series containing
        the DPO values.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the DPO does not exist in this
                   DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the DPO values for the specified ticker and configuration,
                 labeled with the appropriate name.
        :rtype: pd.Series
        """
        # Check if the DPO series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the DPO using the closing price, and the specified length
            dpo_series = dpo(series=new_df[SourceType.CLOSE.value], length=self.length)

            # Add the DPO series to the DataFrame
            df[self.name] = dpo_series

        # Return the DPO series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series.

        :return: The name of the DPO series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the DPO series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'DPO',
            'ticker': self._ticker,
            'length': self.length
        }