import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.stoch import percent_k, percent_d
from trading_strategy_tester.trading_series.stoch_series.percent_k_series import STOCH_PERCENT_K
from trading_strategy_tester.trading_series.stoch_series.percent_d_series import STOCH_PERCENT_D


class TestSTOCH(unittest.TestCase):

    def setUp(self):
        """
        Testing on AAPL stock from 2020-1-1 until 2024-1-1
        """
        # Create a sample series to test
        script_dir = os.path.dirname(__file__)
        self.data = pd.read_csv(os.path.join(script_dir, 'testing_data', 'AAPL_testing_data.csv'))
        # Create downloader for series testing
        self.downloader = DownloadModule(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2024, 1, 1)
        )


    def test_stoch_percent_k_length_14_tradingview_data(self):
        """
        Test %K with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 14

        trading_view_k_percent = pd.Series([
            80.62, 47.21, 85.9, 66.62, 90.33, 96.72, 67.1, 85.01, 99.62, 87.59, 83.16, 69.35, 77.98, 60.64, 59.41,
            36.23, 19.88, 24.15, 29.19, 16.88
        ], name=f'STOCH-PERCENT-K_{length}').reset_index(drop=True)
        calculated_k_percent = percent_k(
            close=self.data[SourceType.CLOSE.value],
            low=self.data[SourceType.LOW.value],
            high=self.data[SourceType.HIGH.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_k_percent, calculated_k_percent)

    def test_stoch_percent_k_length_21_tradingview_data(self):
        """
        Test %K with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 21

        trading_view_k_percent = pd.Series([
            91.37, 82.12, 94.61, 84.55, 94.56, 98.03, 77.45, 89.13, 99.66, 87.59, 83.16, 69.35, 77.98, 60.64, 59.41,
            50.53, 46.01, 46.84, 50.37, 41.74
        ], name=f'STOCH-PERCENT-K_{length}').reset_index(drop=True)
        calculated_k_percent = percent_k(
            close=self.data[SourceType.CLOSE.value],
            low=self.data[SourceType.LOW.value],
            high=self.data[SourceType.HIGH.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_k_percent, calculated_k_percent)


    def test_stoch_percent_d_length_14_smooth_3_tradingview_data(self):
        """
        Test %D with the default length of 14 days and smoothing length of 3 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 14
        d_smooth_length = 3

        trading_view_d_percent = pd.Series([
            72.3, 65.38, 71.24, 66.58, 80.95, 84.56, 84.72, 82.94, 83.91, 90.74, 90.12, 80.03, 76.83, 69.32, 66.01,
            52.09, 38.51, 26.75, 24.41, 23.41
        ], name=f'STOCH-PERCENT-D_{length}_{d_smooth_length}').reset_index(drop=True)
        calculated_d_percent = percent_d(
            close=self.data[SourceType.CLOSE.value],
            low=self.data[SourceType.LOW.value],
            high=self.data[SourceType.HIGH.value],
            length=length,
            d_smooth_length=d_smooth_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_d_percent, calculated_d_percent)


    def test_stoch_percent_d_length_21_smooth_3_tradingview_data(self):
        """
        Test %D with the default length of 21 days and smoothing length of 3 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 21
        d_smooth_length = 3

        trading_view_d_percent = pd.Series([
            88.03, 86.81, 89.37, 87.09, 91.24, 92.38, 90.01, 88.2, 88.75, 92.13, 90.14, 80.03, 76.83, 69.32, 66.01,
            56.86, 51.99, 47.8, 47.74, 46.32
        ], name=f'STOCH-PERCENT-D_{length}_{d_smooth_length}').reset_index(drop=True)
        calculated_d_percent = percent_d(
            close=self.data[SourceType.CLOSE.value],
            low=self.data[SourceType.LOW.value],
            high=self.data[SourceType.HIGH.value],
            length=length,
            d_smooth_length=d_smooth_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_d_percent, calculated_d_percent)


    def test_stoch_percent_d_length_18_smooth_5_tradingview_data(self):
        """
        Test %D with the default length of 18 days and smoothing length of 5 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 18
        d_smooth_length = 5

        trading_view_d_percent = pd.Series([
            85.04, 81.62, 82.65, 81.94, 84.15, 85.99, 85.59, 84.15, 88.41, 87.29, 84.5, 84.95, 83.54, 75.74, 70.11,
            63.58, 58.92, 52.69, 50.63, 43.73
        ], name=f'STOCH-PERCENT-D_{length}_{d_smooth_length}').reset_index(drop=True)
        calculated_d_percent = percent_d(
            close=self.data[SourceType.CLOSE.value],
            low=self.data[SourceType.LOW.value],
            high=self.data[SourceType.HIGH.value],
            length=length,
            d_smooth_length=d_smooth_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_d_percent, calculated_d_percent)


    def test_stoch_percent_k_series_length_14_tradingview_data(self):
        """
        Test %K series with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 14

        trading_view_k_percent = pd.Series([
            80.62, 47.21, 85.9, 66.62, 90.33, 96.72, 67.1, 85.01, 99.62, 87.59, 83.16, 69.35, 77.98, 60.64, 59.41,
            36.23, 19.88, 24.15, 29.19, 16.88
        ], name=f'{ticker}_STOCH-PERCENT-K_{length}').reset_index(drop=True)
        percent_k_series = STOCH_PERCENT_K(ticker, length)
        calculated_k_percent = percent_k_series.get_data(
            self.downloader, pd.DataFrame()
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_k_percent, calculated_k_percent)


    def test_stoch_percent_d_series_length_14_smooth_3_tradingview_data(self):
        """
        Test %D series with the default length of 14 days and smoothing length of 3 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 14
        d_smooth_length = 3

        trading_view_d_percent = pd.Series([
            72.3, 65.38, 71.24, 66.58, 80.95, 84.56, 84.72, 82.94, 83.91, 90.74, 90.12, 80.03, 76.83, 69.32, 66.01,
            52.09, 38.51, 26.75, 24.41, 23.41
        ], name=f'{ticker}_STOCH-PERCENT-D_{length}_{d_smooth_length}').reset_index(drop=True)
        percent_d_series = STOCH_PERCENT_D(ticker, length, d_smooth_length)
        calculated_d_percent = percent_d_series.get_data(
            self.downloader, pd.DataFrame()
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_d_percent, calculated_d_percent)


    def test_stoch_percent_d_series_length_18_smooth_5_tradingview_data(self):
        """
        Test %D series with the default length of 18 days and smoothing length of 5 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 18
        d_smooth_length = 5

        trading_view_d_percent = pd.Series([
            85.04, 81.62, 82.65, 81.94, 84.15, 85.99, 85.59, 84.15, 88.41, 87.29, 84.5, 84.95, 83.54, 75.74, 70.11,
            63.58, 58.92, 52.69, 50.63, 43.73
        ], name=f'{ticker}_STOCH-PERCENT-D_{length}_{d_smooth_length}').reset_index(drop=True)
        percent_d_series = STOCH_PERCENT_D(ticker, length, d_smooth_length)
        calculated_d_percent = percent_d_series.get_data(
            self.downloader, pd.DataFrame()
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_d_percent, calculated_d_percent)


if __name__ == '__main__':
    unittest.main()