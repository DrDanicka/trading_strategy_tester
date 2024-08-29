import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.indicators.cmo import cmo
from trading_strategy_tester.trading_series.cmo_series import CMO

class TestCMO(unittest.TestCase):

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

    def test_cmo_close_length_9_tradingview_data(self):
        """
        Test CMO with default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate CMO.
        """
        trading_view_cmo = pd.Series([
            18.74, -24.28, 24.17, 8.47, 34.29, 42.90, 17.68, 32.92, 42.40, 38.70,
            49.39, 17.43, 32.72, 3.92, -7.93, 3.64, -15.72, -64.91, -58.91, -61.46
        ], name='CMO_9').reset_index(drop=True)
        calculated_cmo = cmo(self.data['Close'], 9).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cmo, trading_view_cmo)

    def test_cmo_high_length_12_tradingview_data(self):
        """
        Test CMO with default length of 12 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate CMO.
        """
        trading_view_cmo = pd.Series([
            25.65, 4.05, 20.90, 26.97, 20.67, 28.75, 3.37, 24.12, 38.80, 42.49, 31.07,
            31.07, 27.80, 41.00, 18.04, 4.02, -6.36, -14.78, 7.54, -2.20
        ], name='CMO_12').reset_index(drop=True)
        calculated_cmo = cmo(self.data['High'], 12).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cmo, trading_view_cmo)

    def test_cmo_open_length_21_tradingview_data(self):
        """
        Test CMO with default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Open price to calculate CMO.
        """
        trading_view_cmo = pd.Series([
            68.67, 60.30, 69.65, 72.19, 62.69, 57.95, 48.49, 45.66, 46.10, 48.77,
            45.02, 30.73, 28.68, 33.40, 23.14, 17.48, 12.42, 11.56, 18.37, 13.12
        ], name='CMO_21').reset_index(drop=True)
        calculated_cmo = cmo(self.data['Open'], 21).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cmo, trading_view_cmo)

    def test_cmo_series_close_length_9_tradingview_data(self):
        """
        Test CMO series with default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate CMO.
        """
        ticker = 'AAPL'

        trading_view_cmo = pd.Series([
            18.74, -24.28, 24.17, 8.47, 34.29, 42.90, 17.68, 32.92, 42.40, 38.70,
            49.39, 17.43, 32.72, 3.92, -7.93, 3.64, -15.72, -64.91, -58.91, -61.46
        ], name=f'{ticker}_CMO_Close_9').reset_index(drop=True)
        cmo_series = CMO(ticker, 'Close', 9)
        calculated_cmo = cmo_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cmo, trading_view_cmo)

if __name__ == '__main__':
    unittest.main()