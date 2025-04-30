import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volume.pvi import pvi
from trading_strategy_tester.trading_series.pvi_series.pvi_series import PVI

class TestPVI(unittest.TestCase):

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

    def test_pvi_tradingview_data(self):
        """
        Test PVI indicator.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        trading_view_pvi = pd.Series([
            -99498478.79, -99498478.79, -98095070.18, -98095070.18, -97613677.89, -97218025.23, -98005866.48,
            -98005866.48, -96830715.53, -96830715.53, -97180307.96, -97180307.96, -97180307.96, -97740033.46,
            -97740033.46, -97740033.46, -97740033.46, -97715126.28, -97715126.28, -97946350.43
        ], name='PVI').reset_index(drop=True)
        calculated_pvi = pvi(
            close=self.data[SourceType.CLOSE.value],
            volume=self.data[SourceType.VOLUME.value]
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_pvi, trading_view_pvi)


    def test_pvi_series_tradingview_data(self):
        """
        Test PVI indicator series.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'

        trading_view_pvi = pd.Series([
            -99498478.79, -99498478.79, -98095070.18, -98095070.18, -97613677.89, -97218025.23, -98005866.48,
            -98005866.48, -96830715.53, -96830715.53, -97180307.96, -97180307.96, -97180307.96, -97740033.46,
            -97740033.46, -97740033.46, -97740033.46, -97715126.28, -97715126.28, -97946350.43
        ], name=f'{ticker}_PVI').reset_index(drop=True)
        pvi_series = PVI(ticker)
        calculated_pvi = pvi_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_pvi, trading_view_pvi)


if __name__ == '__main__':
    unittest.main()