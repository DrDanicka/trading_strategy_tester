import os.path
import unittest
import pandas as pd
from datetime import datetime


from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.trend.sma import sma
from trading_strategy_tester.trading_series.sma_series import SMA

class TestSMA(unittest.TestCase):

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

    def test_sma_close_length_9_offset_0_tradingview_data(self):
        """
        Test SMA with default length of 9 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use Close price to calculate SMA.
        """
        trading_view_sma = pd.Series([
            190.46, 190.23, 190.54, 190.65, 191.13, 191.79, 192.10, 192.69, 193.58, 194.35,
            195.25, 195.52, 196.04, 196.10, 195.99, 196.03, 195.85, 195.31, 194.81, 194.25
        ], name='SMA_9_0').reset_index(drop=True)
        calculated_sma = sma(self.data['Close'], 9, 0).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_sma, trading_view_sma)


    def test_sma_open_length_14_offset_2_tradingview_data(self):
        """
        Test SMA with default length of 14 days and offset 2.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use Open price to calculate SMA.
        """
        trading_view_sma = pd.Series([
            188.74, 189.23, 189.69, 189.98, 190.16, 190.63, 190.92, 191.21, 191.44, 191.56,
            191.81, 192.32, 192.87, 193.32, 193.69, 194.20, 194.61, 194.98, 195.22, 195.09
        ], name='SMA_14_2').reset_index(drop=True)
        calculated_sma = sma(self.data['Open'], 14, 2).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_sma, trading_view_sma)

    def test_sma_low_length_25_offset_5_tradingview_data(self):
        """
        Test SMA with default length of 25 days and offset 5.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use Low price to calculate SMA.
        """
        trading_view_sma = pd.Series([
            178.81, 179.46, 180.24, 180.94, 181.64, 182.58, 183.41, 184.26, 185.23, 186.17,
            186.89, 187.62, 188.24, 188.87, 189.46, 190.06, 190.50, 190.96, 191.31, 191.53
        ], name='SMA_25_5').reset_index(drop=True)
        calculated_sma = sma(self.data['Low'], 25, 5).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_sma, trading_view_sma)

    def test_sma_series_close_length_9_offset_0_tradingview_data(self):
        """
        Test SMA series with default length of 9 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use Close price to calculate SMA.
        """
        ticker = 'AAPL'

        trading_view_sma = pd.Series([
            190.46, 190.23, 190.54, 190.65, 191.13, 191.79, 192.10, 192.69, 193.58, 194.35,
            195.25, 195.52, 196.04, 196.10, 195.99, 196.03, 195.85, 195.31, 194.81, 194.25
        ], name=f'{ticker}_SMA_Close_9_0').reset_index(drop=True)
        sma_series = SMA(ticker, SourceType.CLOSE, 9, 0)
        calculated_sma = sma_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_sma, trading_view_sma)

if __name__ == '__main__':
    unittest.main()