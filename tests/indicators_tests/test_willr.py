import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.willr import willr
from trading_strategy_tester.trading_series.willr_series.willr_series import WILLR
from trading_strategy_tester.utils.sources import get_source_series


class TesWILLR(unittest.TestCase):

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


    def test_willr_close_length_14_tradingview_data(self):
        """
        Test WillR with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate WillR.
        """

        length = 14
        source_type = SourceType.CLOSE

        trading_view_willr = pd.Series([
            -19.38, -52.79, -14.1, -33.38, -9.67, -3.28, -32.9, -14.99, -0.38, -12.41, -16.84, -30.65, -22.02, -39.36,
            -40.59, -63.77, -80.12, -75.85, -70.81, -83.12
        ], name=f'WILLR_{length}').reset_index(drop=True)
        calculated_willr = willr(
            source=get_source_series(self.data, source_type),
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_willr, trading_view_willr)


    def test_willr_hlc3_length_21_tradingview_data(self):
        """
        Test WillR with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HLC3 price to calculate WillR.
        """

        length = 21
        source_type = SourceType.HLC3

        trading_view_willr = pd.Series([
            -11.51, -20.19, -9.53, -10.75, -5.32, -6.11, -26.43, -19.3, -9.09, -13.61, -16.13, -32.73, -24.87, -31.55,
            -37.25, -46.23, -52.29, -57.85, -47.8, -55.33
        ], name=f'WILLR_{length}').reset_index(drop=True)
        calculated_willr = willr(
            source=get_source_series(self.data, source_type),
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_willr, trading_view_willr)


    def test_willr_series_close_length_14_tradingview_data(self):
        """
        Test WillR series with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate WillR.
        """

        ticker = 'AAPL'
        length = 14
        source_type = SourceType.CLOSE

        trading_view_willr = pd.Series([
            -19.38, -52.79, -14.1, -33.38, -9.67, -3.28, -32.9, -14.99, -0.38, -12.41, -16.84, -30.65, -22.02, -39.36,
            -40.59, -63.77, -80.12, -75.85, -70.81, -83.12
        ], name=f'{ticker}_WILLR_{source_type.value}_{length}').reset_index(drop=True)
        willr_series = WILLR(ticker, source_type, length)
        calculated_willr = willr_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_willr, trading_view_willr)


    def test_willr_series_hlc3_length_21_tradingview_data(self):
        """
        Test WillR series with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HLC3 price to calculate WillR.
        """

        ticker = 'AAPL'
        length = 21
        source_type = SourceType.HLC3

        trading_view_willr = pd.Series([
            -11.51, -20.19, -9.53, -10.75, -5.32, -6.11, -26.43, -19.3, -9.09, -13.61, -16.13, -32.73, -24.87, -31.55,
            -37.25, -46.23, -52.29, -57.85, -47.8, -55.33
        ], name=f'{ticker}_WILLR_{source_type.value}_{length}').reset_index(drop=True)
        willr_series = WILLR(ticker, source_type, length)
        calculated_willr = willr_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_willr, trading_view_willr)


if __name__ == '__main__':
    unittest.main()