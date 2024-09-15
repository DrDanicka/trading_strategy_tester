import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.trend.sma import sma
from trading_strategy_tester.utils.validations import get_base_sources


class SMA(TradingSeries):
    """
    The SMA class retrieves the specified price data (e.g., 'Close') for a given ticker and applies the Simple
    Moving Average (SMA) calculation based on the specified length and offset.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 9, offset: int = 0):
        """
        Initializes the SMA series with the specified ticker symbol, target column, SMA length, and offset.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        source : str, optional
            The column in the DataFrame on which the SMA is calculated (e.g., 'Close'). Default is 'Close'.

        length : int, optional
            The number of periods over which to calculate the SMA. Default is 9.

        offset : int, optional
            The number of periods by which to shift the SMA. Default is 0.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the SMA calculation
        self.offset = offset  # Set the offset (number of periods to shift the SMA)
        self.name = f'{self._ticker}_SMA_{self.source}_{self.length}_{self.offset}'  # Define the name for the SMA series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this SMA series.

        This property provides access to the ticker symbol that was specified when the SMA instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the SMA data series for the specified ticker.

        This method checks if the SMA for the given ticker and configuration (target, length, offset) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the SMA, and adds it to
        the DataFrame. It returns a pandas Series containing the SMA values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the SMA does not exist in this DataFrame, it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the SMA values for the specified ticker and configuration, labeled with the appropriate name.
        """

        # Check if the SMA series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the SMA using the specified target column, length, and offset
            sma_series = sma(series=new_df[self.source], length=self.length, offset=self.offset)

            # Add the SMA series to the DataFrame
            df[self.name] = sma_series

        # Return the SMA series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name