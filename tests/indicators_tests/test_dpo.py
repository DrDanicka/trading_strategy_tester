import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.trend.dpo import dpo
from trading_strategy_tester.trading_series.dpo_series.dpo_series import DPO

class TestDPO(unittest.TestCase):

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

    def test_dpo_length_21_tradingview_data(self):
        """
        Test DPO with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 21

        trading_view_dpo = pd.Series([
            14.14, 11.67, 14.98, 13.0, 14.11, 14.7, 11.27, 11.71, 13.9, 13.14,
            11.69, 9.19, 9.67, 6.76, 5.99, 4.32, 3.16, 2.75, 2.78, 1.1
        ], name=f'DPO_{length}').reset_index(drop=True)
        calculated_dpo = dpo(self.data[SourceType.CLOSE.value], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dpo, trading_view_dpo)

    def test_dpo_length_9_tradingview_data(self):
        """
        Test DPO with the default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 9

        trading_view_dpo = pd.Series([
            2.02, -0.35, 3.31, 2.06, 3.98, 5.25, 2.95, 4.17, 7.31, 6.98, 5.78,
            3.79, 4.25, 1.25, 0.33, -1.65, -2.47, -2.89, -2.52, -3.46
        ], name=f'DPO_{length}').reset_index(drop=True)
        calculated_dpo = dpo(self.data[SourceType.CLOSE.value], length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dpo, trading_view_dpo)

    def test_dpo_series_length_21_tradingview_data(self):
        """
        Test DPO series with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 21

        trading_view_dpo = pd.Series([
            14.14, 11.67, 14.98, 13.0, 14.11, 14.7, 11.27, 11.71, 13.9, 13.14,
            11.69, 9.19, 9.67, 6.76, 5.99, 4.32, 3.16, 2.75, 2.78, 1.1
        ], name=f'{ticker}_DPO_{length}').reset_index(drop=True)
        dpo_series = DPO(ticker, length=length)
        calculated_dpo = dpo_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dpo, trading_view_dpo)

if __name__ == '__main__':
    unittest.main()