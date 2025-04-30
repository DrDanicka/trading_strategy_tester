import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volatility.kc import kc
from trading_strategy_tester.trading_series.kc_series.kc_lower_series import KC_LOWER
from trading_strategy_tester.trading_series.kc_series.kc_upper_series import KC_UPPER


class TestKC(unittest.TestCase):

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

    def test_kc_upper_length_20_multiplier_2_EMA_atr_length_10_tradingview_data(self):
        """
        Test KC upper with the default length of 20 days, multiplier of 2 and ATR length of 10
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KC.
        """

        length = 20
        multiplier = 2
        ema = True
        atr_length = 10
        target_col = SourceType.CLOSE.value

        trading_view_kc_upper = pd.Series([
            191.82, 192.33, 193.4, 193.8, 194.35, 194.92, 195.59, 196.08, 196.88, 197.67, 197.91, 198.32, 198.38,
            198.58, 198.9, 198.86, 198.49, 198.44, 198.25, 198.22
        ], name=f'KC-UPPER_{length}_{multiplier}_{ema}_{atr_length}').reset_index(drop=True)
        calculated_kc_upper = kc(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            series=self.data[target_col],
            upper=True,
            length=length,
            multiplier=multiplier,
            use_exp_ma=ema,
            atr_length=atr_length
        ).reset_index(drop=True).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kc_upper, trading_view_kc_upper)


    def test_kc_upper_length_16_multiplier_3_SMA_atr_length_18_tradingview_data(self):
        """
        Test KC upper with the default length of 16 days, multiplier of 3 and ATR length of 18
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Low price to calculate KC.
        """

        length = 16
        multiplier = 3
        ema = False
        atr_length = 18
        target_col = SourceType.LOW.value

        trading_view_kc_upper = pd.Series([
            195.97, 196.5, 197.28, 197.73, 198.16, 198.43, 198.85, 199.06, 199.43, 199.92,
            200.04, 200.41, 200.54, 200.89, 201.3, 201.53, 201.46, 201.64, 201.62, 201.6
        ], name=f'KC-UPPER_{length}_{multiplier}_{ema}_{atr_length}').reset_index(drop=True)
        calculated_kc_upper = kc(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            series=self.data[target_col],
            upper=True,
            length=length,
            multiplier=multiplier,
            use_exp_ma=ema,
            atr_length=atr_length
        ).reset_index(drop=True).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kc_upper, trading_view_kc_upper)

    def test_kc_lower_length_20_multiplier_2_EMA_atr_length_10_tradingview_data(self):
        """
        Test KC lower with the default length of 20 days, multiplier of 2 and ATR length of 10
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KC.
        """

        length = 20
        multiplier = 2
        ema = True
        atr_length = 10
        target_col = SourceType.CLOSE.value

        trading_view_kc_upper = pd.Series([
            181.93, 181.91, 182.04, 182.52, 183.13, 183.89, 183.94, 184.39, 185.06, 185.64, 186.52, 186.8, 187.58,
            187.73, 187.7, 187.8, 188.12, 188.14, 188.38, 188.26
        ], name=f'KC-LOWER_{length}_{multiplier}_{ema}_{atr_length}').reset_index(drop=True)
        calculated_kc_upper = kc(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            series=self.data[target_col],
            upper=False,
            length=length,
            multiplier=multiplier,
            use_exp_ma=ema,
            atr_length=atr_length
        ).reset_index(drop=True).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kc_upper, trading_view_kc_upper)


    def test_kc_lower_length_9_multiplier_1_SMA_atr_length_15_tradingview_data(self):
        """
        Test KC lower with the default length of 9 days, multiplier of 1 and ATR length of 15
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use High price to calculate KC.
        """

        length = 9
        multiplier = 1
        ema = False
        atr_length = 15
        target_col = SourceType.HIGH.value

        trading_view_kc_upper = pd.Series([
            188.81, 188.52, 188.69, 188.91, 189.38, 190.0, 190.17, 190.46, 191.28, 192.14, 193.18, 193.4, 193.77,
            194.06, 194.13, 194.37, 194.39, 193.91, 193.43, 192.98
        ], name=f'KC-LOWER_{length}_{multiplier}_{ema}_{atr_length}').reset_index(drop=True)
        calculated_kc_upper = kc(
            high=self.data[SourceType.HIGH.value],
            low=self.data[SourceType.LOW.value],
            close=self.data[SourceType.CLOSE.value],
            series=self.data[target_col],
            upper=False,
            length=length,
            multiplier=multiplier,
            use_exp_ma=ema,
            atr_length=atr_length
        ).reset_index(drop=True).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kc_upper, trading_view_kc_upper)


    def test_kc_upper_series_length_20_multiplier_2_EMA_atr_length_10_tradingview_data(self):
        """
        Test KC upper series with the default length of 20 days, multiplier of 2 and ATR length of 10
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KC.
        """

        ticker = 'AAPL'
        length = 20
        multiplier = 2
        ema = True
        atr_length = 10
        target_col = SourceType.CLOSE

        trading_view_kc_upper = pd.Series([
            191.82, 192.33, 193.4, 193.8, 194.35, 194.92, 195.59, 196.08, 196.88, 197.67, 197.91, 198.32, 198.38,
            198.58, 198.9, 198.86, 198.49, 198.44, 198.25, 198.22
        ], name=f'{ticker}_KC-UPPER_{target_col.value}_{length}_{multiplier}_{ema}_{atr_length}').reset_index(drop=True)
        kc_upper_series = KC_UPPER(ticker, target_col, length, multiplier, ema, atr_length)
        calculated_kc_upper = kc_upper_series.get_data(self.downloader, pd.DataFrame()).reset_index(drop=True).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kc_upper, trading_view_kc_upper)


    def test_kc_lower_series_length_20_multiplier_2_EMA_atr_length_10_tradingview_data(self):
        """
        Test KC lower series with the default length of 20 days, multiplier of 2 and ATR length of 10
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KC.
        """

        ticker = 'AAPL'
        length = 20
        multiplier = 2
        ema = True
        atr_length = 10
        target_col = SourceType.CLOSE

        trading_view_kc_lower = pd.Series([
            181.93, 181.91, 182.04, 182.52, 183.13, 183.89, 183.94, 184.39, 185.06, 185.64, 186.52, 186.8, 187.58,
            187.73, 187.7, 187.8, 188.12, 188.14, 188.38, 188.26
        ], name=f'{ticker}_KC-LOWER_{target_col.value}_{length}_{multiplier}_{ema}_{atr_length}').reset_index(drop=True)
        kc_lower_series = KC_LOWER(ticker, target_col, length, multiplier, ema, atr_length)
        calculated_kc_lower = kc_lower_series.get_data(self.downloader, pd.DataFrame()).reset_index(drop=True).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kc_lower, trading_view_kc_lower)


if __name__ == '__main__':
    unittest.main()