import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.utils.parameter_validations import get_base_sources
from trading_strategy_tester.indicators.momentum.kst import kst_signal


class KST_SIGNAL(TradingSeries):
    """
    The KST_SIGNAL class retrieves the specified price data (e.g., 'Close') for a given ticker
    and applies the KST signal line calculation based on specified ROC, SMA, and signal line lengths.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE,
                 roc_length_1: int = 10,
                 roc_length_2: int = 15,
                 roc_length_3: int = 20,
                 roc_length_4: int = 30,
                 sma_length_1: int = 10,
                 sma_length_2: int = 10,
                 sma_length_3: int = 10,
                 sma_length_4: int = 15,
                 signal_length: int = 9):
        """
        Initialize the KST signal series with the specified ticker symbol, data source,
        ROC and SMA periods, and signal line length.

        :param ticker: The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).
        :type ticker: str
        :param source: The column in the DataFrame on which the KST signal is calculated (e.g., 'Close'). Default is 'Close'.
        :type source: SourceType, optional
        :param roc_length_1: The period length for the first ROC calculation. Default is 10.
        :type roc_length_1: int, optional
        :param roc_length_2: The period length for the second ROC calculation. Default is 15.
        :type roc_length_2: int, optional
        :param roc_length_3: The period length for the third ROC calculation. Default is 20.
        :type roc_length_3: int, optional
        :param roc_length_4: The period length for the fourth ROC calculation. Default is 30.
        :type roc_length_4: int, optional
        :param sma_length_1: The period length for the SMA of the first ROC. Default is 10.
        :type sma_length_1: int, optional
        :param sma_length_2: The period length for the SMA of the second ROC. Default is 10.
        :type sma_length_2: int, optional
        :param sma_length_3: The period length for the SMA of the third ROC. Default is 10.
        :type sma_length_3: int, optional
        :param sma_length_4: The period length for the SMA of the fourth ROC. Default is 15.
        :type sma_length_4: int, optional
        :param signal_length: The period length for the SMA of the KST line, which generates the signal line. Default is 9.
        :type signal_length: int, optional
        """

        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate and set the data source column
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.roc_length_1 = roc_length_1
        self.roc_length_2 = roc_length_2
        self.roc_length_3 = roc_length_3
        self.roc_length_4 = roc_length_4
        self.sma_length_1 = sma_length_1
        self.sma_length_2 = sma_length_2
        self.sma_length_3 = sma_length_3
        self.sma_length_4 = sma_length_4
        self.signal_length = signal_length
        self.name = f'{self._ticker}_KST-SIGNAL_{self.roc_length_1}_{self.roc_length_2}_{self.roc_length_3}_{self.roc_length_4}_{self.sma_length_1}_{self.sma_length_2}_{self.sma_length_3}_{self.sma_length_4}_{self.signal_length}'

    @property
    def ticker(self) -> str:
        """
        Get the ticker symbol associated with this KST signal series.

        :return: The ticker symbol for the financial instrument.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the KST signal data series for the specified ticker.

        This method checks if the KST signal for the given ticker and configuration (source, ROC/SMA lengths, and signal length)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates
        the KST signal, and adds it to the DataFrame.

        :param downloader: An instance of DownloadModule used to download the latest data for the ticker.
        :type downloader: DownloadModule
        :param df: A DataFrame that may contain existing trading data. If the KST signal does not exist in this DataFrame, it will be calculated and added.
        :type df: pd.DataFrame
        :return: A pandas Series containing the KST signal values for the specified ticker and configuration, labeled with the appropriate name.
        :rtype: pd.Series
        """

        # Check if the KST signal series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the KST signal using the specified source column, ROC/SMA lengths, and signal length
            kst_series = kst_signal(series=new_df[self.source],
                                    roc_length_1=self.roc_length_1,
                                    roc_length_2=self.roc_length_2,
                                    roc_length_3=self.roc_length_3,
                                    roc_length_4=self.roc_length_4,
                                    sma_length_1=self.sma_length_1,
                                    sma_length_2=self.sma_length_2,
                                    sma_length_3=self.sma_length_3,
                                    sma_length_4=self.sma_length_4,
                                    signal_length=self.signal_length)

            # Add the KST signal series to the DataFrame
            df[self.name] = kst_series

        # Return the KST signal series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Get the name of the KST signal series.

        :return: The name of the series.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the KST series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'KST',
            'ticker': self._ticker,
            'source': self.source,
            'roc_length_1': self.roc_length_1,
            'roc_length_2': self.roc_length_2,
            'roc_length_3': self.roc_length_3,
            'roc_length_4': self.roc_length_4,
            'sma_length_1': self.sma_length_1,
            'sma_length_2': self.sma_length_2,
            'sma_length_3': self.sma_length_3,
            'sma_length_4': self.sma_length_4,
            'signal_length': self.signal_length
        }