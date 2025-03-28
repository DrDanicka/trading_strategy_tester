import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.indicators.volume.cmf import cmf
from trading_strategy_tester.trading_series.cmf_series.cmf_series import CMF
from trading_strategy_tester.enums.source_enum import SourceType


class TestCMF(unittest.TestCase):

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

    def test_cmf_length_20_tradingview_data(self):
        """
        Test CMF with the default length of 20 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 20

        trading_view_cmf = pd.Series([
            0.23, 0.19, 0.17, 0.09, 0.07, 0.14, 0.12, 0.19, 0.25, 0.29,
            0.25, 0.26, 0.27, 0.22, 0.22, 0.21, 0.19, 0.22, 0.23, 0.19
        ], name=f'CMF_{length}').reset_index(drop=True)
        calculated_cmf = cmf(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            self.data[SourceType.VOLUME.value],
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cmf, trading_view_cmf)

    def test_cmf_length_10_tradingview_data(self):
        """
        Test CMF with the default length of 10 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 10

        trading_view_cmf = pd.Series([
            0.13, 0.16, 0.17, 0.09, 0.14, 0.22, 0.30, 0.38, 0.55, 0.49,
            0.33, 0.32, 0.34, 0.31, 0.29, 0.20, 0.11, 0.08, -0.08, -0.13
        ], name=f'CMF_{length}').reset_index(drop=True)
        calculated_cmf = cmf(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            self.data[SourceType.VOLUME.value],
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cmf, trading_view_cmf)

    def test_cmf_series_length_20_tradingview_data(self):
        """
        Test CMF series with default length of 20 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        ticker = 'AAPL'
        length = 20

        trading_view_cmf = pd.Series([
            0.23, 0.19, 0.17, 0.09, 0.07, 0.14, 0.12, 0.19, 0.25, 0.29,
            0.25, 0.26, 0.27, 0.22, 0.22, 0.21, 0.19, 0.22, 0.23, 0.19
        ], name=f'{ticker}_CMF_{length}').reset_index(drop=True)
        cmf_series = CMF(ticker, length)
        calculated_cmf = cmf_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cmf, trading_view_cmf)



if __name__ == '__main__':
    unittest.main()