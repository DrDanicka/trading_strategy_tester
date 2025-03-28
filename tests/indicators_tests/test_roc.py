import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.roc import roc
from trading_strategy_tester.trading_series.roc_series.roc_series import ROC

class TestROC(unittest.TestCase):

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

    def test_roc_close_length_9_tradingview_data(self):
        """
        Test ROC with the default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate ROC.
        """
        length = 9
        source = SourceType.CLOSE.value

        trading_view_roc = pd.Series([
            0.82, -1.06, 1.46, 0.53, 2.26, 3.12, 1.46, 2.82, 4.22, 3.59, 4.30,
            1.28, 2.40, 0.29, -0.53, 0.22, -0.85, -2.43, -2.29, -2.55
        ], name=f'ROC_{length}').reset_index(drop=True)
        calculate_roc = roc(self.data[source], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculate_roc, trading_view_roc)


    def test_roc_open_length_21_tradingview_data(self):
        """
        Test ROC with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Open price to calculate ROC.
        """
        length = 21
        source = SourceType.OPEN.value

        trading_view_roc = pd.Series([
            11.30, 8.24, 9.17, 10.24, 8.06, 6.50, 5.55, 4.95, 4.99, 5.50, 5.15,
            3.44, 3.11, 3.69, 2.45, 1.93, 1.44, 1.35, 2.30, 1.57
        ], name=f'ROC_{length}').reset_index(drop=True)
        calculate_roc = roc(self.data[source], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculate_roc, trading_view_roc)


    def test_roc_series_close_length_9_tradingview_data(self):
        """
        Test ROC series with the default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate ROC.
        """

        ticker = 'AAPL'
        length = 9
        source = SourceType.CLOSE

        trading_view_roc = pd.Series([
            0.82, -1.06, 1.46, 0.53, 2.26, 3.12, 1.46, 2.82, 4.22, 3.59, 4.30,
            1.28, 2.40, 0.29, -0.53, 0.22, -0.85, -2.43, -2.29, -2.55
        ], name=f'{ticker}_ROC_{source.value}_{length}').reset_index(drop=True)
        roc_series = ROC(ticker, source, length)
        calculate_roc = roc_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculate_roc, trading_view_roc)


if __name__ == '__main__':
    unittest.main()