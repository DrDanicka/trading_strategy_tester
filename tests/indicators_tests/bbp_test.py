import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.bbp import bbp
from trading_strategy_tester.trading_series.bbp_series import BBP

class TestBBP(unittest.TestCase):

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

    def test_bbp_length_13_tradingview_data(self):
        """
        Test BBP with the default length of 13 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 13

        trading_view_bbp = pd.Series([
            3.28, -0.2, 5.57, 7.06, 7.53, 7.12, 1.82, 2.45, 7.16, 8.58, 7.07, 2.19,
            3.29, 2.95, 1.05, -0.82, -2.04, -3.82, -0.4, -1.65
        ], name=f'BBP_{length}').reset_index(drop=True)
        calculated_bbp = bbp(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bbp, trading_view_bbp)


    def test_bbp_length_21_tradingview_data(self):
        """
        Test BBP with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 21

        trading_view_bbp = pd.Series([
            7.53, 3.73, 9.62, 11.03, 11.6, 11.36, 5.87, 6.46, 11.42, 13.01, 11.5,
            6.41, 7.38, 6.67, 4.42, 2.13, 0.48, -1.66, 1.5, -0.08
        ], name=f'BBP_{length}').reset_index(drop=True)
        calculated_bbp = bbp(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bbp, trading_view_bbp)


    def test_bbp_series_length_13_tradingview_data(self):
        """
        Test BBP series with the default length of 13 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 13

        trading_view_bbp = pd.Series([
            3.28, -0.2, 5.57, 7.06, 7.53, 7.12, 1.82, 2.45, 7.16, 8.58, 7.07, 2.19,
            3.29, 2.95, 1.05, -0.82, -2.04, -3.82, -0.4, -1.65
        ], name=f'{ticker}_BBP_{length}').reset_index(drop=True)
        bbp_series = BBP(ticker, length)
        calculated_bbp = bbp_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bbp, trading_view_bbp)


if __name__ == '__main__':
    unittest.main()