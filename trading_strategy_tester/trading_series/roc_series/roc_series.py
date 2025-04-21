import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.parameter_validations import get_base_sources
from trading_strategy_tester.indicators.momentum.roc import roc

class ROC(TradingSeries):
    """
    The ROC class retrieves the specified price data (e.g., 'Close') for a given ticker
    and applies the Rate of Change (ROC) calculation based on the specified length.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 9):
        """
        Initialize the ROC series with the specified ticker symbol, target column, and ROC length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param source: The column in the DataFrame on which the ROC is calculated (e.g., 'Close'). Default is 'Close'.
        :type source: SourceType, optional
        :param length: The number of periods over which to calculate the ROC. Default is 9.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the ROC calculation
        self.name = f'{self._ticker}_ROC_{self.source}_{self.length}'  # Define the name for the ROC series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this ROC series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the ROC data series for the specified ticker.

        This method checks if the ROC for the given ticker and configuration (target, length) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the ROC, and adds it to
        the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the ROC does not exist in this DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the ROC values for the specified ticker and configuration, labeled with the appropriate name.
        :rtype: pd.Series
        """
        # Check if the ROC series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the ROC using the specified target column and length
            roc_series = roc(series=new_df[self.source], length=self.length)

            # Add the ROC series to the DataFrame
            df[self.name] = roc_series

        # Return the ROC series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the ROC series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the ROC signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'ROC',
            'ticker': self._ticker,
            'source': self.source,
            'length': self.length
        }