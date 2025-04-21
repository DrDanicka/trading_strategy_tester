import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.overlap.ichimoku import leading_span_b
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class ICHIMOKU_LEADING_SPAN_B(TradingSeries):
    """
    A class to calculate and manage the Ichimoku Leading Span B (Senkou Span B) for a specific ticker.

    Inherits from:
    - TradingSeries

    :param ticker: The ticker symbol of the asset for which to calculate the Ichimoku Leading Span B.
    :type ticker: str
    :param length: The period length over which the Leading Span B is calculated (default is 52).
    :type length: int
    :param displacement: The period displacement for shifting the span forward (default is 26).
    :type displacement: int
    """

    def __init__(self, ticker: str, length: int = 52, displacement: int = 26):
        """
        Initialize the ICHIMOKU_LEADING_SPAN_B class with the ticker, length, and displacement.

        :param ticker: The ticker symbol for the asset.
        :type ticker: str
        :param length: The period for calculating the Leading Span B (default is 52).
        :type length: int
        :param displacement: The number of periods to shift the span forward (default is 26).
        :type displacement: int
        """
        super().__init__(ticker)
        self.length = length
        self.displacement = displacement
        self.name = f'{self._ticker}_ICHIMOKU-SPAN-B_{self.length}_{self.displacement}'

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
        Retrieve or calculate the Ichimoku Leading Span B for the ticker.

        If the Leading Span B is not present in the provided DataFrame, it downloads the necessary data,
        computes the Leading Span B, and appends it to the DataFrame.

        :param downloader: An instance of DownloadModule to download the ticker data.
        :type downloader: DownloadModule
        :param df: A DataFrame to check for the existence of the Ichimoku Leading Span B and store it if necessary.
        :type df: pd.DataFrame
        :return: The calculated Ichimoku Leading Span B as a pandas Series.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download new data for the ticker if Leading Span B is not already present
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the Ichimoku Leading Span B (Senkou Span B)
            ichimoku_leading_span_b = leading_span_b(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                length=self.length,
                displacement=self.displacement,
            )

            # Store the result in the DataFrame
            df[self.name] = ichimoku_leading_span_b

        # Return the calculated or existing Leading Span B as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Return the name of the Ichimoku Leading Span B, which includes the ticker, length, and displacement.

        :return: The name of the Ichimoku Leading Span B.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the ICHIMOKU_LEADING_SPAN_B series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'ICHIMOKU_LEADING_SPAN_B',
            'ticker': self._ticker,
            'length': self.length,
            'displacement': self.displacement
        }