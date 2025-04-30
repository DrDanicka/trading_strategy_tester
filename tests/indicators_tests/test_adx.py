import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.indicators.trend.adx import adx
from trading_strategy_tester.trading_series.adx_series.adx_series import ADX
from trading_strategy_tester.enums.source_enum import SourceType


class TestADX(unittest.TestCase):

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

    def test_adx_smoothing_14_length_14_tradingview_data(self):
        """
        Test ADX with smoothing length of 14 and DI length of 14.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places.
        """
        adx_smoothing = 14
        length = 14

        trading_view_adx = pd.Series([
            31.89, 31.35, 31.97, 32.61, 33.26, 34.09, 33.66, 33.59, 34.27, 35.21,
            36.09, 35.58, 35.20, 34.34, 32.93, 31.39, 29.89, 27.78, 26.24, 24.53
        ], name=f'ADX_{adx_smoothing}_{length}').reset_index(drop=True)
        calculated_adx = adx(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            adx_smoothing,
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_adx, trading_view_adx)

    def test_adx_smoothing_9_length_21_tradingview_data(self):
        """
        Test ADX with smoothing length of 9 and DI length of 21.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places.
        """
        adx_smoothing = 9
        length = 21

        trading_view_adx = pd.Series([
            24.48, 24.03, 24.83, 25.64, 26.42, 27.36, 27.08, 27.17, 28.08, 29.26,
            30.31, 29.96, 29.73, 29.02, 27.78, 26.44, 25.17, 23.26, 21.98, 20.21
        ], name=f'ADX_{adx_smoothing}_{length}').reset_index(drop=True)
        calculated_adx = adx(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.CLOSE.value],
            adx_smoothing,
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_adx, trading_view_adx)


    def test_adx_smoothing_1_length_9_tradingview_data(self):
        """
        Test ADX with smoothing length of 1 and DI length of 9.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places.
        """
        adx_smoothing = 1
        length = 9

        trading_view_adx = pd.Series([
            44.50, 20.65, 45.42, 46.96, 48.06, 52.62, 24.64, 32.28, 48.06, 54.02,
            54.02, 24.83, 26.74, 15.76, 3.13, 1.67, 3.02, 18.57, 5.84, 18.12
        ], name=f'ADX_{adx_smoothing}_{length}').reset_index(drop=True)
        calculated_adx = adx(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value], self.data[SourceType.CLOSE.value],
            adx_smoothing,
            length).tail(20).reset_index(
            drop=True).round(2)
        pd.testing.assert_series_equal(calculated_adx, trading_view_adx)

    def test_adx_series_smoothing_14_length_14_tradingview_data(self):
        """
        Test ADX series with smoothing length of 14 and DI length of 14.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places.
        """
        ticker = 'AAPL'
        adx_smoothing = 14
        length = 14

        trading_view_adx = pd.Series([
            31.89, 31.35, 31.97, 32.61, 33.26, 34.09, 33.66, 33.59, 34.27, 35.21,
            36.09, 35.58, 35.20, 34.34, 32.93, 31.39, 29.89, 27.78, 26.24, 24.53
        ], name=f'{ticker}_ADX_{adx_smoothing}_{length}').reset_index(drop=True)
        adx_series = ADX(ticker, adx_smoothing, length)
        calculated_adx = adx_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_adx, trading_view_adx)


if __name__ == '__main__':
    unittest.main()