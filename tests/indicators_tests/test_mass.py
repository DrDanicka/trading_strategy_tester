import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.trend.mass import mass_index
from trading_strategy_tester.trading_series.mass_series.mass_series import MASS_INDEX


class TestMASS(unittest.TestCase):

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


    def test_mass_index_length_10_tradingview_data(self):
        """
        Test MASS INDEX with the default length of 10 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places
        """

        length = 10

        trading_view_mass = pd.Series([
            9.16, 9.33, 9.63, 9.88, 10.01, 10.14, 10.24, 10.39, 10.46, 10.58, 10.57, 10.51, 10.24, 10.07, 10.11, 10.13,
            10.08, 10.0, 9.84, 9.69
        ], name=f'MASS-INDEX_{length}').reset_index(drop=True)
        calculated_mass_index = mass_index(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_mass_index, trading_view_mass)


    def test_mass_index_length_20_tradingview_data(self):
        """
        Test MASS INDEX with the default length of 20 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places
        """

        length = 20

        trading_view_mass = pd.Series([
            18.55, 18.58, 18.74, 18.84, 18.9, 18.98, 19.02, 19.15, 19.34, 19.6, 19.73, 19.85, 19.87, 19.96, 20.12,
            20.27, 20.31, 20.39, 20.3, 20.27
        ], name=f'MASS-INDEX_{length}').reset_index(drop=True)
        calculated_mass_index = mass_index(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_mass_index, trading_view_mass)

    def test_mass_index_series_length_10_tradingview_data(self):
        """
        Test MASS INDEX series with the default length of 10 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places
        """

        ticker = 'AAPL'
        length = 10

        trading_view_mass = pd.Series([
            9.16, 9.33, 9.63, 9.88, 10.01, 10.14, 10.24, 10.39, 10.46, 10.58, 10.57, 10.51, 10.24, 10.07, 10.11, 10.13,
            10.08, 10.0, 9.84, 9.69
        ], name=f'{ticker}_MASS-INDEX_{length}').reset_index(drop=True)
        mass_series = MASS_INDEX(ticker, length)
        calculated_mass_index = mass_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_mass_index, trading_view_mass)

if __name__ == '__main__':
    unittest.main()