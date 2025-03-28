import random
import unittest

import pandas as pd

from trading_strategy_tester.conditions.trend_conditions.downtrend_for_x_days_condition import DowntrendForXDaysCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries

class TestDowntrendCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame()

    def test_uptrend_for_2_days(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 2
        test_parameter = random.randint(1, 100)
        expected_signal = f'DowntrendForXDaysSignal({number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_uptrend = pd.Series([False, False, False, True, True, False, False, False, True, True])
        expected_signal_series = expected_uptrend.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        uptrend_series, signal_series = DowntrendForXDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([1, 2, 3, 2, 1, 2, 4, 5, 2, 1]),
                test_parameter
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(uptrend_series, expected_uptrend)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_uptrend_for_5_days(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 5
        test_parameter = random.randint(1, 100)
        expected_signal = f'DowntrendForXDaysSignal({number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_uptrend = pd.Series([False, False, False, False, True, False, False, False, False, False, True, True])
        expected_signal_series = expected_uptrend.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        uptrend_series, signal_series = DowntrendForXDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([12, 11, 10, 9, 8, 15, 16, 5, 4, 3, 2, 1]),
                test_parameter
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(uptrend_series, expected_uptrend)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_uptrend_for_4_days_with_non_ascending_values(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 4
        test_parameter = random.randint(1, 100)
        expected_signal = f'DowntrendForXDaysSignal({number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_uptrend = pd.Series([False, False, False, True, True, False, False, False, False, True, True, True])
        expected_signal_series = expected_uptrend.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        uptrend_series, signal_series = DowntrendForXDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([12, 11, 11, 9, 8, 15, 16, 5, 4, 2, 2, 1]),
                test_parameter
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(uptrend_series, expected_uptrend)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_to_string(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 2
        test_parameter = random.randint(1, 100)
        expected_signal = f'DowntrendForXDaysCondition({number_of_days}, {ticker}_TEST_{test_parameter})'

        # Act
        downtrend_condition = DowntrendForXDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([1, 2, 3, 2, 1, 2, 4, 5, 2, 1]),
                test_parameter
            ),
            number_of_days
        )

        # Assert
        self.assertEqual(downtrend_condition.to_string(), expected_signal)

if __name__ == '__main__':
    unittest.main()