import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.overlap.ema import ema
from trading_strategy_tester.trading_series.ma_series.ema_series import EMA

class TestEMA(unittest.TestCase):

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

    def test_ema_close_length_9_offset_0_tradingview_data(self):
        """
        Test EMA with default length of 9 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use Close price to calculate EMA.
        """
        length = 9
        offset = 0
        source = SourceType.CLOSE

        trading_view_ema = pd.Series([
            189.75, 189.69, 190.43, 190.81, 191.50, 192.34, 192.51, 192.95, 193.95, 194.78,
            195.34, 195.45, 195.75, 195.57, 195.39, 195.03, 194.63, 194.34, 194.19, 193.85
        ], name=f'EMA_{length}_{offset}').reset_index(drop=True)
        calculated_ema = ema(
            self.data[source.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ema, trading_view_ema)

    def test_ema_high_length_15_offset_3_tradingview_data(self):
        """
        Test EMA with default length of 15 days and offset 3.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use High price to calculate EMA.
        """
        length = 15
        offset = 3
        source = SourceType.HIGH

        trading_view_ema = pd.Series([
            188.11, 188.61, 188.82, 189.17, 189.28, 189.92, 190.52, 191.08, 191.70, 191.92,
            192.27, 192.99, 193.82, 194.39, 194.67, 194.95, 195.29, 195.52, 195.50, 195.30
        ], name=f'EMA_{length}_{offset}').reset_index(drop=True)
        calculated_ema = ema(
            self.data[source.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ema, trading_view_ema)

    def test_ema_open_length_21_offset_5_tradingview_data(self):
        """
        Test EMA with default length of 21 days and offset 5.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use Open price to calculate EMA.
        """
        length = 21
        offset = 5
        source = SourceType.OPEN

        trading_view_ema = pd.Series([
            184.12, 184.65, 185.11, 185.64, 186.02, 186.41, 186.74, 187.05, 187.72, 188.26,
            188.80, 189.19, 189.55, 190.05, 190.77, 191.39, 191.82, 192.21, 192.64, 192.95
        ], name=f'EMA_{length}_{offset}').reset_index(drop=True)
        calculated_ema = ema(
            self.data[source.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ema, trading_view_ema)

    def test_ema_series_close_length_9_offset_0_tradingview_data(self):
        """
        Test EMA series with default length of 9 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicators data.
        The data is rounded to 2 decimal places, and we use Close price to calculate EMA.
        """
        ticker = 'AAPL'
        length = 9
        offset = 0
        source = SourceType.CLOSE

        trading_view_ema = pd.Series([
            189.75, 189.69, 190.43, 190.81, 191.50, 192.34, 192.51, 192.95, 193.95, 194.78,
            195.34, 195.45, 195.75, 195.57, 195.39, 195.03, 194.63, 194.34, 194.19, 193.85
        ], name=f'{ticker}_EMA_{source.value}_{length}_{offset}').reset_index(drop=True)
        ema_series = EMA(
            ticker,
            source,
            length,
            offset
        )
        calculated_ema = ema_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ema, trading_view_ema)



if __name__ == '__main__':
    unittest.main()