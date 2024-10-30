import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.macd import macd, macd_signal
from trading_strategy_tester.trading_series.macd_series.macd_series import MACD
from trading_strategy_tester.trading_series.macd_series.macd_signal_series import MACD_SIGNAL
from trading_strategy_tester.utils.sources import get_source_series


class TestMACD(unittest.TestCase):

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

    def test_macd_close_fast_12_slow_26_EMA_tradingview_data(self):
        """
        Test MACD with fast length of 12 and slow length of 26.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD.
        """

        source = SourceType.CLOSE
        fast_length = 12
        slow_length = 26
        smoothing_type = SmoothingType.EMA

        trading_view_macd = pd.Series([
            3.5, 3.27, 3.37, 3.33, 3.41, 3.55, 3.42, 3.4, 3.6, 3.73, 3.75, 3.59,
            3.5, 3.23, 2.96, 2.64, 2.31, 2.03, 1.82, 1.56
        ], name=f'MACD_{fast_length}_{slow_length}_{smoothing_type.value}').reset_index(drop=True)
        calculated_macd = macd(
            series=self.data[source.value],
            slow_length=slow_length,
            fast_length=fast_length,
            ma_type=smoothing_type,
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd, trading_view_macd)


    def test_macd_signal_hcl3_fast_16_slow_20_SMA_tradingview_data(self):
        """
        Test MACD with fast length of 16 and slow length of 20.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD.
        """

        source = SourceType.HLC3
        fast_length = 16
        slow_length = 20
        smoothing_type = SmoothingType.SMA

        trading_view_macd = pd.Series([
            1.9, 1.61, 1.34, 1.25, 1.1, 0.9, 0.73, 0.55, 0.44, 0.42,
            0.4, 0.44, 0.59, 0.68, 0.82, 0.9, 0.89, 1.0, 0.89, 0.71
        ], name=f'MACD_{fast_length}_{slow_length}_{smoothing_type.value}').reset_index(drop=True)
        calculated_macd = macd(
            series=get_source_series(self.data, source),
            slow_length=slow_length,
            fast_length=fast_length,
            ma_type=smoothing_type
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd, trading_view_macd)


    def test_macd_signal_close_fast_12_slow_26_EMA_EMA_signal_9_tradingview_data(self):
        """
        Test MACD signal with fast length of 12 and slow length of 26 and signal length of 9.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD signal.
        """

        source = SourceType.CLOSE
        fast_length = 12
        slow_length = 26
        oscillator_ma_type = SmoothingType.EMA
        signal_ma_type = SmoothingType.EMA
        signal_length = 9

        trading_view_macd_signal = pd.Series([
            3.55, 3.49, 3.47, 3.44, 3.43, 3.46, 3.45, 3.44, 3.47, 3.52, 3.57,
            3.57, 3.56, 3.49, 3.39, 3.24, 3.05, 2.85, 2.64, 2.43
        ], name=f'MACD-SIGNAL_{fast_length}_{slow_length}_{oscillator_ma_type.value}_{signal_ma_type.value}_{signal_length}').reset_index(drop=True)
        calculated_macd_signal = macd_signal(
            series=self.data[source.value],
            slow_length=slow_length,
            fast_length=fast_length,
            oscillator_ma_type=oscillator_ma_type,
            signal_ma_type=signal_ma_type,
            signal_length=signal_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd_signal, trading_view_macd_signal)


    def test_macd_signal_hl2_fast_13_slow_21_SMA_SMA_signal_15_tradingview_data(self):
        """
        Test MACD signal with fast length of 12 and slow length of 26 and signal length of 9.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD signal.
        """

        source = SourceType.HL2
        fast_length = 13
        slow_length = 21
        oscillator_ma_type = SmoothingType.SMA
        signal_ma_type = SmoothingType.SMA
        signal_length = 15

        trading_view_macd_signal = pd.Series([
            3.82, 4.03, 4.15, 4.17, 4.11, 3.97, 3.75, 3.47, 3.17, 2.85,
            2.54, 2.26, 2.02, 1.82, 1.69, 1.58, 1.5, 1.43, 1.38, 1.34
        ], name=f'MACD-SIGNAL_{fast_length}_{slow_length}_{oscillator_ma_type.value}_{signal_ma_type.value}_{signal_length}').reset_index(drop=True)
        calculated_macd_signal = macd_signal(
            series=get_source_series(self.data, source),
            slow_length=slow_length,
            fast_length=fast_length,
            oscillator_ma_type=oscillator_ma_type,
            signal_ma_type=signal_ma_type,
            signal_length=signal_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd_signal, trading_view_macd_signal)


    def test_macd_series_close_fast_12_slow_26_EMA_tradingview_data(self):
        """
        Test MACD series with fast length of 12 and slow length of 26.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD.
        """

        ticker = 'AAPL'
        source = SourceType.CLOSE
        fast_length = 12
        slow_length = 26
        smoothing_type = SmoothingType.EMA

        trading_view_macd = pd.Series([
            3.5, 3.27, 3.37, 3.33, 3.41, 3.55, 3.42, 3.4, 3.6, 3.73, 3.75, 3.59,
            3.5, 3.23, 2.96, 2.64, 2.31, 2.03, 1.82, 1.56
        ], name=f'{ticker}_MACD_{fast_length}_{slow_length}_{smoothing_type.value}').reset_index(drop=True)
        macd_series = MACD(
            ticker=ticker,
            source=source,
            fast_length=fast_length,
            slow_length=slow_length,
            ma_type=smoothing_type
        )
        calculated_macd = macd_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd, trading_view_macd)


    def test_macd_signal_series_hcl3_fast_16_slow_20_SMA_tradingview_data(self):
        """
        Test MACD with fast length of 16 and slow length of 20.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD.
        """

        ticker = 'AAPL'
        source = SourceType.HLC3
        fast_length = 16
        slow_length = 20
        smoothing_type = SmoothingType.SMA

        trading_view_macd = pd.Series([
            1.9, 1.61, 1.34, 1.25, 1.1, 0.9, 0.73, 0.55, 0.44, 0.42,
            0.4, 0.44, 0.59, 0.68, 0.82, 0.9, 0.89, 1.0, 0.89, 0.71
        ], name=f'{ticker}_MACD_{fast_length}_{slow_length}_{smoothing_type.value}').reset_index(drop=True)
        macd_series = MACD(
            ticker=ticker,
            source=source,
            fast_length=fast_length,
            slow_length=slow_length,
            ma_type=smoothing_type
        )
        calculated_macd = macd_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd, trading_view_macd)


    def test_macd_signal_seriess_close_fast_12_slow_26_EMA_EMA_signal_9_tradingview_data(self):
        """
        Test MACD signal series with fast length of 12 and slow length of 26 and signal length of 9.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD signal.
        """

        ticker = 'AAPL'
        source = SourceType.CLOSE
        fast_length = 12
        slow_length = 26
        oscillator_ma_type = SmoothingType.EMA
        signal_ma_type = SmoothingType.EMA
        signal_length = 9

        trading_view_macd = pd.Series([
            3.55, 3.49, 3.47, 3.44, 3.43, 3.46, 3.45, 3.44, 3.47, 3.52, 3.57,
            3.57, 3.56, 3.49, 3.39, 3.24, 3.05, 2.85, 2.64, 2.43
        ], name=f'{ticker}_MACD-SIGNAL_{fast_length}_{slow_length}_{oscillator_ma_type.value}_{signal_ma_type.value}_{signal_length}').reset_index(drop=True)
        macd_signal_series = MACD_SIGNAL(
            ticker=ticker,
            source=source,
            fast_length=fast_length,
            slow_length=slow_length,
            oscillator_ma_type=oscillator_ma_type,
            signal_ma_type=signal_ma_type,
            signal_length=signal_length
        )
        calculated_macd_signal = macd_signal_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd_signal, trading_view_macd)


    def test_macd_signal_seriess_hl2_fast_13_slow_21_SMA_SMA_signal_15_tradingview_data(self):
        """
        Test MACD signal series with fast length of 13 and slow length of 21 and signal length of 15.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate MACD signal.
        """

        ticker = 'AAPL'
        source = SourceType.HL2
        fast_length = 13
        slow_length = 21
        oscillator_ma_type = SmoothingType.SMA
        signal_ma_type = SmoothingType.SMA
        signal_length = 15

        trading_view_macd = pd.Series([
            3.82, 4.03, 4.15, 4.17, 4.11, 3.97, 3.75, 3.47, 3.17, 2.85,
            2.54, 2.26, 2.02, 1.82, 1.69, 1.58, 1.5, 1.43, 1.38, 1.34
        ], name=f'{ticker}_MACD-SIGNAL_{fast_length}_{slow_length}_{oscillator_ma_type.value}_{signal_ma_type.value}_{signal_length}').reset_index(drop=True)
        macd_signal_series = MACD_SIGNAL(
            ticker=ticker,
            source=source,
            fast_length=fast_length,
            slow_length=slow_length,
            oscillator_ma_type=oscillator_ma_type,
            signal_ma_type=signal_ma_type,
            signal_length=signal_length
        )
        calculated_macd_signal = macd_signal_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_macd_signal, trading_view_macd)


if __name__ == '__main__':
    unittest.main()