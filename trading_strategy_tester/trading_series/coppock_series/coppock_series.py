import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.momentum.cop import cop

class COPPOCK(TradingSeries):
    """
    The COPPOCK class retrieves the specified price data (e.g., 'Close') for a given ticker
    and applies the Coppock Curve calculation based on the specified parameters.

    The Coppock Curve is a momentum indicator used in technical analysis primarily to identify long-term buying opportunities.
    It is calculated using a weighted moving average of the sum of the rates of change (ROC) for two different periods.
    """

    def __init__(self, ticker: str, length: int = 10, long_roc_length: int = 14, short_roc_length: int = 11):
        """
        Initialize the COPPOCK series with the specified ticker symbol, lengths, and parameters.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The window length to calculate the weighted moving average for the Coppock Curve. Default is 10.
        :type length: int, optional
        :param long_roc_length: The number of periods to use for calculating the long rate of change (ROC). Default is 14.
        :type long_roc_length: int, optional
        :param short_roc_length: The number of periods to use for calculating the short rate of change (ROC). Default is 11.
        :type short_roc_length: int, optional
        """
        super().__init__(ticker)
        self.length = length  # Set the length for the weighted moving average calculation
        self.long_roc_length = long_roc_length  # Set the period length for the long rate of change
        self.short_roc_length = short_roc_length  # Set the period length for the short rate of change
        # Define the name for the Coppock Curve series
        self.name = f'{self._ticker}_COPPOCK_{self.length}_{self.long_roc_length}_{self.short_roc_length}'

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this Coppock Curve series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Coppock Curve data series for the specified ticker.

        This method checks if the Coppock Curve for the given ticker and configuration already exists in the provided DataFrame.
        If it does not exist, it downloads the data, calculates the Coppock Curve, and adds it to the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the Coppock Curve does not exist in this DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the Coppock Curve values for the specified ticker and configuration, labeled with the appropriate name.
        :rtype: pd.Series
        """
        # Check if the Coppock Curve series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the Coppock Curve using the specified length, long and short ROC lengths
            coppock_series = cop(series=new_df[SourceType.CLOSE.value], length=self.length)

            # Add the Coppock Curve series to the DataFrame
            df[self.name] = coppock_series

        # Return the Coppock Curve series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the Coppock Curve series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the COPPOCK series to a dictionary representation.

        :return: A dictionary containing the series name and its values.
        :rtype: dict
        """
        return {
            'type': 'COPPOCK',
            'ticker': self._ticker,
            'length': self.length,
            'long_roc_length': self.long_roc_length,
            'short_roc_length': self.short_roc_length
        }