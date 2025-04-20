import os
import pandas as pd
import yfinance as yf
from datetime import datetime

from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.enums.source_enum import SourceType


class DownloadModule:
    """
    A module for downloading and caching financial data from Yahoo Finance.

    Methods:
    --------
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
                 start_date: datetime = datetime(2024, 1, 1),
                 end_date: datetime = datetime.today(),
                 interval: Interval = Interval.ONE_DAY,
                 period: Period = Period.NOT_PASSED):
        """
        Initializes the DownloadModule with the given parameters.

        :param start_date: The start date for the data download.
        :type start_date: datetime
        :param end_date: The end date for the data download.
        :type end_date: datetime
        :param interval: The interval between data points.
        :type interval: Interval
        :param period: The period over which to fetch data.
        :type period: Period
        """

        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval.value  # String value representing the interval
        self.period = period.value  # String value representing the period

        script_dir = os.path.dirname(__file__)
        self.data_path = os.path.join(script_dir, '..' ,'_data')

        # Create the data directory if it does not exist
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)

    def download_save_and_return_ticker(self, ticker: str, filepath: str, datetime_type: bool) -> pd.DataFrame:
        """
        Downloads data for a given ticker and saves it to a CSV file. Returns the data as a DataFrame.

        :param ticker: The ticker symbol for the data to be downloaded.
        :type ticker: str
        :param filepath: The file path where the data should be saved.
        :type filepath: str
        :param datetime_type: If True, uses start_date and end_date for downloading; otherwise, uses period.
        :type datetime_type: bool
        :return: The DataFrame containing the downloaded data.
        :rtype: pd.DataFrame

        :raise ValueError: If no data is found for the given ticker.
        """

        if datetime_type:
            df = yf.download(ticker, interval=self.interval, start=self.start_date, end=self.end_date, auto_adjust=False, progress=False)
        else:
            df = yf.download(ticker, interval=self.interval, period=self.period, auto_adjust=False, progress=False)

        if len(df) == 0:
            self.delete_temp_files()
            raise ValueError(f"No data found for ticker '{ticker}'. Please check the ticker symbol or the date range or other parameters.")

        # Automatically change columns to ensure robustness against future changes of API
        df.columns = [
            'Adj Close',
            SourceType.CLOSE.value,
            SourceType.HIGH.value,
            SourceType.LOW.value,
            SourceType.OPEN.value,
            SourceType.VOLUME.value
        ]

        df.to_csv(filepath)
        return df

    def return_cached_or_download_date(self, ticker: str) -> pd.DataFrame:
        """
        Returns cached data for the given ticker if available; otherwise, downloads it using a date range.

        :param ticker: The ticker symbol for the data to be retrieved or downloaded.
        :type ticker: str
        :return: The DataFrame containing the cached or newly downloaded data.
        :rtype: pd.DataFrame
        """

        filename = f'{ticker}_{self.start_date.date()}_{self.end_date.date()}_{self.interval}.csv'
        filepath = os.path.join(self.data_path, filename)

        if os.path.isfile(filepath):
            return pd.read_csv(filepath, index_col='Date', parse_dates=True)
        else:
            return self.download_save_and_return_ticker(ticker, filepath, True)

    def return_cached_or_download_period(self, ticker: str) -> pd.DataFrame:
        """
       Returns cached data for the given ticker if available; otherwise, downloads it using period.

       :param ticker: The ticker symbol for the data to be retrieved or downloaded.
       :type ticker: str
       :return: The DataFrame containing the cached or newly downloaded data.
       :rtype: pd.DataFrame
       """

        filename = f'{ticker}_{datetime.today().date()}_{self.period}_{self.interval}.csv'
        filepath = os.path.join(self.data_path, filename)

        if os.path.isfile(filepath):
            return pd.read_csv(filepath, index_col='Date', parse_dates=True)
        else:
            return self.download_save_and_return_ticker(ticker, filepath, False)

    def download_ticker(self, ticker: str) -> pd.DataFrame:
        """
        Determines the appropriate method to fetch data based on the period attribute and returns the DataFrame.

        :param ticker: The ticker symbol for the data to be downloaded.
        :type ticker: str
        :return: The DataFrame containing the data for the given ticker.
        :rtype: pd.DataFrame
        """

        if self.period == 'not_passed':
            return self.return_cached_or_download_date(ticker=ticker)
        else:
            return self.return_cached_or_download_period(ticker=ticker)

    def delete_temp_files(self):
        """
        Deletes all files in the directory specified by self.data_path.

        :raises FileNotFoundError: If self.data_path does not exist.
        :raises IsADirectoryError: If self.data_path is not a directory.
        """

        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"The directory '{self.data_path}' does not exist.")

        if not os.path.isdir(self.data_path):
            raise IsADirectoryError(f"The path '{self.data_path}' is not a directory.")

        for filename in os.listdir(self.data_path):
            file_path = os.path.join(self.data_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
