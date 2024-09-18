import random
import unittest

import pandas as pd

from trading_strategy_tester.conditions.parameterized_conditions.after_x_days_condition import AfterXDaysCondition
from trading_strategy_tester.conditions.test_condition import TestCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries

class TestAfterXDaysCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame()

    def test_after_1_day_condition(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 1
        test_parameter = random.randint(1, 100)
        expected_signal = f'AfterXDaysSignal({number_of_days}, TestCondition({ticker}_TEST_{test_parameter}))'

        expected_after_x_days = pd.Series([False, True, True, False, False])
        expected_signal_series = pd.Series([None, expected_signal, expected_signal, None, None])

        # Act
        after_x_days, signal_series = AfterXDaysCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, True, False, False, False]), test_parameter
                )
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(after_x_days, expected_after_x_days)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_after_2_day_condition(self):
        # Arrange
        ticker = 'TSLA'
        number_of_days = 2
        test_parameter = random.randint(1, 100)
        expected_signal = f'AfterXDaysSignal({number_of_days}, TestCondition({ticker}_TEST_{test_parameter}))'

        expected_after_x_days = pd.Series([False, False, True, False, True])
        expected_signal_series = pd.Series([None, None, expected_signal, None, expected_signal])

        # Act
        after_x_days, signal_series = AfterXDaysCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, False, False]), test_parameter
                )
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(after_x_days, expected_after_x_days)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_after_0_day_condition(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 0
        test_parameter = random.randint(1, 100)
        expected_signal = f'AfterXDaysSignal({number_of_days}, TestCondition({ticker}_TEST_{test_parameter}))'

        expected_after_x_days = pd.Series([True, True, False, False, False])
        expected_signal_series = pd.Series([expected_signal, expected_signal, None, None, None])

        # Act
        after_x_days, signal_series = AfterXDaysCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, True, False, False, False]), test_parameter
                )
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(after_x_days, expected_after_x_days)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

if __name__ == '__main__':
    unittest.main()