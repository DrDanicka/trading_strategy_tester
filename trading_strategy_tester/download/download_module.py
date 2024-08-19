import os
import pandas as pd
import yfinance as yf
from datetime import datetime

from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.enums.period_enum import Period

class DownloadModule:
    """
    A module for downloading and caching financial data from Yahoo Finance.

    Attributes:
    -----------
    start_date : datetime
        The start date for the data download.
    end_date : datetime:
        The end date for the data download.
    interval : str:
        The interval between data points (e.g., daily, weekly).
    period : str:
        The period over which to fetch data (e.g., 1mo, 1y).

    Methods:
    -------
    download_save_and_return_ticker(ticker, filepath, datetime_type):
        Downloads data for a given ticker, saves it to a CSV file, and returns a DataFrame.
    return_cached_or_download_date(ticker):
        Returns cached data based on start and end date for a given ticker if available, otherwise downloads it.
    return_cached_or_download_period(ticker):
        Returns cached data based on a specified period for a given ticker if available, otherwise downloads it.
    download_ticker(ticker):
        Determines the appropriate method to fetch data based on the period and returns the DataFrame.
    """

    def __init__(self,
                 start_date:datetime=datetime(2024, 1, 1),
                 end_date:datetime=datetime.today(),
                 interval: Interval=Interval.ONE_DAY,
                 period: Period=Period.NOT_PASSED):
        """
        Initializes the DownloadModule with the given parameters.

        Parameters:
        -----------
        start_date : datetime
            The start date for the data download.
        end_date : datetime
            The end date for the data download.
        interval : Interval
            The interval between data points.
        period : Period
            The period over which to fetch data.
        """

        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval.value  # String value representing the interval
        self.period = period.value  # String value representing the period

        script_dir = os.path.dirname(__file__)
        os.chdir(script_dir)

        self.data_path = os.path.join('..', '..', 'data')

    def download_save_and_return_ticker(self, ticker: str, filepath: str, datetime_type: bool) -> pd.DataFrame:
        """
        Downloads data for a given ticker and saves it to a CSV file. Returns the data as a DataFrame.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the data to be downloaded.
        filepath : str
            The file path where the data should be saved.
        datetime_type : bool
            If True, uses start_date and end_date for downloading; otherwise, uses period.

        Returns:
        --------
        pd.DataFrame
            The DataFrame containing the downloaded data.
        """

        if datetime_type:
            df = yf.download(ticker, interval=self.interval, start=self.start_date, end=self.end_date)
        else:
            df = yf.download(ticker, interval=self.interval, period=self.period)

        df.to_csv(filepath)

        return df


    def return_cached_or_download_date(self, ticker: str) -> pd.DataFrame:
        """
        Returns cached data for the given ticker if available; otherwise, downloads it using a date range.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the data to be retrieved or downloaded.

        Returns:
        --------
        pd.DataFrame
            The DataFrame containing the cached or newly downloaded data.
        """

        # Filename format consists of Ticker, start date, end date and interval separated by '_'
        filename = f'{ticker}_{self.start_date.date()}_{self.end_date.date()}_{self.interval}.csv'
        filepath = os.path.join(self.data_path, filename)

        if os.path.isfile(filepath):
            return pd.read_csv(filepath, index_col='Date', parse_dates=True)
        else:
            return self.download_save_and_return_ticker(ticker, filepath, True)

    def return_cached_or_download_period(self, ticker: str) -> pd.DataFrame:
        """
       Returns cached data for the given ticker if available; otherwise, downloads it using period.

       Parameters:
       -----------
       ticker : str
           The ticker symbol for the data to be retrieved or downloaded.

       Returns:
       --------
       pd.DataFrame
           The DataFrame containing the cached or newly downloaded data.
       """

        # Filename consists of Ticker, today's date, period and interval separated by '_'
        filename = f'{ticker}_{datetime.today().date()}_{self.period}_{self.interval}.csv'
        filepath = os.path.join(self.data_path, filename)

        if os.path.isfile(filepath):
            return pd.read_csv(filepath, index_col='Date', parse_dates=True)
        else:
            return self.download_save_and_return_ticker(ticker, filepath, False)

    def download_ticker(self, ticker: str) -> pd.DataFrame:
        """
        Determines the appropriate method to fetch data based on the period attribute and returns the DataFrame.

        Parameters:
        -----------
        ticker : str
            The ticker symbol for the data to be downloaded.

        Returns:
        --------
        pd.DataFrame
            The DataFrame containing the data for the given ticker.
        """

        if self.period == 'not_passed':
            return self.return_cached_or_download_date(ticker=ticker)
        else:
            return self.return_cached_or_download_period(ticker=ticker)