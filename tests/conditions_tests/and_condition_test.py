import random
import unittest

import numpy as np
import pandas as pd

from trading_strategy_tester.conditions.logical_conditions.and_condition import AndCondition
from trading_strategy_tester.conditions.test_condition import TestCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries


class TestAndCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame(index=np.arange(5))

    def test_and_condition_one_true(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter = random.randint(1, 100)
        expected_signal = f'And(TestCondition({ticker}_TEST_{test_parameter}), TestCondition({ticker}_TEST_{test_parameter}), TestCondition({ticker}_TEST_{test_parameter}))'

        expected_and = pd.Series([True, False, False, False, False])
        expected_signal_series = pd.Series([expected_signal, None, None, None, None])

        # Act
        and_condition, signal_series = AndCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, False, True, False]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, False, False]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, True, True]), test_parameter
                )
            )
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(and_condition, expected_and)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_and_condition_multiple_true(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter = random.randint(1, 100)
        expected_signal = f'And(TestCondition({ticker}_TEST_{test_parameter}), TestCondition({ticker}_TEST_{test_parameter}), TestCondition({ticker}_TEST_{test_parameter}))'

        expected_and = pd.Series([True, False, False, True, False])
        expected_signal_series = pd.Series([expected_signal, None, None, expected_signal, None])

        # Act
        and_condition, signal_series = AndCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, False, True, False]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, True, True]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, True, True]), test_parameter
                )
            )
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(and_condition, expected_and)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_and_condition_none_true(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter = random.randint(1, 100)

        expected_and = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        # Act
        and_condition, signal_series = AndCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, True, False]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, False, True]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, True, True]), test_parameter
                )
            )
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(and_condition, expected_and)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

if __name__ == '__main__':
    unittest.main()