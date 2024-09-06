import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.dmi import di_plus, di_minus
from trading_strategy_tester.trading_series.di_plus_series import DI_PLUS
from trading_strategy_tester.trading_series.di_minus_series import DI_MINUS


class TestDMI(unittest.TestCase):

    def setUp(self):
        """
        Testing on AAPL stock from 2020-1-1 until 2024-1-1
        """
        # Create a sample series to test
        self.data = pd.read_csv(os.path.join('..', 'testing_data', 'AAPL_testing_data.csv'))
        # Create downloader for series testing
        self.downloader = DownloadModule(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2024, 1, 1)
        )

    def test_di_plus_length_14_tradingview_data(self):
        """
        Test DI+ with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 14

        trading_view_di_plus = pd.Series([
            33.16, 29.83, 37.00, 35.44, 33.65, 34.18, 30.57, 31.34, 36.82, 37.65,
            36.33, 33.47, 33.38, 30.91, 28.11, 26.35, 25.61, 23.94, 26.16, 24.22
        ], name=f'DIPLUS_{length}').reset_index(drop=True)
        calculated_di_plus = di_plus(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            di_length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_di_plus, trading_view_di_plus)


    def test_di_plus_length_9_tradingview_data(self):
        """
        Test DI+ with the default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 9

        trading_view_di_plus = pd.Series([
            33.42, 27.98, 39.52, 36.82, 33.87, 34.69, 29.04, 30.40, 38.92, 39.92,
            37.74, 33.12, 32.99, 29.12, 24.98, 22.52, 21.49, 19.24, 23.20, 20.41
        ], name=f'DIPLUS_{length}').reset_index(drop=True)
        calculated_di_plus = di_plus(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            di_length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_di_plus, trading_view_di_plus)


    def test_di_minus_length_14_tradingview_data(self):
        """
        Test DI- with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 14

        trading_view_di_minus = pd.Series([
            14.92, 18.15, 15.89, 14.83, 13.83, 13.01, 17.18, 15.91, 14.63, 13.42,
            12.95, 18.4, 17.89, 19.31, 20.93, 20.98, 20.76, 24.1, 23.09, 25.38
        ], name=f'DIMINUS_{length}').reset_index(drop=True)
        calculated_di_minus = di_minus(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            di_length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_di_minus, trading_view_di_minus)


    def test_di_minus_length_21_tradingview_data(self):
        """
        Test DI- with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 21

        trading_view_di_minus = pd.Series([
            17.45, 19.34, 17.78, 17.01, 16.26, 15.63, 18.19, 17.31, 16.39, 15.49,
            15.13, 18.6, 18.27, 19.18, 20.24, 20.3, 20.17, 22.35, 21.75, 23.27
        ], name=f'DIMINUS_{length}').reset_index(drop=True)
        calculated_di_minus = di_minus(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            di_length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_di_minus, trading_view_di_minus)

    def test_di_plus_series_length_14_tradingview_data(self):
        """
        Test DI+ series with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 14

        trading_view_di_plus = pd.Series([
            33.16, 29.83, 37.00, 35.44, 33.65, 34.18, 30.57, 31.34, 36.82, 37.65,
            36.33, 33.47, 33.38, 30.91, 28.11, 26.35, 25.61, 23.94, 26.16, 24.22
        ], name=f'{ticker}_DIPLUS_{length}').reset_index(drop=True)
        di_plus_series = DI_PLUS(ticker, length)
        calculated_di_plus = di_plus_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_di_plus, trading_view_di_plus)

    def test_di_minus_series_length_14_tradingview_data(self):
        """
        Test DI- series with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 14

        trading_view_di_minus = pd.Series([
            14.92, 18.15, 15.89, 14.83, 13.83, 13.01, 17.18, 15.91, 14.63, 13.42,
            12.95, 18.4, 17.89, 19.31, 20.93, 20.98, 20.76, 24.1, 23.09, 25.38
        ], name=f'{ticker}_DIMINUS_{length}').reset_index(drop=True)
        di_minus_series = DI_MINUS(ticker, length)
        calculated_di_minus = di_minus_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_di_minus, trading_view_di_minus)


if __name__ == '__main__':
    unittest.main()