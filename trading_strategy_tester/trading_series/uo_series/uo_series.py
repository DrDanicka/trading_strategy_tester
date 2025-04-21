import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.momentum.uo import uo


class UO(TradingSeries):
    """
    The UO (Ultimate Oscillator) class retrieves the specified price data (e.g., 'Close', 'Low', 'High') for
    a given ticker and applies the Ultimate Oscillator calculation based on specified fast, middle, and slow lengths.
    """

    def __init__(self, ticker: str, fast_length: int = 7, middle_length: int = 14, slow_length: int = 28):
        """
        Initialize the UO series with the specified ticker symbol and UO calculation lengths.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param fast_length: The number of periods for the fast component of the UO calculation. Default is 7.
        :type fast_length: int, optional
        :param middle_length: The number of periods for the middle component of the UO calculation. Default is 14.
        :type middle_length: int, optional
        :param slow_length: The number of periods for the slow component of the UO calculation. Default is 28.
        :type slow_length: int, optional
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        self.fast_length = fast_length  # Set the fast period length for UO calculation
        self.middle_length = middle_length  # Set the middle period length for UO calculation
        self.slow_length = slow_length  # Set the slow period length for UO calculation
        self.name = f'{ticker}_UO_{fast_length}_{middle_length}_{slow_length}'  # Define the name for the UO series

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this Ultimate Oscillator series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Ultimate Oscillator data series for the specified ticker.

        This method checks if the UO series for the given ticker and configuration (lengths) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the UO, and adds
        it to the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the UO series does not exist in this
        DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the Ultimate Oscillator values for the specified ticker and
        configuration, labeled with the appropriate name.
        :rtype: pd.Series
        """

        # Check if the Ultimate Oscillator series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the UO using the specified fast, middle, and slow lengths
            uo_series = uo(
                close=new_df[SourceType.CLOSE.value],
                low=new_df[SourceType.LOW.value],
                high=new_df[SourceType.HIGH.value],
                fast_length=self.fast_length,
                middle_length=self.middle_length,
                slow_length=self.slow_length
            )

            # Add the UO series to the DataFrame
            df[self.name] = uo_series

        # Return the UO series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the Ultimate Oscillator series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the UO signal series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'UO',
            'ticker': self._ticker,
            'fast_length': self.fast_length,
            'middle_length': self.middle_length,
            'slow_length': self.slow_length
        }