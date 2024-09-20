import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.indicators.volatility.atr import atr
from trading_strategy_tester.trading_series.atr_series.atr_series import ATR

class TestATR(unittest.TestCase):

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

    def test_atr_length_14_smoothing_RMA(self):
        """
        Test ATR with the default length of 14 days and RMA smoothing.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        trading_view_atr = pd.Series([
            2.61, 2.69, 2.85, 2.84, 2.83, 2.79, 2.90, 2.91, 2.93, 2.97,
            2.86, 2.88, 2.75, 2.76, 2.82, 2.79, 2.67, 2.65, 2.57, 2.57
        ], name='ATR_14_RMA').reset_index(drop=True)
        calculated_atr = atr(self.data['High'], self.data['Low'], self.data['Close'],
                             14, SmoothingType.RMA).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_atr, trading_view_atr)

    def test_atr_length_21_smoothing_SMA(self):
        """
        Test ATR with the default length of 21 days and SMA smoothing.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        trading_view_atr = pd.Series([
            2.61, 2.61, 2.64, 2.61, 2.58, 2.60, 2.69, 2.64, 2.69, 2.70,
            2.67, 2.68, 2.64, 2.67, 2.76, 2.76, 2.72, 2.75, 2.74, 2.72
        ], name='ATR_21_SMA').reset_index(drop=True)
        calculated_atr = atr(self.data['High'], self.data['Low'], self.data['Close'],
                             21, SmoothingType.SMA).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_atr, trading_view_atr)

    def test_atr_length_9_smoothing_EMA(self):
        """
        Test ATR with the default length of 9 days and EMA smoothing.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        trading_view_atr = pd.Series([
            2.29, 2.59, 3.06, 2.98, 2.92, 2.80, 3.10, 3.08, 3.12, 3.19,
            2.83, 2.90, 2.53, 2.60, 2.79, 2.72, 2.39, 2.39, 2.22, 2.31
        ], name='ATR_9_EMA').reset_index(drop=True)
        calculated_atr = atr(self.data['High'], self.data['Low'], self.data['Close'],
                             9, SmoothingType.EMA).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_atr, trading_view_atr)

    def test_atr_length_18_smoothing_WMA(self):
        """
        Test ATR with the default length of 18 days and WMA smoothing.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        trading_view_atr = pd.Series([
            2.28, 2.43, 2.69, 2.70, 2.70, 2.68, 2.86, 2.90, 2.97, 3.05,
            2.91, 2.96, 2.77, 2.79, 2.87, 2.82, 2.63, 2.59, 2.45, 2.44
        ], name='ATR_18_WMA').reset_index(drop=True)
        calculated_atr = atr(self.data['High'], self.data['Low'], self.data['Close'],
                             18, SmoothingType.WMA).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_atr, trading_view_atr)

    def test_atr_series_length_14_smoothing_RMA(self):
        """
        Test ATR series with the default length of 14 days and RMA smoothing.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        ticker = 'AAPL'

        trading_view_atr = pd.Series([
            2.61, 2.69, 2.85, 2.84, 2.83, 2.79, 2.90, 2.91, 2.93, 2.97,
            2.86, 2.88, 2.75, 2.76, 2.82, 2.79, 2.67, 2.65, 2.57, 2.57
        ], name=f'{ticker}_ATR_14_RMA').reset_index(drop=True)
        atr_series = ATR(ticker, 14, SmoothingType.RMA)
        calculated_atr = atr_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_atr, trading_view_atr)


if __name__ == '__main__':
    unittest.main()