import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volatility.bb import bb_lower, bb_upper, bb_middle
from trading_strategy_tester.trading_series.bb_lower_series import BB_LOWER
from trading_strategy_tester.trading_series.bb_upper_series import BB_UPPER
from trading_strategy_tester.trading_series.bb_middle_series import BB_MIDDLE

class TestBB(unittest.TestCase):

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

    def test_bb_lower_close_length_20_SMA_stddev_2_offset_0(self):
        """
        Test Lower Bollinger Band with the default length of 20, ma_type: SMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Lower Bollinger Band.
        """
        trading_view_bb_lower = pd.Series([
            178.62, 180.71, 182.19, 183.31, 184.18, 185.29, 185.81, 186.78, 186.70, 186.74,
            186.76, 187.05, 187.10, 187.37, 187.59, 187.99, 188.43, 188.79, 189.44, 189.91
        ], name='BBLOWER_20_SMA_2.0_0').reset_index(drop=True)
        calculated_bb_lower = bb_lower(self.data['Close'], 20 ,SmoothingType.SMA,
                                       2, 0).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_lower, trading_view_bb_lower)


    def test_bb_lower_close_length_20_EMA_stddev_2_offset_0(self):
        """
        Test Lower Bollinger Band with the default length of 20, ma_type: EMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Lower Bollinger Band.
        """
        trading_view_bb_lower = pd.Series([
            178.33, 180.03, 181.40, 182.43, 183.32, 184.43, 184.96, 185.91, 186.04, 186.26,
            186.45, 186.78, 186.97, 187.21, 187.40, 187.66, 187.90, 188.11, 188.58, 188.84
        ], name='BBLOWER_20_EMA_2.0_0').reset_index(drop=True)
        calculated_bb_lower = bb_lower(self.data['Close'], 20 ,SmoothingType.EMA,
                                       2, 0).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_lower, trading_view_bb_lower)


    def test_bb_lower_high_length_14_RMA_stddev_1_offset_2(self):
        """
        Test Lower Bollinger Band with the default length of 14, ma_type: RMA, std_dev: 1, offset: 2
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate Lower Bollinger Band.
        """
        trading_view_bb_lower = pd.Series([
            183.11, 183.99, 184.65, 185.46, 185.95, 186.31, 186.61, 186.93, 187.25, 187.59,
            187.76, 187.99, 188.42, 188.88, 189.29, 189.93, 190.49, 191.31, 191.33, 191.26
        ], name='BBLOWER_14_RMA_1.0_2').reset_index(drop=True)
        calculated_bb_lower = bb_lower(self.data['High'], 14 ,SmoothingType.RMA,
                                       1, 2) .tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_lower, trading_view_bb_lower)

    def test_bb_lower_low_length_9_WMA_stddev_3_offset_1(self):
        """
        Test Lower Bollinger Band with the default length of 9, ma_type: WMA, std_dev: 3, offset: 1
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Low price to calculate Lower Bollinger Band.
        """
        trading_view_bb_lower = pd.Series([
            186.93, 187.05, 186.08, 186.16, 185.87, 184.94, 184.73, 184.96, 185.34, 185.82,
            186.02, 187.85, 189.01, 189.47, 189.61, 189.40, 189.82, 190.06, 188.12, 188.20
        ], name='BBLOWER_9_WMA_3.0_1').reset_index(drop=True)
        calculated_bb_lower = bb_lower(self.data['Low'], 9 ,SmoothingType.WMA,
                                       3, 1).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_lower, trading_view_bb_lower)


    def test_bb_upper_close_length_20_SMA_stddev_2_offset_0(self):
        """
        Test Upper Bollinger Band with the default length of 20, ma_type: SMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Upper Bollinger Band.
        """
        trading_view_bb_upper = pd.Series([
            195.70, 194.89, 194.82, 194.76, 195.03, 195.24, 195.40, 195.42, 196.56, 197.52,
            198.29, 198.62, 199.12, 199.26, 199.39, 199.34, 199.23, 199.15, 198.92, 198.71
        ], name='BBUPPER_20_SMA_2.0_0').reset_index(drop=True)
        calculated_bb_upper = bb_upper(self.data['Close'], 20, SmoothingType.SMA,
                                       2, 0).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_upper, trading_view_bb_upper)

    def test_bb_upper_close_length_20_EMA_stddev_2_offset_0(self):
        """
        Test Upper Bollinger Band with the default length of 20, ma_type: EMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Upper Bollinger Band.
        """
        trading_view_bb_upper = pd.Series([
            195.42, 194.21, 194.04, 193.88, 194.16, 194.38, 194.56, 194.56, 195.90, 197.04,
            197.98, 198.35, 198.99, 199.10, 199.20, 199.01, 198.70, 198.47, 198.05, 197.64
        ], name='BBUPPER_20_EMA_2.0_0').reset_index(drop=True)
        calculated_bb_upper = bb_upper(self.data['Close'], 20, SmoothingType.EMA,
                                       2, 0).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_upper, trading_view_bb_upper)

    def test_bb_upper_high_length_14_RMA_stddev_1_offset_2(self):
        """
        Test Upper Bollinger Band with the default length of 14, ma_type: RMA, std_dev: 1, offset: 2
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate Upper Bollinger Band.
        """
        trading_view_bb_upper = pd.Series([
            188.11, 187.89, 188.04, 187.76, 188.38, 189.11, 189.85, 190.64, 190.99, 191.45,
            192.49, 193.62, 194.27, 194.57, 194.90, 195.06, 195.16, 194.71, 194.81, 194.95
        ], name='BBUPPER_14_RMA_1.0_2').reset_index(drop=True)
        calculated_bb_upper = bb_upper(self.data['High'], 14 ,SmoothingType.RMA,
                                       1, 2) .tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_upper, trading_view_bb_upper)

    def test_bb_upper_low_length_9_WMA_stddev_3_offset_1(self):
        """
        Test Upper Bollinger Band with the default length of 9, ma_type: WMA, std_dev: 3, offset: 1
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Low price to calculate Upper Bollinger Band.
        """
        trading_view_bb_upper = pd.Series([
            191.37, 191.22, 191.42, 191.77, 193.25, 195.89, 197.66, 197.87, 197.96, 199.08,
            200.72, 200.75, 199.98, 200.32, 200.39, 200.23, 199.24, 198.29, 198.78, 198.25
        ], name='BBUPPER_9_WMA_3.0_1').reset_index(drop=True)
        calculated_bb_upper = bb_upper(self.data['Low'], 9 ,SmoothingType.WMA,
                                       3, 1).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_upper, trading_view_bb_upper)

    def test_bb_middle_close_length_20_SMA_stddev_2_offset_0(self):
        """
        Test Middle Bollinger Band with the default length of 20, ma_type: SMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Middle Bollinger Band.
        """
        trading_view_bb_middle = pd.Series([
            187.16, 187.80, 188.51, 189.03, 189.60, 190.27, 190.60, 191.10, 191.63, 192.13,
            192.52, 192.83, 193.11, 193.32, 193.49, 193.67, 193.83, 193.97, 194.18, 194.31
        ], name='BBMIDDLE_20_SMA_2.0_0').reset_index(drop=True)
        calculated_bb_middle = bb_middle(self.data['Close'], 20, SmoothingType.SMA,
                                       2, 0).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_middle, trading_view_bb_middle)

    def test_bb_middle_close_length_20_EMA_stddev_2_offset_0(self):
        """
        Test Middle Bollinger Band with the default length of 20, ma_type: EMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Middle Bollinger Band.
        """
        trading_view_bb_middle = pd.Series([
            186.88, 187.12, 187.72, 188.16, 188.74, 189.40, 189.76, 190.23, 190.97, 191.65,
            192.21, 192.56, 192.98, 193.16, 193.30, 193.33, 193.30, 193.29, 193.32, 193.24
        ], name='BBMIDDLE_20_EMA_2.0_0').reset_index(drop=True)
        calculated_bb_middle = bb_middle(self.data['Close'], 20, SmoothingType.EMA,
                                       2, 0).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_middle, trading_view_bb_middle)

    def test_bb_middle_high_length_14_RMA_stddev_1_offset_2(self):
        """
        Test Middle Bollinger Band with the default length of 14, ma_type: RMA, std_dev: 1, offset: 2
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate Middle Bollinger Band.
        """
        trading_view_bb_middle = pd.Series([
            185.61, 185.94, 186.35, 186.61, 187.17, 187.71, 188.23, 188.78, 189.12, 189.52,
            190.13, 190.80, 191.35, 191.72, 192.10, 192.50, 192.82, 193.01, 193.07, 193.10
        ], name='BBMIDDLE_14_RMA_1.0_2').reset_index(drop=True)
        calculated_bb_middle = bb_middle(self.data['High'], 14, SmoothingType.RMA,
                                       1, 2).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_middle, trading_view_bb_middle)

    def test_bb_middle_low_length_9_WMA_stddev_3_offset_1(self):
        """
        Test Middle Bollinger Band with the default length of 9, ma_type: WMA, std_dev: 3, offset: 1
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Low price to calculate Middle Bollinger Band.
        """
        trading_view_bb_middle = pd.Series([
            189.15, 189.14, 188.75, 188.97, 189.56, 190.41, 191.19, 191.41, 191.65, 192.45,
            193.37, 194.30, 194.50, 194.90, 195.00, 194.82, 194.53, 194.18, 193.45, 193.23
        ], name='BBMIDDLE_9_WMA_3.0_1').reset_index(drop=True)
        calculated_bb_middle = bb_middle(self.data['Low'], 9, SmoothingType.WMA,
                                       3, 1).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_middle, trading_view_bb_middle)

    def test_bb_lower_series_close_length_20_SMA_stddev_2_offset_0(self):
        """
        Test Lower Bollinger Band series with the default length of 20, ma_type: SMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Lower Bollinger Band.
        """
        ticker = 'AAPL'

        trading_view_bb_lower = pd.Series([
            178.62, 180.71, 182.19, 183.31, 184.18, 185.29, 185.81, 186.78, 186.70, 186.74,
            186.76, 187.05, 187.10, 187.37, 187.59, 187.99, 188.43, 188.79, 189.44, 189.91
        ], name=f'{ticker}_BBLOWER_Close_20_SMA_2.0_0').reset_index(drop=True)
        bb_lower_series = BB_LOWER(ticker, SourceType.CLOSE, 20, SmoothingType.SMA, 2, 0)
        calculated_bb_lower = bb_lower_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_lower, trading_view_bb_lower)

    def test_bb_upper_series_close_length_20_SMA_stddev_2_offset_0(self):
        """
        Test Upper Bollinger Band series with the default length of 20, ma_type: SMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Upper Bollinger Band.
        """
        ticker = 'AAPL'

        trading_view_bb_upper = pd.Series([
            195.70, 194.89, 194.82, 194.76, 195.03, 195.24, 195.40, 195.42, 196.56, 197.52,
            198.29, 198.62, 199.12, 199.26, 199.39, 199.34, 199.23, 199.15, 198.92, 198.71
        ], name=f'{ticker}_BBUPPER_Close_20_SMA_2.0_0').reset_index(drop=True)
        bb_upper_series = BB_UPPER(ticker, SourceType.CLOSE, 20, SmoothingType.SMA, 2, 0)
        calculated_bb_upper = bb_upper_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_upper, trading_view_bb_upper)

    def test_bb_middle_series_close_length_20_SMA_stddev_2_offset_0(self):
        """
        Test Middle Bollinger Band series with the default length of 20, ma_type: SMA, std_dev: 2, offset: 0
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate Middle Bollinger Band.
        """
        ticker = 'AAPL'

        trading_view_bb_middle = pd.Series([
            187.16, 187.80, 188.51, 189.03, 189.60, 190.27, 190.60, 191.10, 191.63, 192.13,
            192.52, 192.83, 193.11, 193.32, 193.49, 193.67, 193.83, 193.97, 194.18, 194.31
        ], name=f'{ticker}_BBMIDDLE_Close_20_SMA_2.0_0').reset_index(drop=True)
        bb_middle_series = BB_MIDDLE(ticker, SourceType.CLOSE, 20, SmoothingType.SMA, 2, 0)
        calculated_bb_middle = bb_middle_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_middle, trading_view_bb_middle)


    def test_bb_lower_series_high_length_14_RMA_stddev_1_offset_2(self):
        """
        Test Lower Bollinger Band series with the default length of 14, ma_type: RMA, std_dev: 1, offset: 2
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate Lower Bollinger Band.
        """
        ticker = 'AAPL'

        trading_view_bb_lower = pd.Series([
            183.11, 183.99, 184.65, 185.46, 185.95, 186.31, 186.61, 186.93, 187.25, 187.59,
            187.76, 187.99, 188.42, 188.88, 189.29, 189.93, 190.49, 191.31, 191.33, 191.26
        ], name=f'{ticker}_BBLOWER_High_14_RMA_1.0_2').reset_index(drop=True)
        bb_lower_series = BB_LOWER(ticker, SourceType.HIGH, 14, SmoothingType.RMA, 1, 2)
        calculated_bb_lower = bb_lower_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_lower, trading_view_bb_lower)

    def test_bb_upper_series_high_length_14_RMA_stddev_1_offset_2(self):
        """
        Test Upper Bollinger Band series with the default length of 14, ma_type: RMA, std_dev: 1, offset: 2
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate Upper Bollinger Band.
        """
        ticker = 'AAPL'

        trading_view_bb_upper = pd.Series([
            188.11, 187.89, 188.04, 187.76, 188.38, 189.11, 189.85, 190.64, 190.99, 191.45,
            192.49, 193.62, 194.27, 194.57, 194.90, 195.06, 195.16, 194.71, 194.81, 194.95
        ], name=f'{ticker}_BBUPPER_High_14_RMA_1.0_2').reset_index(drop=True)
        bb_upper_series = BB_UPPER(ticker, SourceType.HIGH, 14, SmoothingType.RMA, 1, 2)
        calculated_bb_upper = bb_upper_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_bb_upper, trading_view_bb_upper)


if __name__ == '__main__':
    unittest.main()