import random
import unittest

import numpy as np
import pandas as pd

from trading_strategy_tester.conditions.logical_conditions.if_then_else_condition import IfThenElse
from trading_strategy_tester.conditions.test_condition import TestCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries

class TestIfThenElseCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame(index=np.arange(5))

    def test_if_then_else_condition_only_if(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter1 = random.randint(1, 100)
        test_parameter2 = random.randint(1, 100)
        expected_signal1 = f'TestCondition({ticker}_TEST_{test_parameter1})'
        expected_signal2 = f'TestCondition({ticker}_TEST_{test_parameter2})'

        expected_if_then_else = pd.Series([True, False, False, True, False])
        expected_signal_series = pd.Series([expected_signal1, None, None, expected_signal1, None])

        if_then_else_condition, signal_series = IfThenElse(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, False, True, False]), test_parameter1
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, False, False]), test_parameter2
                )
            )
        ).evaluate(self.downloader, self.df)

        pd.testing.assert_series_equal(if_then_else_condition, expected_if_then_else)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_if_then_else_condition_both_if_else(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter1 = random.randint(1, 100)
        test_parameter2 = random.randint(1, 100)
        expected_signal1 = f'TestCondition({ticker}_TEST_{test_parameter1})'
        expected_signal2 = f'TestCondition({ticker}_TEST_{test_parameter2})'

        expected_if_then_else = pd.Series([True, True, False, True, False])
        expected_signal_series = pd.Series([expected_signal1, expected_signal2, None, expected_signal1, None])

        if_then_else_condition, signal_series = IfThenElse(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, False, True, False]), test_parameter1
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, True, False, False, False]), test_parameter2
                )
            )
        ).evaluate(self.downloader, self.df)

        pd.testing.assert_series_equal(if_then_else_condition, expected_if_then_else)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_if_then_else_condition_all_false(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter1 = random.randint(1, 100)
        test_parameter2 = random.randint(1, 100)
        expected_signal1 = f'TestCondition({ticker}_TEST_{test_parameter1})'
        expected_signal2 = f'TestCondition({ticker}_TEST_{test_parameter2})'

        expected_if_then_else = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        if_then_else_condition, signal_series = IfThenElse(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, False, False]), test_parameter1
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([False, False, False, False, False]), test_parameter2
                )
            )
        ).evaluate(self.downloader, self.df)

        pd.testing.assert_series_equal(if_then_else_condition, expected_if_then_else)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_if_then_else_condition_if_else_true_cover(self):
        # Arrange
        ticker = 'AAPL'
        test_parameter1 = random.randint(1, 100)
        test_parameter2 = random.randint(1, 100)
        expected_signal1 = f'TestCondition({ticker}_TEST_{test_parameter1})'
        expected_signal2 = f'TestCondition({ticker}_TEST_{test_parameter2})'

        expected_if_then_else = pd.Series([True, True, False, True, False])
        expected_signal_series = pd.Series([expected_signal1, expected_signal2, None, expected_signal1, None])

        if_then_else_condition, signal_series = IfThenElse(
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, False, False, True, False]), test_parameter1
                )
            ),
            TestCondition(
                TestingSeries(
                    ticker, pd.Series([True, True, False, False, False]), test_parameter2
                )
            )
        ).evaluate(self.downloader, self.df)

        pd.testing.assert_series_equal(if_then_else_condition, expected_if_then_else)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

if __name__ == '__main__':
    unittest.main()