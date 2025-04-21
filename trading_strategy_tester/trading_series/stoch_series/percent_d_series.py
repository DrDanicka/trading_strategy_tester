import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.stoch import percent_d
from trading_strategy_tester.trading_series.trading_series import TradingSeries

class STOCH_PERCENT_D(TradingSeries):
    """
    The STOCH_PERCENT_D class retrieves the price data (e.g., 'Close', 'Low', 'High') for a given ticker and applies
    the Stochastic %D calculation based on specified periods for %K and %D smoothing.
    """

    def __init__(self, ticker: str, length: int = 14, smoothing_length: int = 3):
        """
        Initialize the STOCH_PERCENT_D series with the specified ticker symbol, %K period length,
        and %D smoothing period.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate the %K component of the Stochastic Oscillator.
        Default is 14.
        :type length: int, optional
        :param smoothing_length: The number of periods over which to calculate the %D smoothing of %K. Default is 3.
        :type smoothing_length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for the %K calculation
        self.d_smooth_length = smoothing_length  # Set the length for %D smoothing
        self.name = f'{self._ticker}_STOCH-PERCENT-D_{self.length}_{self.d_smooth_length}'  # Define the name for the series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this Stochastic %D series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Stochastic %D data series for the specified ticker.

        This method checks if the %D series for the given ticker and configuration (length and d_smooth_length)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates %D,
        and adds it to the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If %D does not exist in this DataFrame,
        it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the Stochastic %D values for the specified ticker and configuration,
        labeled with the appropriate name.
        :rtype: pd.Series
        """

        # Check if the Stochastic %D series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the %D series using the specified length and smoothing period
            percent_d_series = percent_d(
                close=new_df[SourceType.CLOSE.value],
                low=new_df[SourceType.LOW.value],
                high=new_df[SourceType.HIGH.value],
                length=self.length,
                d_smooth_length=self.d_smooth_length
            )

            # Add the %D series to the DataFrame
            df[self.name] = percent_d_series

        # Return the %D series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the Stochastic %D series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the STOCH_PERCENT_D signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'STOCH_PERCENT_D',
            'ticker': self._ticker,
            'length': self.length,
            'smoothing_length': self.d_smooth_length
        }