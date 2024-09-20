import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volatility.dc import dc_upper, dc_lower, dc_basis
from trading_strategy_tester.trading_series.dc_series.dc_upper_series import DC_UPPER
from trading_strategy_tester.trading_series.dc_series.dc_lower_series import DC_LOWER
from trading_strategy_tester.trading_series.dc_series.dc_basis_series import DC_BASIS

class TestDonchainChannel(unittest.TestCase):

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

    def test_dc_upper_length_20_offset_0_tradingview_data(self):
        """
        Test Donchain Channel upper with the default length of 20 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 20
        offset = 0

        trading_view_dc_upper = pd.Series([
            192.93, 192.93, 194.4, 194.76, 195.0, 195.99, 195.99, 195.99, 198.0, 199.62,
            199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62
        ], name=f'DCUPPER_{length}_{offset}').reset_index(drop=True)
        calculated_dc_upper = dc_upper(self.data[SourceType.HIGH.value], length, offset).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_upper, trading_view_dc_upper)


    def test_dc_upper_length_9_offset_2_tradingview_data(self):
        """
        Test Donchain Channel upper with the default length of 9 days and offset 2.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 9
        offset = 2

        trading_view_dc_upper = pd.Series([
            192.93, 192.93, 192.93, 192.93, 194.4, 194.76, 195.0, 195.99, 195.99, 195.99,
            198.0, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62
        ], name=f'DCUPPER_{length}_{offset}').reset_index(drop=True)
        calculated_dc_upper = dc_upper(self.data[SourceType.HIGH.value], length, offset).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_upper, trading_view_dc_upper)


    def test_dc_lower_length_20_offset_0_tradingview_data(self):
        """
        Test Donchain Channel lower with the default length of 20 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 20
        offset = 0

        trading_view_dc_lower = pd.Series([
            173.35, 176.21, 178.97, 181.59, 181.81, 183.53, 184.21, 186.3, 187.45, 187.45,
            187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45
        ], name=f'DCLOWER_{length}_{offset}').reset_index(drop=True)
        calculated_dc_lower = dc_lower(self.data[SourceType.LOW.value], length, offset).tail(20).reset_index(
            drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_lower, trading_view_dc_lower)


    def test_dc_lower_length_12_offset_1_tradingview_data(self):
        """
        Test Donchain Channel lower with the default length of 12 days and offset 1.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 12
        offset = 1

        trading_view_dc_lower = pd.Series([
            186.3, 187.78, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45,
            187.45, 187.45, 187.45, 187.45, 190.18, 191.42, 191.42, 191.42, 191.09, 191.09
        ], name=f'DCLOWER_{length}_{offset}').reset_index(drop=True)
        calculated_dc_lower = dc_lower(self.data[SourceType.LOW.value], length, offset).tail(20).reset_index(
            drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_lower, trading_view_dc_lower)


    def test_dc_basis_length_20_offset_0_tradingview_data(self):
        """
        Test Donchain Channel with the default length of 20 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 20
        offset = 0

        trading_view_dc_basis = pd.Series([
            183.14, 184.57, 186.68, 188.17, 188.4, 189.76, 190.1, 191.15, 192.72, 193.53,
            193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53
        ], name=f'DCBASIS_{length}_{offset}').reset_index(drop=True)
        calculated_dc_basis = dc_basis(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_basis, trading_view_dc_basis)


    def test_dc_basis_length_15_offset_3_tradingview_data(self):
        """
        Test Donchain Channel with the default length of 15 days and offset 3.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 15
        offset = 3

        trading_view_dc_basis = pd.Series([
            185.95, 187.26, 187.37, 188.23, 188.57, 190.35, 191.1, 191.22, 191.72, 191.72,
            191.72, 192.72, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 194.9
        ], name=f'DCBASIS_{length}_{offset}').reset_index(drop=True)
        calculated_dc_basis = dc_basis(
            self.data[SourceType.HIGH.value],
            self.data[SourceType.LOW.value],
            length,
            offset
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_basis, trading_view_dc_basis)


    def test_dc_upper_series_length_20_offset_0_tradingview_data(self):
        """
        Test Donchain Channel upper series with the default length of 20 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 20
        offset = 0

        trading_view_dc_upper = pd.Series([
            192.93, 192.93, 194.4, 194.76, 195.0, 195.99, 195.99, 195.99, 198.0, 199.62,
            199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62, 199.62
        ], name=f'{ticker}_DCUPPER_{length}_{offset}').reset_index(drop=True)
        dc_upper_series = DC_UPPER(ticker, length, offset)
        calculated_dc_upper = dc_upper_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_upper, trading_view_dc_upper)


    def test_dc_lower_series_length_20_offset_0_tradingview_data(self):
        """
        Test Donchain Channel lower series with the default length of 20 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 20
        offset = 0

        trading_view_dc_lower = pd.Series([
            173.35, 176.21, 178.97, 181.59, 181.81, 183.53, 184.21, 186.3, 187.45, 187.45,
            187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45, 187.45
        ], name=f'{ticker}_DCLOWER_{length}_{offset}').reset_index(drop=True)
        dc_lower_series = DC_LOWER(ticker, length, offset)
        calculated_dc_lower = dc_lower_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(
            drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_lower, trading_view_dc_lower)


    def test_dc_basis_series_length_20_offset_0_tradingview_data(self):
        """
        Test Donchain Channel with the default length of 20 days and offset 0.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 20
        offset = 0

        trading_view_dc_basis = pd.Series([
            183.14, 184.57, 186.68, 188.17, 188.4, 189.76, 190.1, 191.15, 192.72, 193.53,
            193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53, 193.53
        ], name=f'{ticker}_DCBASIS_{length}_{offset}').reset_index(drop=True)
        dc_basis_series = DC_BASIS(ticker, length, offset)
        calculated_dc_basis = dc_basis_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_dc_basis, trading_view_dc_basis)

if __name__ == '__main__':
    unittest.main()