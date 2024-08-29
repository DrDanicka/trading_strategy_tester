import pandas as pd

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trading_series.trading_series import TradingSeries
from trading_strategy_tester.indicators.cmo import cmo
from trading_strategy_tester.utils.validations import get_base_sources


class CMO(TradingSeries):
    """
    The CMO (Chande Momentum Oscillator) class retrieves the specified price data (e.g., 'Close') for a given ticker
    and calculates the CMO based on the specified length.
    """

    def __init__(self, ticker: str, source: SourceType = SourceType.CLOSE, length: int = 9):
        """
        Initializes the CMO series with the specified ticker symbol, target column, and CMO length.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the financial instrument (e.g., 'AAPL' for Apple Inc.).

        source : str, optional
            The column in the DataFrame on which the CMO is calculated (e.g., 'Close'). Default is 'Close'.

        length : int, optional
            The number of periods over which to calculate the CMO. Default is 9.
        """
        super().__init__(ticker)  # Initialize the parent TradingSeries class with the ticker symbol
        # Validate source
        self.source = get_base_sources(source=source, default=SourceType.CLOSE).value
        self.length = length  # Set the length (number of periods) for the CMO calculation
        self.name = f'{self._ticker}_CMO_{self.source}_{self.length}'  # Define the name for the CMO series

    @property
    def ticker(self) -> str:
        """
        Returns the ticker symbol associated with this CMO series.

        This property provides access to the ticker symbol that was specified when the CMO instance was created.

        Returns:
        --------
        str
            The ticker symbol for the financial instrument.
        """
        return self._ticker  # Return the ticker symbol stored in the parent class

    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        """
        Retrieves or calculates the CMO data series for the specified ticker.

        This method checks if the CMO for the given ticker and configuration (target, length) already exists
        in the provided DataFrame. If it does not exist, it downloads the data, calculates the CMO, and adds it to
        the DataFrame. It returns a pandas Series containing the CMO values.

        Parameters:
        -----------
        downloader : DownloadModule
            An instance of DownloadModule used to download the latest data for the ticker.

        df : pd.DataFrame
            A DataFrame that may contain existing trading data. If the CMO does not exist in this DataFrame,
            it will be calculated and added.

        Returns:
        --------
        pd.Series
            A pandas Series containing the CMO values for the specified ticker and configuration, labeled with
            the appropriate name.
        """

        # Check if the CMO series already exists in the DataFrame
        if self.name not in df.columns:
            # Download the latest data for the ticker using the downloader
            new_df = downloader.download_ticker(self.ticker)
            # Calculate the CMO using the specified target column and length
            cmo_series = cmo(series=new_df[self.source], length=self.length)

            # Add the CMO series to the DataFrame
            df[self.name] = cmo_series

        # Return the CMO series as a pandas Series
        return pd.Series(df[self.name], name=self.name)

    def get_name(self) -> str:
        """
        Returns the name of the series.

        This method provides access to the name of the CMO series, which is formatted based on the ticker,
        target column, and length of the CMO.

        Returns:
        --------
        str
            The name of the CMO series.
        """
        return self.name
