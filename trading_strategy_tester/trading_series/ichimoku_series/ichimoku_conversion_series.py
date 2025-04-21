import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.overlap.ichimoku import conversion_line
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class ICHIMOKU_CONVERSION(TradingSeries):
    """
    A class to calculate and manage the Ichimoku Conversion Line (Tenkan-sen) for a specific ticker.

    Inherits from:
    - TradingSeries

    :param ticker: The ticker symbol of the asset for which to calculate the Ichimoku Conversion Line.
    :type ticker: str
    :param length: The period length over which the Conversion Line is calculated (default is 9).
    :type length: int
    """

    def __init__(self, ticker: str, length: int = 9):
        """
        Initialize the ICHIMOKU_CONVERSION class with the ticker and length.

        :param ticker: The ticker symbol for the asset.
        :type ticker: str
        :param length: The period for calculating the Conversion Line (default is 9).
        :type length: int
        """
        super().__init__(ticker)
        self.length = length
        self.name = f'{self._ticker}_ICHIMOKU-CONVERSION-LINE_{self.length}'

    @property
    def ticker(self) -> str:
        """
        Getter method to access the ticker symbol.

        :return: The ticker symbol.
        :rtype: str
        """
        return self._ticker

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieve or calculate the Ichimoku Conversion Line for the ticker.

        If the Conversion Line is not present in the provided DataFrame, it downloads the necessary data,
        computes the Conversion Line, and appends it to the DataFrame.

        :param downloader: An instance of DownloadModule to download the ticker data.
        :type downloader: DownloadModule
        :param df: A DataFrame to check for the existence of the Ichimoku Conversion Line and store it if necessary.
        :type df: pd.DataFrame
        :return: The calculated Ichimoku Conversion Line as a pandas Series.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download new data for the ticker if Conversion Line is not already present
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the Ichimoku Conversion Line (Tenkan-sen)
            ichimoku_conversion_series = conversion_line(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                length=self.length,
            )

            # Store the result in the DataFrame
            df[self.name] = ichimoku_conversion_series

        # Return the calculated or existing Conversion Line as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Return the name of the Ichimoku Conversion Line, which includes the ticker and length.

        :return: The name of the Ichimoku Conversion Line.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the ICHIMOKU_CONVERSION series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'ICHIMOKU_CONVERSION',
            'ticker': self._ticker,
            'length': self.length
        }