import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.volatility.bb import bb_upper
from trading_strategy_tester.utils.validations import get_base_sources


class BBUPPER(TradingSeries):
    """
    The BBUpper class retrieves the specified price data (e.g., 'Close') for a given ticker and applies the
    Bollinger Band upper calculation based on the specified parameters.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 20, ma_type: SmoothingType = SmoothingType.SMA,
                 std_dev: float = 2, offset: int = 0):
        """
        Initializes the BBUpper series with the specified parameters.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        source : str, optional
            The column in the DataFrame on which the upper Bollinger Band is calculated (e.g., 'Close').
            Default is 'Close'.

        length : int, optional
            The number of periods over which to calculate the moving average. Default is 20.

        ma_type : SmoothingType, optional
            The type of moving average to use (e.g., Simple Moving Average, SMA). Default is SmoothingType.SMA.

        std_dev : int, optional
            The number of standard deviations to use for the Bollinger Band calculation. Default is 2.

        offset : int, optional
            The number of periods to offset the calculation. Default is 0.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the moving average
        self.ma_type = ma_type  # Set the type of moving average (e.g., SMA)
        self.std_dev = float(std_dev)  # Set the number of standard deviations for the Bollinger Band
        self.offset = offset  # Set the offset for the calculation
        self.name = f'{self._ticker}_BBUPPER_{self.source}_{self.length}_{self.ma_type.value}_{self.std_dev}_{self.offset}'
        # Define the name for the BBUpper series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this BBUpper series.

        This property provides access to the ticker symbol that was specified when the BBUpper instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the upper Bollinger Band (BBUpper) data series for the specified ticker.

        This method checks if the BBUpper for the given ticker and configuration (target, length, ma_type, std_dev, offset)
        already exists in the provided DataFrame. If it does not exist, it downloads the data, calculates the BBUpper,
        and adds it to the DataFrame. It returns a pandas Series containing the BBUpper values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the BBUpper does not exist in this DataFrame,
            it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the upper Bollinger Band values for the specified ticker and configuration,
            labeled with the appropriate name.
        """

        # Check if the BBUpper series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self._ticker)
            # Calculate the BBUpper using the specified parameters
            bb_upper_series = bb_upper(
                series=new_df[self.source],
                length=self.length,
                ma_type=self.ma_type,
                std_dev=self.std_dev,
                offset=self.offset
            )

            # Add the BBUpper series to the DataFrame
            df[self.name] = bb_upper_series

        # Return the BBUpper series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series
        """
        return self.name