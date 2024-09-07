import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.cci import cci
from trading_strategy_tester.trading_series.cci_series import CCI
from trading_strategy_tester.trading_series.cci_smoothened_series import CCI_SMOOTHENED
from trading_strategy_tester.utils.sources import get_source_series

class TestCCI(unittest.TestCase):

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

    def test_cci_hlc3_length_20_tradingview_data(self):
        """
        Test CCI with the default length of 20 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HCL3 to calculate CCI.
        """
        length = 20
        hlc3_series = get_source_series(self.data, SourceType.HLC3)

        trading_view_cci = pd.Series([
            64.68, 28.36, 110.19, 122.75, 162.15, 183.88, 84.26, 110.55, 196.98, 191.37,
            153.25, 85.47, 99.01, 69.16, 45.96, 12.94, -13.45, -39.43, -6.84, -48.73
        ], name=f'CCI_{length}_SMA_1').reset_index(drop=True)
        calculated_cci = cci(hlc3_series, length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

    def test_cci_close_length_10_tradingview_data(self):
        """
        Test CCI with the default length of 10 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate CCI.
        """
        length = 10
        close_series = get_source_series(self.data, SourceType.CLOSE)

        trading_view_cci = pd.Series([
            91.34, -94.44, 217.17, 98.58, 150.94, 146.72, 45.06, 82.54, 158.43, 128.33,
            90.24, 22.15, 51.89, -52.42, -63.13, -92.52, -114.70, -94.33, -65.41, -97.71
        ], name=f'CCI_{length}_SMA_1').reset_index(drop=True)
        calculated_cci = cci(close_series, length).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

    def test_cci_hlc3_length_14_SMA_5_tradingview_data(self):
        """
        Test CCI with the default length of 14 days, SMA smoothing with length of 5.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HLC3 to calculate CCI.
        """
        length = 14
        hlc3_series = get_source_series(self.data, SourceType.HLC3)

        trading_view_cci = pd.Series([
            46.01, 21.46, 50.47, 77.56, 112.91, 134.40, 159.68, 135.93, 131.41, 125.01,
            115.57, 116.54, 115.02, 91.91, 62.95, 27.88, -1.80, -40.09, -60.08, -79.20
        ], name=f'CCI_{length}_SMA_5').reset_index(drop=True)
        calculated_cci = cci(hlc3_series, length, SmoothingType.SMA, 5).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

    def test_cci_hl2_length_21_RMA_10_tradingview_data(self):
        """
        Test CCI with the default length of 21 days, RMA smoothing with length of 10.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HL2 to calculate CCI.
        """
        length = 21
        hl2_series = get_source_series(self.data, SourceType.HL2)

        trading_view_cci = pd.Series([
            75.36, 70.93, 73.25, 78.23, 85.17, 92.81, 91.59, 92.36, 102.00, 111.91,
            117.32, 114.59, 113.38, 110.79, 105.33, 97.20, 87.21, 74.61, 67.70, 58.14
        ], name=f'CCI_{length}_RMA_10').reset_index(drop=True)
        calculated_cci = cci(hl2_series, length, SmoothingType.RMA, 10).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

    def test_cci_series_hlc3_length_20_tradingview_data(self):
        """
        Test CCI series with the default length of 20 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HCL3 to calculate CCI.
        """
        ticker = 'AAPL'
        length = 20
        source = SourceType.HLC3

        trading_view_cci = pd.Series([
            64.68, 28.36, 110.19, 122.75, 162.15, 183.88, 84.26, 110.55, 196.98, 191.37,
            153.25, 85.47, 99.01, 69.16, 45.96, 12.94, -13.45, -39.43, -6.84, -48.73
        ], name=f'{ticker}_CCI_{source.value}_{length}').reset_index(drop=True)
        cci_series = CCI(ticker, source, length)
        calculated_cci = cci_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

    def test_cci_series_close_length_10_tradingview_data(self):
        """
        Test CCI series with the default length of 10 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close to calculate CCI.
        """
        ticker = 'AAPL'
        length = 10
        source = SourceType.CLOSE

        trading_view_cci = pd.Series([
            91.34, -94.44, 217.17, 98.58, 150.94, 146.72, 45.06, 82.54, 158.43, 128.33,
            90.24, 22.15, 51.89, -52.42, -63.13, -92.52, -114.70, -94.33, -65.41, -97.71
        ], name=f'{ticker}_CCI_{source.value}_{length}').reset_index(drop=True)
        cci_series = CCI(ticker, source, length)
        calculated_cci = cci_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

    def test_ccismoothened_series_hlc3_length_14_SMA_5_tradingview_data(self):
        """
        Test CCISmoothened series with the default length of 14 days, SMA smoothing with length of 5.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HLC3 to calculate CCI.
        """
        ticker = 'AAPL'
        length = 14
        source = SourceType.HLC3
        smoothing_type = SmoothingType.SMA
        smoothing_length = 5

        trading_view_cci = pd.Series([
            46.01, 21.46, 50.47, 77.56, 112.91, 134.40, 159.68, 135.93, 131.41, 125.01,
            115.57, 116.54, 115.02, 91.91, 62.95, 27.88, -1.80, -40.09, -60.08, -79.20
        ], name=f'{ticker}_CCISmoothened_{source.value}_{length}_{smoothing_type.value}_{smoothing_length}').reset_index(drop=True)
        cci_series = CCI_SMOOTHENED(ticker, source, length, smoothing_type, smoothing_length)
        calculated_cci = cci_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

    def test_ccismoothened_series_hl2_length_21_RMA_10_tradingview_data(self):
        """
        Test CCISmoothened series with the default length of 21 days, RMA smoothing with length of 10.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use HL2 to calculate CCI.
        """
        ticker = 'AAPL'
        length = 21
        source = SourceType.HL2
        smoothing_type = SmoothingType.RMA
        smoothing_length = 10

        trading_view_cci = pd.Series([
            75.36, 70.93, 73.25, 78.23, 85.17, 92.81, 91.59, 92.36, 102.00, 111.91,
            117.32, 114.59, 113.38, 110.79, 105.33, 97.20, 87.21, 74.61, 67.70, 58.14
        ],
            name=f'{ticker}_CCISmoothened_{source.value}_{length}_{smoothing_type.value}_{smoothing_length}').reset_index(
            drop=True)
        cci_series = CCI_SMOOTHENED(ticker, source, length, smoothing_type, smoothing_length)
        calculated_cci = cci_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_cci, trading_view_cci)

if __name__ == '__main__':
    unittest.main()