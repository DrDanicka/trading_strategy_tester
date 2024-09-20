import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.overlap.ichimoku import conversion_line, base_line, leading_span_a, \
    leading_span_b, lagging_span
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_base_series import ICHIMOKU_BASE
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_conversion_series import ICHIMOKU_CONVERSION
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_lagging_span_series import ICHIMOKU_LAGGING_SPAN
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_leading_span_a_series import \
    ICHIMOKU_LEADING_SPAN_A
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_leading_span_b_series import ICHIMOKU_LEADING_SPAN_B


class TestIchimoku(unittest.TestCase):

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

    def test_ichimoku_conversion_line_length_9_tradingview_data(self):
        """
        Test Ichimoku conversion line with the default length of 9 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 9

        trading_view_conversion_line = pd.Series([
            190.56, 190.19, 190.92, 191.1, 191.22, 191.72, 191.72, 191.72, 192.72, 193.53, 194.9, 195.52, 195.52,
            195.52, 195.52, 195.67, 196.22, 195.35, 194.74, 194.38
        ], name=f'ICHIMOKU-CONVERSION-LINE_{length}').reset_index(drop=True)
        calculated_ichimoku_conversion_line = conversion_line(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_conversion_line, trading_view_conversion_line)


    def test_ichimoku_base_line_length_26_tradingview_data(self):
        """
        Test Ichimoku base line with the default length of 26 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 26

        trading_view_base_line = pd.Series([
            179.3, 179.88, 181.15, 181.33, 182.56, 184.67, 184.67, 186.1, 188.49, 190.6, 190.71, 191.57, 191.92, 192.96,
            193.53, 193.53, 193.53, 193.53, 193.53, 193.53
        ], name=f'ICHIMOKU-BASE-LINE_{length}').reset_index(drop=True)
        calculated_ichimoku_base_line = base_line(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            length=length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_base_line, trading_view_base_line)


    def test_ichimoku_leading_span_A_length_26_tradingview_data(self):
        """
        Test Ichimoku leading span A with the displacement of 26 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        displacement = 26

        trading_view_leading_span_a = pd.Series([
            173.19, 173.02, 172.88, 172.88, 172.27, 172.86, 172.86, 173.28, 174.06, 174.85, 175.45,
            176.68, 177.23, 178.81, 179.51, 180.95, 181.64, 182.77, 182.83, 183.76
        ], name=f'ICHIMOKU-SPAN-A_{displacement}').reset_index(drop=True)
        calculated_ichimoku_leading_span_a = leading_span_a(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            displacement=displacement
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_leading_span_a, trading_view_leading_span_a)


    def test_ichimoku_leading_span_B_length_52_displacement_26_tradingview_data(self):
        """
        Test Ichimoku leading span B with the length of 52 days and displacement of 26 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 52
        displacement = 26

        trading_view_leading_span_b = pd.Series([
            177.82, 177.82, 177.82, 177.82, 177.82, 177.82, 177.82, 177.82, 177.82, 177.82, 177.82,
            177.82, 177.82, 177.82, 177.82, 178.32, 178.32, 178.79, 178.79, 179.3
        ], name=f'ICHIMOKU-SPAN-B_{length}_{displacement}').reset_index(drop=True)
        calculated_ichimoku_leading_span_b = leading_span_b(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            length=length,
            displacement=displacement
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_leading_span_b, trading_view_leading_span_b)


    def test_ichimoku_lagging_span_length_26_tradingview_data(self):
        """
        Test Ichimoku lagging span with the displacement of 26 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        displacement = 26

        trading_view_lagging_span = pd.Series([
            189.97, 189.79, 190.4, 189.37, 189.95, 191.24, 189.43, 193.42, 192.32, 194.27,
            195.71, 193.18, 194.71, 197.96, 198.11, 197.57, 195.89, 196.94, 194.83, 194.68
        ], name=f'ICHIMOKU-LAGGING-SPAN_{displacement}').reset_index(drop=True)
        calculated_ichimoku_lagging_span = lagging_span(
            close=self.data[SourceType.CLOSE.value],
            displacement=displacement
        ).tail(50).reset_index(drop=True).round(2)[:20]
        pd.testing.assert_series_equal(calculated_ichimoku_lagging_span, trading_view_lagging_span)


    def test_ichimoku_conversion_series_length_14_tradingview_data(self):
        """
        Test Ichimoku conversion series with length of 14 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 14

        trading_view_conversion_line = pd.Series([
            188.57, 189.61, 190.92, 191.1, 191.22, 191.72, 191.72, 191.72, 192.72, 193.53,
            193.53, 193.53, 193.53, 193.53, 193.53, 194.9, 195.52, 195.35, 195.35, 195.35
        ], name=f'{ticker}_ICHIMOKU-CONVERSION-LINE_{length}').reset_index(drop=True)
        ichimoku_conversion_series = ICHIMOKU_CONVERSION(ticker=ticker, length=length)
        calculated_ichimoku_conversion_line = ichimoku_conversion_series.get_data(
            self.downloader,
            pd.DataFrame()
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_conversion_line, trading_view_conversion_line)


    def test_ichimoku_base_series_length_20_tradingview_data(self):
        """
        Test Ichimoku base series with length of 20 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 20

        trading_view_base_line = pd.Series([
            183.14, 184.57, 186.68, 188.17, 188.4, 189.76, 190.1, 191.15, 192.72, 193.53,
            193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53
        ], name=f'{ticker}_ICHIMOKU-BASE-LINE_{length}').reset_index(drop=True)
        ichimoku_base_series = ICHIMOKU_BASE(ticker=ticker, length=length)
        calculated_ichimoku_base_line = ichimoku_base_series.get_data(
            self.downloader,
            pd.DataFrame()
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_base_line, trading_view_base_line)


    def test_ichimoku_span_a_series_displacement_26_tradingview_data(self):
        """
        Test Ichimoku base series with length of 26 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        displacement = 26

        trading_view_span_a = pd.Series([
            173.19, 173.02, 172.88, 172.88, 172.27, 172.86, 172.86, 173.28, 174.06, 174.85, 175.45,
            176.68, 177.23, 178.81, 179.51, 180.95, 181.64, 182.77, 182.83, 183.76
        ], name=f'{ticker}_ICHIMOKU-SPAN-A_{displacement}').reset_index(drop=True)
        ichimoku_span_a_series = ICHIMOKU_LEADING_SPAN_A(ticker=ticker, displacement=displacement)
        calculated_ichimoku_span_a = ichimoku_span_a_series.get_data(
            self.downloader,
            pd.DataFrame()
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_span_a, trading_view_span_a)


    def test_ichimoku_span_b_series_length_10_displacement_26_tradingview_data(self):
        """
        Test Ichimoku base series with length of 10 days and displacement of 26 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        displacement = 26
        length = 10

        trading_view_span_b = pd.Series([
            173.8, 172.38, 172.04, 171.75, 171.75, 171.72, 171.72, 172.55, 174.06, 174.56, 175.47, 177.24, 177.24,
            179.11, 181.43, 182.16, 183.59, 185.44, 186.75, 187.37
        ], name=f'{ticker}_ICHIMOKU-SPAN-B_{length}_{displacement}').reset_index(drop=True)
        ichimoku_span_b_series = ICHIMOKU_LEADING_SPAN_B(ticker=ticker, length=length, displacement=displacement)
        calculated_ichimoku_span_b = ichimoku_span_b_series.get_data(
            self.downloader,
            pd.DataFrame()
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_ichimoku_span_b, trading_view_span_b)


    def test_ichimoku_lagging_span_series_displacement_18_tradingview_data(self):
        """
        Test Ichimoku lagging span series with displacement of 18 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        displacement = 18

        trading_view_lagging_span = pd.Series([
            184.8, 187.44, 188.01, 189.71, 189.69, 191.45, 190.64, 191.31, 189.97, 189.79, 190.4, 189.37, 189.95,
            191.24, 189.43, 193.42, 192.32, 194.27, 195.71, 193.18
        ], name=f'{ticker}_ICHIMOKU-LAGGING-SPAN_{displacement}').reset_index(drop=True)
        ichimoku_lagging_span_series = ICHIMOKU_LAGGING_SPAN(ticker=ticker, displacement=displacement)
        calculated_lagging_span = ichimoku_lagging_span_series.get_data(
            self.downloader,
            pd.DataFrame()
        ).tail(50).reset_index(drop=True).round(2)[:20]
        pd.testing.assert_series_equal(calculated_lagging_span, trading_view_lagging_span)

if __name__ == '__main__':
    unittest.main()