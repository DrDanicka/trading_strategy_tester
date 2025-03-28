import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.cop import cop
from trading_strategy_tester.trading_series.coppock_series.coppock_series import COPPOCK

class TestCOPPOCK(unittest.TestCase):

    def setUp(self):
        """
        Testing on AAPL stock from 2020-1-1 until 2024-1-1
        """
        # Create a sample series to test
        self.data = pd.read_csv(os.path.join('testing_data', 'AAPL_testing_data.csv'))
        # Create downloader for series testing
        self.downloader = DownloadModule(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2024, 1, 1)
        )

    def test_coppock_length_10_long_roc_14_short_roc_11_tradingview_data(self):
        """
        Test COPPOCK with the default length of 10 days, long RoC length of 14 days and short RoC length of 11 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 10
        long_roc_length = 14
        short_roc_length = 11

        trading_view_coppock = pd.Series([
            8.44, 6.84, 6.03, 5.07, 4.63, 4.56, 4.08, 4.11, 4.68, 5.49, 6.09,
            6.11, 6.57, 6.12, 5.61, 4.92, 3.67, 2.85, 1.86, 0.41
        ], name=f'COPPOCK_{length}_{long_roc_length}_{short_roc_length}').reset_index(drop=True)
        calculated_coppock = cop(
            self.data[SourceType.CLOSE.value],
            length,
            long_roc_length,
            short_roc_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_coppock, trading_view_coppock)


    def test_coppock_length_15_long_roc_10_short_roc_20_tradingview_data(self):
        """
        Test COPPOCK with the default length of 15 days, long RoC length of 10 days and short RoC length of 20 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 15
        long_roc_length = 10
        short_roc_length = 20

        trading_view_coppock = pd.Series([
            13.80, 12.88, 12.26, 11.38, 10.72, 10.43, 9.57, 9.08, 8.99, 8.88, 8.54,
            8.20, 7.68, 7.09, 6.38, 5.60, 4.98,4.28, 3.58, 2.74
        ], name=f'COPPOCK_{length}_{long_roc_length}_{short_roc_length}').reset_index(drop=True)
        calculated_coppock = cop(
            self.data[SourceType.CLOSE.value],
            length,
            long_roc_length,
            short_roc_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_coppock, trading_view_coppock)


    def test_coppock_series_length_10_long_roc_14_short_roc_11_tradingview_data(self):
        """
        Test COPPOCK series with the default length of 10 days, long RoC length of 14 days and short RoC length of 11 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        ticker = 'AAPL'
        length = 10
        long_roc_length = 14
        short_roc_length = 11

        trading_view_coppock = pd.Series([
            8.44, 6.84, 6.03, 5.07, 4.63, 4.56, 4.08, 4.11, 4.68, 5.49, 6.09,
            6.11, 6.57, 6.12, 5.61, 4.92, 3.67, 2.85, 1.86, 0.41
        ], name=f'{ticker}_COPPOCK_{length}_{long_roc_length}_{short_roc_length}').reset_index(drop=True)
        coppock_series = COPPOCK(ticker, length, long_roc_length, short_roc_length)
        calculated_coppock = coppock_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_coppock, trading_view_coppock)



if __name__ == '__main__':
    unittest.main()