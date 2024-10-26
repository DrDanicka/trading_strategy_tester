import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.momentum.kst import kst, kst_signal
from trading_strategy_tester.trading_series.kst_series.kst_signal_series import KST_SIGNAL
from trading_strategy_tester.trading_series.kst_series.kst_line_series import KST


class TestKST(unittest.TestCase):

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

    def test_kst_close_params_1_tradingview_data(self):
        """
        Test KST with specified lengths.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KST.
        """

        roc_length_1 = 10
        roc_length_2 = 15
        roc_length_3 = 20
        roc_length_4 = 30
        sma_length_1 = 10
        sma_length_2 = 10
        sma_length_3 = 10
        sma_length_4 = 15
        source = SourceType.CLOSE.value

        trading_view_kst = pd.Series([
            81.31, 77.77, 76.27, 73.4, 71.5, 71.01, 69.25, 68.3, 69.42, 70.54,
            71.19, 71.95, 71.16, 70.25, 68.19, 65.02, 62.67, 58.88, 54.52, 48.74
        ], name=f'KST_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}').reset_index(drop=True)
        calculated_kst = kst(
            series=self.data[source],
            roc_length_1=roc_length_1,
            roc_length_2=roc_length_2,
            roc_length_3=roc_length_3,
            roc_length_4=roc_length_4,
            sma_length_1=sma_length_1,
            sma_length_2=sma_length_2,
            sma_length_3=sma_length_3,
            sma_length_4=sma_length_4,
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kst, trading_view_kst)


    def test_kst_close_params_2_tradingview_data(self):
        """
        Test KST with specified lengths.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KST.
        """

        roc_length_1 = 8
        roc_length_2 = 17
        roc_length_3 = 23
        roc_length_4 = 40
        sma_length_1 = 12
        sma_length_2 = 14
        sma_length_3 = 17
        sma_length_4 = 10

        source = SourceType.CLOSE.value

        trading_view_kst = pd.Series([
            84.73, 84.56, 85.2, 83.6, 82.39, 81.09, 78.39, 76.64, 76.71, 76.73, 77.14,
            78.14, 79.18, 79.34, 79.66, 80.22, 79.83, 78.87, 77.17, 73.6
        ],
            name=f'KST_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}').reset_index(
            drop=True)
        calculated_kst = kst(
            series=self.data[source],
            roc_length_1=roc_length_1,
            roc_length_2=roc_length_2,
            roc_length_3=roc_length_3,
            roc_length_4=roc_length_4,
            sma_length_1=sma_length_1,
            sma_length_2=sma_length_2,
            sma_length_3=sma_length_3,
            sma_length_4=sma_length_4,
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kst, trading_view_kst)


    def test_kst_signal_close_params_1_signal_length_9_tradingview_data(self):
        """
        Test KST SIGNAL with specified lengths and signal length of 9.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KST SIGNAL.
        """

        roc_length_1 = 10
        roc_length_2 = 15
        roc_length_3 = 20
        roc_length_4 = 30
        sma_length_1 = 10
        sma_length_2 = 10
        sma_length_3 = 10
        sma_length_4 = 15
        signal_length = 9
        source = SourceType.CLOSE.value

        trading_view_kst_signal = pd.Series([
            76.96, 78.92, 79.92, 79.93, 79.21, 78.1, 76.45, 74.67, 73.14, 71.94,
            71.21, 70.73, 70.48, 70.34, 70.03, 69.56, 68.93, 67.76, 65.98, 63.48
        ],
            name=f'KST-SIGNAL_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}_{signal_length}').reset_index(
            drop=True)
        calculated_kst_signal = kst_signal(
            series=self.data[source],
            roc_length_1=roc_length_1,
            roc_length_2=roc_length_2,
            roc_length_3=roc_length_3,
            roc_length_4=roc_length_4,
            sma_length_1=sma_length_1,
            sma_length_2=sma_length_2,
            sma_length_3=sma_length_3,
            sma_length_4=sma_length_4,
            signal_length=signal_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kst_signal, trading_view_kst_signal)

    def test_kst_signal_close_params_2_signal_length_15_tradingview_data(self):
        """
        Test KST SIGNAL with specified lengths and signal length of 15.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KST SIGNAL.
        """

        roc_length_1 = 8
        roc_length_2 = 17
        roc_length_3 = 23
        roc_length_4 = 40
        sma_length_1 = 12
        sma_length_2 = 14
        sma_length_3 = 17
        sma_length_4 = 10
        signal_length = 15
        source = SourceType.CLOSE.value

        trading_view_kst_signal = pd.Series([
            50.69, 56.36, 61.54, 65.98, 69.78, 73.01, 75.55, 77.39, 78.72, 79.63, 80.17, 80.5, 80.63, 80.51, 80.24,
            79.94, 79.62, 79.2, 78.77, 78.18
        ],
            name=f'KST-SIGNAL_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}_{signal_length}').reset_index(
            drop=True)
        calculated_kst_signal = kst_signal(
            series=self.data[source],
            roc_length_1=roc_length_1,
            roc_length_2=roc_length_2,
            roc_length_3=roc_length_3,
            roc_length_4=roc_length_4,
            sma_length_1=sma_length_1,
            sma_length_2=sma_length_2,
            sma_length_3=sma_length_3,
            sma_length_4=sma_length_4,
            signal_length=signal_length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kst_signal, trading_view_kst_signal)


    def test_kst_series_default_params_tradingview_data(self):
        """
        Test KST series with default params.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KST.
        """

        ticker = 'AAPL'
        roc_length_1 = 10
        roc_length_2 = 15
        roc_length_3 = 20
        roc_length_4 = 30
        sma_length_1 = 10
        sma_length_2 = 10
        sma_length_3 = 10
        sma_length_4 = 15
        source = SourceType.CLOSE.value

        trading_view_kst = pd.Series([
            81.31, 77.77, 76.27, 73.4, 71.5, 71.01, 69.25, 68.3, 69.42, 70.54,
            71.19, 71.95, 71.16, 70.25, 68.19, 65.02, 62.67, 58.88, 54.52, 48.74
        ],
            name=f'{ticker}_KST_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}').reset_index(
            drop=True)
        kst_series = KST(
            ticker=ticker,
            source=source,
            roc_length_1=roc_length_1,
            roc_length_2=roc_length_2,
            roc_length_3=roc_length_3,
            roc_length_4=roc_length_4,
            sma_length_1=sma_length_1,
            sma_length_2=sma_length_2,
            sma_length_3=sma_length_3,
            sma_length_4=sma_length_4
        )
        calculated_kst = kst_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kst, trading_view_kst)



    def test_kst_signal_series_default_params_tradingview_data(self):
        """
        Test KST SIGNAL series with default params.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places, and we use Close price to calculate KST SIGNAL.
        """

        ticker = 'AAPL'
        roc_length_1 = 10
        roc_length_2 = 15
        roc_length_3 = 20
        roc_length_4 = 30
        sma_length_1 = 10
        sma_length_2 = 10
        sma_length_3 = 10
        sma_length_4 = 15
        signal_length = 9
        source = SourceType.CLOSE.value

        trading_view_kst_signal = pd.Series([
            76.96, 78.92, 79.92, 79.93, 79.21, 78.1, 76.45, 74.67, 73.14, 71.94,
            71.21, 70.73, 70.48, 70.34, 70.03, 69.56, 68.93, 67.76, 65.98, 63.48
        ],
            name=f'{ticker}_KST-SIGNAL_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}_{signal_length}').reset_index(
            drop=True)
        kst_signal_series = KST_SIGNAL(
            ticker=ticker,
            source=source,
            roc_length_1=roc_length_1,
            roc_length_2=roc_length_2,
            roc_length_3=roc_length_3,
            roc_length_4=roc_length_4,
            sma_length_1=sma_length_1,
            sma_length_2=sma_length_2,
            sma_length_3=sma_length_3,
            sma_length_4=sma_length_4,
            signal_length=signal_length
        )
        calculated_kst_signal = kst_signal_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_kst_signal, trading_view_kst_signal)
