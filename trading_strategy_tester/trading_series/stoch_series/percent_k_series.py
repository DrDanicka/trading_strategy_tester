import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.stoch import percent_k
from trading_strategy_tester.trading_series.trading_series import TradingSeries

class STOCH_PERCENT_K(TradingSeries):
    """
    The STOCH_PERCENT_K class retrieves the specified price data (e.g., 'Close', 'Low', 'High') for a given ticker
    and applies the Stochastic %K calculation based on a specified period.
    """

    def __init__(self, ticker: str, length: int = 14):
        """
        Initialize the STOCH_PERCENT_K series with the specified ticker symbol and %K period length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param length: The number of periods over which to calculate the %K component of the Stochastic Oscillator.
        Default is 14.
        :type length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.length = length  # Set the length (number of periods) for the %K calculation
        self.name = f'{self._ticker}_STOCH-PERCENT-K_{self.length}'  # Define the name for the %K series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this Stochastic %K series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Stochastic %K data series for the specified ticker.

        This method checks if the %K for the given ticker and configuration (length) already exists in the provided
        DataFrame. If it does not exist, it downloads the data, calculates %K, and adds it to the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the %K does not exist in this DataFrame,
        it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the Stochastic %K values for the specified ticker and configuration,
        labeled with the appropriate name.
        :rtype: pd.Series
        """

        # Check if the Stochastic %K series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the %K series using the specified length
            percent_k_series = percent_k(
                close=new_df[SourceType.CLOSE.value],
                low=new_df[SourceType.LOW.value],
                high=new_df[SourceType.HIGH.value],
                length=self.length
            )

            # Add the %K series to the DataFrame
            df[self.name] = percent_k_series

        # Return the %K series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the Stochastic %K series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the STOCH_PERCENT_K signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'STOCH_PERCENT_K',
            'ticker': self._ticker,
            'length': self.length
        }