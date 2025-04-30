import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.momentum import momentum
from trading_strategy_tester.trading_series.momentum_series.momentum_series import MOMENTUM
from trading_strategy_tester.utils.sources import get_source_series


class TestMomentum(unittest.TestCase):

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


    def test_momentum_close_length_10_tradingview_data(self):
        """
        Test Momentum with the default length of 10 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Momentum.
        """

        source = SourceType.CLOSE
        length = 10

        trading_view_momentum = pd.Series([
            1.53, -0.26, 1.97, 1.68, 2.96, 5.74, 3.39, 4.31, 8.59, 8.16, 6.33, 6.46, 3.52, 2.51, 0.41, -2.11, -0.13,
            -1.56, -4.38, -5.58
        ], name=f'MOMENTUM_{length}').reset_index(drop=True)
        calculated_momentum = momentum(
            series=get_source_series(self.data, source),
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_momentum, trading_view_momentum)


    def test_momentum_hlc3_length_18_tradingview_data(self):
        """
        Test Momentum with the default length of 18 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HLC3 price to calculate Momentum.
        """

        source = SourceType.HLC3
        length = 18

        trading_view_momentum = pd.Series([
            12.39, 7.9, 10.02, 10.28, 8.79, 10.11, 5.41, 5.29, 7.16, 8.42, 6.58, 5.0, 4.9, 5.74, 5.3, 3.7, 3.11, 3.09,
            3.13, 3.91
        ], name=f'MOMENTUM_{length}').reset_index(drop=True)
        calculated_momentum = momentum(
            series=get_source_series(self.data, source),
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_momentum, trading_view_momentum)


    def test_momentum_series_close_length_10_tradingview_data(self):
        """
        Test Momentum series with the default length of 10 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Momentum.
        """

        ticker = 'AAPL'
        source = SourceType.CLOSE
        length = 10

        trading_view_momentum = pd.Series([
            1.53, -0.26, 1.97, 1.68, 2.96, 5.74, 3.39, 4.31, 8.59, 8.16, 6.33, 6.46, 3.52, 2.51, 0.41, -2.11, -0.13,
            -1.56, -4.38, -5.58
        ], name=f'{ticker}_MOMENTUM_{source.value}_{length}').reset_index(drop=True)
        momentum_series = MOMENTUM(ticker, source, length)
        calculated_momentum = momentum_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_momentum, trading_view_momentum)


    def test_momentum_series_hlc3_length_18_tradingview_data(self):
        """
        Test Momentum series with the default length of 18 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Momentum.
        """

        ticker = 'AAPL'
        source = SourceType.HLC3
        length = 18

        trading_view_momentum = pd.Series([
            12.39, 7.9, 10.02, 10.28, 8.79, 10.11, 5.41, 5.29, 7.16, 8.42, 6.58, 5.0, 4.9, 5.74, 5.3, 3.7, 3.11, 3.09,
            3.13, 3.91
        ], name=f'{ticker}_MOMENTUM_{source.value}_{length}').reset_index(drop=True)
        momentum_series = MOMENTUM(ticker, source, length)
        calculated_momentum = momentum_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_momentum, trading_view_momentum)


if __name__ == '__main__':
    unittest.main()