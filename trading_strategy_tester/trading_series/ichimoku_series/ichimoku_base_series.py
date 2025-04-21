import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.overlap.ichimoku import base_line
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class ICHIMOKU_BASE(TradingSeries):
    """
    A class to calculate and manage the Ichimoku Base Line (Kijun-sen) for a specific ticker.

    Inherits from:
    - TradingSeries

    :param ticker: The ticker symbol of the asset for which to calculate the Ichimoku Base Line.
    :type ticker: str
    :param length: The period length over which the Base Line is calculated (default is 26).
    :type length: int
    """

    def __init__(self, ticker: str, length: int = 26):
        """
        Initialize the ICHIMOKU_BASE class with the ticker and length.

        :param ticker: The ticker symbol for the asset.
        :type ticker: str
        :param length: The period for calculating the Base Line (default is 26).
        :type length: int
        """
        super().__init__(ticker)
        self.length = length
        self.name = f'{self._ticker}_ICHIMOKU-BASE-LINE_{self.length}'

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
        Retrieve or calculate the Ichimoku Base Line for the ticker.

        If the Base Line is not present in the provided DataFrame, it downloads the necessary data,
        computes the Base Line, and appends it to the DataFrame.

        :param downloader: An instance of DownloadModule to download the ticker data.
        :type downloader: DownloadModule
        :param df: A DataFrame to check for the existence of the Ichimoku Base Line and store it if necessary.
        :type df: pd.DataFrame
        :return: The calculated Ichimoku Base Line as a pandas Series.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download new data for the ticker if Base Line is not already present
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the Ichimoku Base Line (Kijun-sen)
            ichimoku_base_series = base_line(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                length=self.length,
            )

            # Store the result in the DataFrame
            df[self.name] = ichimoku_base_series

        # Return the calculated or existing Base Line as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Return the name of the Ichimoku Base Line, which includes the ticker and length.

        :return: The name of the Ichimoku Base Line.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the ICHIMOKU_BASE series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'ICHIMOKU_BASE',
            'ticker': self._ticker,
            'length': self.length
        }