import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.overlap.ichimoku import leading_span_a
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class ICHIMOKU_LEADING_SPAN_A(TradingSeries):
    """
    A class to calculate and manage the Ichimoku Leading Span A (Senkou Span A) for a specific ticker.

    Inherits from:
    - TradingSeries

    :param ticker: The ticker symbol of the asset for which to calculate the Ichimoku Leading Span A.
    :type ticker: str
    :param displacement: The period displacement for shifting the span forward (default is 26).
    :type displacement: int
    """

    def __init__(self, ticker: str, displacement: int = 26):
        """
        Initialize the ICHIMOKU_LEADING_SPAN_A class with the ticker and displacement.

        :param ticker: The ticker symbol for the asset.
        :type ticker: str
        :param displacement: The number of periods to shift the span forward (default is 26).
        :type displacement: int
        """
        super().__init__(ticker)
        self.displacement = displacement
        self.name = f'{self._ticker}_ICHIMOKU-SPAN-A_{self.displacement}'

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
        Retrieve or calculate the Ichimoku Leading Span A for the ticker.

        If the Leading Span A is not present in the provided DataFrame, it downloads the necessary data,
        computes the Leading Span A, and appends it to the DataFrame.

        :param downloader: An instance of DownloadModule to download the ticker data.
        :type downloader: DownloadModule
        :param df: A DataFrame to check for the existence of the Ichimoku Leading Span A and store it if necessary.
        :type df: pd.DataFrame
        :return: The calculated Ichimoku Leading Span A as a pandas Series.
        :rtype: pd.Series
        """
        if self.name not in df.columns:
            # Download new data for the ticker if Leading Span A is not already present
            new_df = downloader.download_ticker(self._ticker)

            # Calculate the Ichimoku Leading Span A (Senkou Span A)
            ichimoku_leading_span_a = leading_span_a(
                high=new_df[SourceType.HIGH.value],
                low=new_df[SourceType.LOW.value],
                displacement=self.displacement,
            )

            # Store the result in the DataFrame
            df[self.name] = ichimoku_leading_span_a

        # Return the calculated or existing Leading Span A as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Return the name of the Ichimoku Leading Span A, which includes the ticker and displacement.

        :return: The name of the Ichimoku Leading Span A.
        :rtype: str
        """
        return self.name

    def to_dict(self) -> dict:
        """
        Convert the ICHIMOKU_LEADING_SPAN_A series to a dictionary representation.

        :return: A dictionary containing the series type and its values.
        :rtype: dict
        """
        return {
            'type': 'ICHIMOKU_LEADING_SPAN_A',
            'ticker': self._ticker,
            'displacement': self.displacement
        }