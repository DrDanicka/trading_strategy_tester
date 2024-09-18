import random
import unittest

import numpy as np
import pandas as pd

from trading_strategy_tester.conditions.logical_conditions.or_condition import OrCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.conditions.test_condition import TestCondition
from trading_strategy_tester.trading_series.testing_series import TestingSeries

class TestOrCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame(index=np.arange(5))

    def test_or_condition_one_false(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter1 = random.randint(1, 100)
        test_parameter2 = random.randint(1, 100)
        test_parameter3 = random.randint(1, 100)
        expected_signal1 = f'TestCondition({ticker}_TEST_{test_parameter1})'
        expected_signal2 = f'TestCondition({ticker}_TEST_{test_parameter2})'
        expected_signal3 = f'TestCondition({ticker}_TEST_{test_parameter3})'

        expected_or = pd.Series([True, True, False, True, True])
        expected_signal_series = pd.Series([expected_signal1, expected_signal3, None, expected_signal2, expected_signal3])

        or_condition, signal_series = OrCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, False, False, False]), test_parameter1
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, False, True, False]), test_parameter2
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, True, False, True, True]), test_parameter3
                )
            )
        ).evaluate(self.downloader, self.df)


        pd.testing.assert_series_equal(or_condition, expected_or)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_or_condition_non_true(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter = random.randint(1, 100)

        expected_or = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        or_condition, signal_series = OrCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, False, False]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, False, False]), test_parameter
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, False, False]), test_parameter
                )
            )
        ).evaluate(self.downloader, self.df)

        pd.testing.assert_series_equal(or_condition, expected_or)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_or_condition_all_true(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter1 = random.randint(1, 100)
        test_parameter2 = random.randint(1, 100)
        test_parameter3 = random.randint(1, 100)
        expected_signal1 = f'TestCondition({ticker}_TEST_{test_parameter1})'
        expected_signal2 = f'TestCondition({ticker}_TEST_{test_parameter2})'
        expected_signal3 = f'TestCondition({ticker}_TEST_{test_parameter3})'

        expected_or = pd.Series([True, True, True, True, True])
        expected_signal_series = pd.Series(
            [expected_signal2, expected_signal3, expected_signal2, expected_signal3, expected_signal2])

        or_condition, signal_series = OrCondition(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, False, False]), test_parameter1
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, True, False, True]), test_parameter2
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, True, True, True, True]), test_parameter3
                )
            )
        ).evaluate(self.downloader, self.df)

        pd.testing.assert_series_equal(or_condition, expected_or)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

if __name__ == '__main__':
    unittest.main()