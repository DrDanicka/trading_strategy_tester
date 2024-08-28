import pandas as pd
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.trading_series import TradingSeries


class Const(TradingSeries):
    """
    The Const class represents a constant data series that generates a series of a fixed numeric value
    (const_number) for a given DataFrame.

    This is useful for cases where a constant value is needed across the entire length of a DataFrame,
    such as setting a baseline or a fixed reference point.
    """

    def __init__(self, const_number: int):
        """
        Initializes the constant series with the specified numeric value.

        Parameters:
        -----------
        const_number : int
            The constant numeric value that will be used to generate the data series.
        """
        super().__init__('')  # Initialize the parent TradingSeries class without a specific ticker symbol
        self.const_number = const_number  # Store the constant numeric value
        self.name = f'__Const_{const_number}'  # Define the name for the constant series

    @property
    def ticker(self) -> str:
        """
        Returns an empty string as the ticker symbol for this constant series.

        This property is overridden to provide an empty string because a constant series
        does not have an associated ticker.

        Returns:
        --------
        str
            An empty string representing the ticker symbol.
        """
        return ''

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Generates a constant data series with the specified value (const_number) for the length of the given DataFrame.

        This method creates a pandas Series filled with the constant value across all rows of the DataFrame.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule (not used in this implementation, included for compatibility).

        df : pd.DataFrame
            A DataFrame for which the constant series is to be generated.

        Returns:
        --------
        pd.Series
            A pandas Series containing the constant numeric value (const_number) for the entire length of the DataFrame.
        """
        # Create a Series filled with the constant value for the entire length of the DataFrame
        return pd.Series([self.const_number] * len(df), index=df.index, name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the constant series.

        This method provides the name that identifies the constant series, which is based on the constant value.

        Returns:
        --------
        str
            The name of the constant series.
        """
        return self.name
