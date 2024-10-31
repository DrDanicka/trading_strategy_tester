import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volume.obv import obv
from trading_strategy_tester.trading_series.obv_series.obv_series import OBV


class TestOBV(unittest.TestCase):

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

    def test_obv_tradingview_data(self):
        """
        Test OBV indicator.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        trading_view_obv = pd.Series([
            1736754100.0, 1693364600.0, 1759993000.0, 1718903300.0, 1766381000.0, 1819758300.0, 1758814600.0,
            1811511500.0, 1881915700.0, 1948747300.0, 1820490600.0, 1764738700.0, 1805452800.0, 1753210000.0,
            1706727500.0, 1669604700.0, 1640685400.0, 1688773100.0, 1722823000.0, 1680194200.0
        ], name='OBV').reset_index(drop=True)
        calculated_obv = obv(
            close=self.data[SourceType.CLOSE.value],
            volume=self.data['Volume']
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_obv, trading_view_obv)


    def test_obv_series_tradingview_data(self):
        """
        Test OBV series.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'

        trading_view_obv = pd.Series([
            1736754100.0, 1693364600.0, 1759993000.0, 1718903300.0, 1766381000.0, 1819758300.0, 1758814600.0,
            1811511500.0, 1881915700.0, 1948747300.0, 1820490600.0, 1764738700.0, 1805452800.0, 1753210000.0,
            1706727500.0, 1669604700.0, 1640685400.0, 1688773100.0, 1722823000.0, 1680194200.0
        ], name=f'{ticker}_OBV').reset_index(drop=True)
        obv_series = OBV(ticker)
        calculated_obv = obv_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_obv, trading_view_obv)

if __name__ == '__main__':
    unittest.main()