import unittest
import pandas as pd
from trading_strategy_tester.indicators.rsi import rsi

class TestRSI(unittest.TestCase):

    def setUp(self):
        """
        Testing on AAPL stock from 2020-1-1 until 2024-1-1
        """
        # Create a sample series to test
        self.data = pd.read_csv('AAPL_testing_data.csv')

    def test_rsi_close_length_14_tradingview_data(self):
        """
        Test RSI with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate RSI.
        """
        trading_view_rsi = pd.Series([
            67.43, 60.92, 68.21, 64.63, 67.85, 70.02, 62.09, 64.70, 69.49, 69.69,
            67.93, 62.61, 64.48, 58.18, 57.75, 54.61, 53.03, 53.29, 54.48, 51.06
        ], name='RSI_14').reset_index(drop=True)
        calculated_rsi = rsi(self.data['Close'], 14).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_rsi, trading_view_rsi)


    def test_rsi_open_length_9_tradingview_data(self):
        """
        Test RSI with the default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Open price to calculate RSI.
        """
        trading_view_rsi = pd.Series([
            67.41, 64.63, 65.68, 78.72, 72.71, 74.25, 66.22, 66.00, 72.83, 79.57,
            76.02, 66.26, 66.50, 69.06, 63.18, 56.90, 47.79, 42.35, 51.50, 50.20
        ], name = 'RSI_9').reset_index(drop=True)
        calculated_rsi = rsi(self.data['Open'], 9).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_rsi, trading_view_rsi)

    def test_rsi_high_length_21_tradingview_data(self):
        """
        Test RSI with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate RSI.
        """
        trading_view_rsi = pd.Series([
            62.81, 59.56, 65.04, 65.44, 65.72, 66.88, 61.38, 62.95, 66.75, 68.42,
            65.80, 62.17, 62.56, 63.47, 62.17, 58.66, 55.65, 54.90, 56.74, 56.20
        ], name = 'RSI_21').reset_index(drop=True)
        calculated_rsi = rsi(self.data['High'], 21).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_rsi, trading_view_rsi)

if __name__ == '__main__':
    unittest.main()