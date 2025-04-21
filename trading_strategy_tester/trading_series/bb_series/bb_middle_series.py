import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volatility.bb import bb_middle
from trading_strategy_tester.utils.parameter_validations import get_base_sources


class BB_MIDDLE(TradingSeries):
    """
    The BBMiddle class retrieves the specified price data (e.g., 'Close') for a given ticker and applies the
    Bollinger Band middle calculation based on the specified parameters.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 20,
                 ma_type: SmoothingType = SmoothingType.SMA, std_dev: float = 2, offset: int = 0):
        """
        Initialize the BBMiddle series with the specified parameters.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param source: The column in the DataFrame on which the middle Bollinger Band is calculated (e.g., 'Close').
                       Default is SourceType.CLOSE.
        :type source: SourceType, optional
        :param length: The number of periods over which to calculate the moving average. Default is 20.
        :type length: int, optional
        :param ma_type: The type of moving average to use (e.g., Simple Moving Average, SMA). Default is SmoothingType.SMA.
        :type ma_type: SmoothingType, optional
        :param std_dev: The number of standard deviations to use for the Bollinger Band calculation. Default is 2.
        :type std_dev: float, optional
        :param offset: The number of periods to offset the calculation. Default is 0.
        :type offset: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the moving average
        self.ma_type = ma_type  # Set the type of moving average (e.g., SMA)
        self.std_dev = float(std_dev)  # Set the number of standard deviations for the Bollinger Band
        self.offset = offset  # Set the offset for the calculation
        self.name = f'{self._ticker}_BBMIDDLE_{self.source}_{self.length}_{self.ma_type.value}_{self.std_dev}_{self.offset}'
        # Define the name for the BBMiddle series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this BBMiddle series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the middle Bollinger Band (BBMiddle) data series for the specified ticker.

        If the BBMiddle data is not already present in the provided DataFrame, this method downloads the
        latest market data for the ticker, calculates the BBMiddle indicator, and adds it to the DataFrame.

        :param downloader: The module responsible for downloading market data.
        :type downloader: DownloadModule
        :param df: DataFrame containing the existing market data.
        :type df: pd.DataFrame
        :return: A Pandas Series containing the middle Bollinger Band values for the specified ticker and configuration.
        :rtype: pd.Series
        """
        # Check if the BBMiddle series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest price data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the BBMiddle using the specified parameters
            bb_middle_series = bb_middle(
                series=new_df[self.source],
                length=self.length,
                ma_type=self.ma_type,
                std_dev=self.std_dev,
                offset=self.offset
            )

            # Add the BBMiddle series to the DataFrame
            df[self.name] = bb_middle_series

        # Return the BBMiddle series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the BBMiddle indicator.

        :return: The name of the BBMiddle indicator, formatted with the ticker and configuration.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the BBMiddle series to a dictionary representation.

        :return: A dictionary representation of the BBMiddle series.
        :rtype: dict
        """
        return {
            'type': 'BB_MIDDLE',
            'ticker': self._ticker,
            'source': self.source,
            'length': self.length,
            'ma_type': self.ma_type,
            'std_dev': self.std_dev,
            'offset': self.offset
        }