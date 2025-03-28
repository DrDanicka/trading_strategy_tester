import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.trix import trix
from trading_strategy_tester.trading_series.trix_series.trix_series import TRIX


class TestTRIX(unittest.TestCase):

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


    def test_trix_length_18_tradingview_data(self):
        """
        Test TRIX with the default length of 18 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 18

        trading_view_trix = pd.Series([
            23.3, 23.71, 24.13, 24.46, 24.8, 25.2, 25.44, 25.62, 25.92, 26.28, 26.6, 26.75, 26.81, 26.65, 26.29, 25.71,
            24.92, 23.98, 22.96, 21.83
        ], name=f'TRIX_{length}').reset_index(drop=True)
        calculated_trix = trix(
            close=self.data[SourceType.CLOSE.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_trix, trading_view_trix)


    def test_trix_length_25_tradingview_data(self):
        """
        Test TRIX with the default length of 18 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 25

        trading_view_trix = pd.Series([
            11.24, 12.08, 12.91, 13.68, 14.43, 15.18, 15.85, 16.48, 17.13, 17.78, 18.4, 18.94, 19.42, 19.79, 20.06,
            20.2, 20.22, 20.14, 19.98, 19.73
        ], name=f'TRIX_{length}').reset_index(drop=True)
        calculated_trix = trix(
            close=self.data[SourceType.CLOSE.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_trix, trading_view_trix)


    def test_trix_series_length_18_tradingview_data(self):
        """
        Test TRIX series with the default length of 18 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 18

        trading_view_trix = pd.Series([
            23.3, 23.71, 24.13, 24.46, 24.8, 25.2, 25.44, 25.62, 25.92, 26.28, 26.6, 26.75, 26.81, 26.65, 26.29, 25.71,
            24.92, 23.98, 22.96, 21.83
        ], name=f'{ticker}_TRIX_{length}').reset_index(drop=True)
        trix_series = TRIX(ticker=ticker, length=length)
        calculated_trix = trix_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_trix, trading_view_trix)




if __name__ == '__main__':
    unittest.main()