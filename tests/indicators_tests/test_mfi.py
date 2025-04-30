import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volume.mfi import mfi
from trading_strategy_tester.trading_series.mfi_series.mfi_series import MFI
from trading_strategy_tester.utils.sources import get_source_series


class TestMFI(unittest.TestCase):

    def setUp(self):
        """
        Testing on AAPL stock from 2020-1-1 until 2024-1-1
        """
        # Create a sample series to test
        script_dir = os.path.dirname(__file__)
        self.data = pd.read_csv(os.path.join(script_dir, 'testing_data', 'AAPL_testing_data.csv'))
        # Create downloader for series testing
        self.downloader = DownloadModule(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2024, 1, 1)
        )


    def test_mfi_length_14_tradingview_data(self):
        """
        Test MFI with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 14

        trading_view_mfi = pd.Series([
            54.01, 53.95, 54.55, 53.71, 53.27, 61.75, 52.94, 59.93, 61.86, 67.53, 59.91, 54.0, 59.06, 58.7, 53.17, 53.5,
            47.64, 42.09, 41.09, 34.73
        ], name=f'MFI_{length}').reset_index(drop=True)
        calculated_mfi = mfi(
            hlc3=get_source_series(self.data, SourceType.HLC3),
            volume=self.data[SourceType.VOLUME.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_mfi, calculated_mfi)

    def test_mfi_length_21_tradingview_data(self):
        """
        Test MFI with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 21

        trading_view_mfi = pd.Series([
            65.97, 60.84, 67.78, 67.21, 66.59, 66.83, 61.03, 60.61, 65.91, 66.25,
            56.74, 51.74, 55.93, 51.4, 50.97, 47.51, 47.29, 46.95, 46.77, 46.76
        ], name=f'MFI_{length}').reset_index(drop=True)
        calculated_mfi = mfi(
            hlc3=get_source_series(self.data, SourceType.HLC3),
            volume=self.data[SourceType.VOLUME.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_mfi, calculated_mfi)


    def test_mfi_series_length_14_tradingview_data(self):
        """
        Test MFI series with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 14

        trading_view_mfi = pd.Series([
            54.01, 53.95, 54.55, 53.71, 53.27, 61.75, 52.94, 59.93, 61.86, 67.53, 59.91, 54.0, 59.06, 58.7, 53.17, 53.5,
            47.64, 42.09, 41.09, 34.73
        ], name=f'{ticker}_MFI_{length}').reset_index(drop=True)
        mfi_series = MFI(ticker, length)
        calculated_mfi = mfi_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(trading_view_mfi, calculated_mfi)


if __name__ == '__main__':
    unittest.main()