import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.uo import uo
from trading_strategy_tester.trading_series.uo_series.uo_series import UO


class TestUO(unittest.TestCase):

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

    def test_uo_fast_7_middle_14_slow_28_tradingview_data(self):
        """
        Test UO with fast length of 7 middle length of 14 and slow length of 28.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        fast_length = 7
        middle_length = 14
        slow_length = 28

        trading_view_uo = pd.Series([
            51.81, 54.08, 59.91, 56.17, 57.58, 63.9, 59.08, 61.49, 66.82, 64.31, 67.29, 64.57, 65.55, 61.31, 53.17,
            45.79, 41.37, 47.13, 44.82, 40.59
        ], name=f'UO_{fast_length}_{middle_length}_{slow_length}').reset_index(drop=True)
        calculated_uo = uo(
            close=self.data[SourceType.CLOSE.value],
            low=self.data[SourceType.LOW.value],
            high=self.data[SourceType.HIGH.value],
            fast_length=fast_length,
            middle_length=middle_length,
            slow_length=slow_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_uo, trading_view_uo)

    def test_uo_fast_4_middle_12_slow_25_tradingview_data(self):
        """
        Test UO with fast length of 4 middle length of 12 and slow length of 25.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        fast_length = 4
        middle_length = 12
        slow_length = 25

        trading_view_uo = pd.Series([
            56.35, 55.77, 68.24, 58.41, 57.07, 61.82, 52.91, 66.48, 71.56, 67.37, 72.88, 63.51, 58.81, 46.34, 43.59,
            40.36, 34.75, 47.71, 48.89, 47.38
        ], name=f'UO_{fast_length}_{middle_length}_{slow_length}').reset_index(drop=True)
        calculated_uo = uo(
            close=self.data[SourceType.CLOSE.value],
            low=self.data[SourceType.LOW.value],
            high=self.data[SourceType.HIGH.value],
            fast_length=fast_length,
            middle_length=middle_length,
            slow_length=slow_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_uo, trading_view_uo)


    def test_uo_series_fast_7_middle_14_slow_28_tradingview_data(self):
        """
        Test UO series with fast length of 7 middle length of 14 and slow length of 28.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        fast_length = 7
        middle_length = 14
        slow_length = 28

        trading_view_uo = pd.Series([
            51.81, 54.08, 59.91, 56.17, 57.58, 63.9, 59.08, 61.49, 66.82, 64.31, 67.29, 64.57, 65.55, 61.31, 53.17,
            45.79, 41.37, 47.13, 44.82, 40.59
        ], name=f'{ticker}_UO_{fast_length}_{middle_length}_{slow_length}').reset_index(drop=True)
        uo_series =UO(
            ticker=ticker,
            fast_length=fast_length,
            middle_length=middle_length,
            slow_length=slow_length
        )
        calculated_uo = uo_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_uo, trading_view_uo)


if __name__ == '__main__':
    unittest.main()