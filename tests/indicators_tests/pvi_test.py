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
        self.data = pd.read_csv(os.path.join('..', 'testing_data', 'AAPL_testing_data.csv'))
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
            92726425.21, 92315760.34, 93719168.95, 93485489.42, 93966881.72, 94362534.37, 93574693.12, 93992060.34,
            95167211.29, 95217849.46, 94868257.03, 94394178.83, 94612413.19, 94052687.7, 94016898.54, 93810959.94,
            93728802.39, 93753709.56, 93829514.52, 93598290.37
        ], name='PVI').reset_index(drop=True)
        calculated_pvi = pvi(
            close=self.data[SourceType.CLOSE.value],
            volume=self.data['Volume']
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
            92726425.21, 92315760.34, 93719168.95, 93485489.42, 93966881.72, 94362534.37, 93574693.12, 93992060.34,
            95167211.29, 95217849.46, 94868257.03, 94394178.83, 94612413.19, 94052687.7, 94016898.54, 93810959.94,
            93728802.39, 93753709.56, 93829514.52, 93598290.37
        ], name=f'{ticker}_PVI').reset_index(drop=True)
        pvi_series = PVI(ticker)
        calculated_pvi = pvi_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_pvi, trading_view_pvi)