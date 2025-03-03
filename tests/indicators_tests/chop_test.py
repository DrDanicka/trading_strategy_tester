import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.indicators.volatility.chop import chop
from trading_strategy_tester.trading_series.chop_series.chop_series import CHOP
from trading_strategy_tester.enums.source_enum import SourceType


class TestCHOP(unittest.TestCase):

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

    def test_chop_length_14_offset_0_tradingview_data(self):
        """
        Test CHOP with the default length of 14 days and offset of 0 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 14
        offset = 0

        trading_view_chop = pd.Series([
            48.91, 61.16, 61.21, 59.93, 58.42, 54.30, 56.43, 57.63, 50.58, 46.46,
            46.13, 47.48, 45.61, 46.27, 47.40, 55.81, 57.36, 55.62, 54.40, 54.77
        ], name=f'CHOP_{length}_{offset}').reset_index(drop=True)
        calculated_chop = chop(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_chop, trading_view_chop)

    def test_chop_length_18_offset_1_tradingview_data(self):
        """
        Test CHOP with the default length of 18 days and offset of 1 day.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 18
        offset = 1

        trading_view_chop = pd.Series([
            33.78, 39.32, 46.77, 45.52, 49.73, 50.01, 53.83, 58.93, 59.62, 52.55,
            48.77, 48.20, 49.17, 48.32, 48.87, 50.10, 50.60, 49.22, 49.41, 48.85
        ], name=f'CHOP_{length}_{offset}').reset_index(drop=True)
        calculated_chop = chop(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_chop, trading_view_chop)

    def test_chop_length_21_offset_2_tradingview_data(self):
        """
        Test CHOP with the default length of 21 days and offset of 2 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 21
        offset = 2

        trading_view_chop = pd.Series([
            27.26, 29.81, 33.77, 33.76, 36.63, 40.94, 45.83, 44.27, 49.69, 50.85,
            51.72, 50.51, 50.13, 50.26, 49.82, 50.19, 51.23, 51.32, 50.75, 51.11
        ], name=f'CHOP_{length}_{offset}').reset_index(drop=True)
        calculated_chop = chop(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_chop, trading_view_chop)

    def test_chop_series_length_14_offset_0_tradingview_data(self):
        """
        Test CHOP Series with the default length of 14 days and offset of 0 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        ticker = 'AAPL'
        length = 14
        offset = 0

        trading_view_chop = pd.Series([
            48.91, 61.16, 61.21, 59.93, 58.42, 54.30, 56.43, 57.63, 50.58, 46.46,
            46.13, 47.48, 45.61, 46.27, 47.40, 55.81, 57.36, 55.62, 54.40, 54.77
        ], name=f'{ticker}_CHOP_{length}_{offset}').reset_index(drop=True)
        chop_series = CHOP(ticker,  length,offset)
        calculated_chop = chop_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_chop, trading_view_chop)


if __name__ == '__main__':
    unittest.main()
