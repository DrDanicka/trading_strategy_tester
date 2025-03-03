import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volume.eom import eom
from trading_strategy_tester.trading_series.eom_series.eom_series import EOM

class TestEOM(unittest.TestCase):

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

    def test_eom_length_14_divisor_10000000_tradingview_data(self):
        """
        Test EOM with the default length of 14 days and divisor of 10_000_000.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 6 decimal places.
        """

        length = 14
        divisor = 10_000_000

        trading_view_eom = pd.Series([
            0.122939, 0.050444, 0.165749, 0.18572, 0.168636, 0.193623, 0.091728, 0.131671, 0.186771, 0.329406, 0.336966,
            0.259903, 0.2618, 0.295126, 0.200504, 0.219269, 0.037389, -0.053482, -0.021089, -0.075727
        ], name=f'EOM_{length}_{divisor}').reset_index(drop=True)
        calculated_eom = eom(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.VOLUME.value],
            length,
            divisor
        ).tail(20).reset_index(drop=True).round(6)
        pd.testing.assert_series_equal(calculated_eom, trading_view_eom)

    def test_eom_length_21_divisor_10000_tradingview_data(self):
        """
        Test EOM with the default length of 21 days and divisor of 10_000.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 6 decimal places.
        """

        length = 21
        divisor = 10_000

        trading_view_eom = pd.Series([
            0.000334, 0.000224, 0.000362, 0.000332, 0.000276, 0.000255, 0.000207, 0.000183, 0.000249, 0.000256,
            0.000233, 0.000167, 0.000184, 0.00015, 0.000121, 5.5e-05, 9.9e-05, 8e-05, 0.000104, 6.9e-05
        ], name=f'EOM_{length}_{divisor}').reset_index(drop=True)
        calculated_eom = eom(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            self.data[SourceType.VOLUME.value],
            length,
            divisor
        ).tail(20).reset_index(drop=True).round(6)
        pd.testing.assert_series_equal(calculated_eom, trading_view_eom)

    def test_eom_series_length_14_divisor_10000_tradingview_data(self):
        """
        Test EOM series with the default length of 14 days and divisor of 10_000.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 6 decimal places.
        """

        ticker = 'AAPL'
        length = 14
        divisor = 10_000

        trading_view_eom = pd.Series([
            0.000123, 5e-05, 0.000166, 0.000186, 0.000169, 0.000194, 9.2e-05, 0.000132, 0.000187, 0.000329, 0.000337,
            0.00026, 0.000262, 0.000295, 0.000201, 0.000219, 3.7e-05, -5.3e-05, -2.1e-05, -7.6e-05
        ], name=f'{ticker}_EOM_{length}_{divisor}').reset_index(drop=True)
        eom_series = EOM(ticker, length, divisor)
        calculated_eom = eom_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(6)
        pd.testing.assert_series_equal(calculated_eom, trading_view_eom)

if __name__ == '__main__':
    unittest.main()