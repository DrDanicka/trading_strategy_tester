import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.indicators.trend.aroon import aroon_up, aroon_down
from trading_strategy_tester.trading_series.aroon_series.aroon_up_series import AROON_UP
from trading_strategy_tester.trading_series.aroon_series.aroon_down_series import AROON_DOWN
from trading_strategy_tester.enums.source_enum import SourceType

class TestAroon(unittest.TestCase):

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

    def test_aroon_up_length_14_tradingview_data(self):
        """
        Test AroonUp with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 14

        trading_view_aroon_up = pd.Series([
            57.14, 50.00, 100.00, 100.00, 100.00, 100.00, 92.86, 85.71, 100.00, 100.00,
            92.86, 85.71, 78.57, 71.43, 64.29, 57.14, 50.00, 42.86, 35.71, 28.57
        ], name=f'AROONUP_{length}').reset_index(drop=True)
        calculated_aroon_up = aroon_up(self.data[SourceType.HIGH.value], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_aroon_up, trading_view_aroon_up)

    def test_aroon_up_length_21_tradingview_data(self):
        """
        Test AroonUp with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 21

        trading_view_aroon_up = pd.Series([
            71.43, 66.67, 100.00, 100.00, 100.00, 100.00, 95.24, 90.48, 100.00, 100.00,
            95.24, 90.48, 85.71, 80.95, 76.19, 71.43, 66.67, 61.90, 57.14, 52.38
        ], name=f'AROONUP_{length}').reset_index(drop=True)
        calculated_aroon_up = aroon_up(self.data[SourceType.HIGH.value], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_aroon_up, trading_view_aroon_up)

    def test_aroon_down_length_14_tradingview_data(self):
        """
        Test AroonDown with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 14

        trading_view_aroon_down = pd.Series([
            0.00, 0.00, 0.00, 85.71, 78.57, 71.43, 64.29, 57.14, 50.00, 42.86, 35.71,
            28.57, 21.43, 14.29, 7.14, 0.00, 0.00, 100.00, 92.86, 85.71
        ], name=f'AROONDOWN_{length}').reset_index(drop=True)
        calculated_aroon_down = aroon_down(self.data[SourceType.LOW.value], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_aroon_down, trading_view_aroon_down)

    def test_aroon_down_length_21_tradingview_data(self):
        """
        Test AroonDown with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        length = 21

        trading_view_aroon_down = pd.Series([
            0.00, 4.76, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 57.14,
            52.38, 47.62, 42.86, 38.10, 33.33, 28.57, 23.81, 19.05, 14.29
        ], name=f'AROONDOWN_{length}').reset_index(drop=True)
        calculated_aroon_down = aroon_down(self.data[SourceType.LOW.value], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_aroon_down, trading_view_aroon_down)

    def test_aroon_up_series_length_14_tradingview_data(self):
        """
        Test AroonUp series with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        ticker = 'AAPL'
        length = 14

        trading_view_aroon_up = pd.Series([
            57.14, 50.00, 100.00, 100.00, 100.00, 100.00, 92.86, 85.71, 100.00, 100.00,
            92.86, 85.71, 78.57, 71.43, 64.29, 57.14, 50.00, 42.86, 35.71, 28.57
        ], name=f'{ticker}_AROONUP_{length}').reset_index(drop=True)
        aroon_up_series = AROON_UP(ticker, length)
        calculated_aroon_up = aroon_up_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_aroon_up, trading_view_aroon_up)

    def test_aroon_down_series_length_14_tradingview_data(self):
        """
        Test AroonDown series with the default length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """
        ticker = 'AAPL'
        length = 14

        trading_view_aroon_down = pd.Series([
            0.00, 0.00, 0.00, 85.71, 78.57, 71.43, 64.29, 57.14, 50.00, 42.86, 35.71,
            28.57, 21.43, 14.29, 7.14, 0.00, 0.00, 100.00, 92.86, 85.71
        ], name=f'{ticker}_AROONDOWN_{length}').reset_index(drop=True)
        aroon_down_series = AROON_DOWN(ticker, length)
        calculated_aroon_down = aroon_down_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_aroon_down, trading_view_aroon_down)


if __name__ == '__main__':
    unittest.main()