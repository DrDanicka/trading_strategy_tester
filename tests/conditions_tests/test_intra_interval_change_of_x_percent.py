import random
import unittest

import numpy as np
import pandas as pd

from trading_strategy_tester.conditions.parameterized_conditions.intra_interval_change_of_x_percent_condition import IntraIntervalChangeOfXPercentCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries

class TestChangeOfXPercentOnYDays(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame(index=np.arange(6))

    def test_change_of_10_percent(self):
        # Arrange
        ticker = 'AAPL'
        percent = 10
        test_parameter = random.randint(1, 100)
        expected_signal = f'IntraIntervalChangeOfXPercentSignal({percent}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, False, True, False, False])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = IntraIntervalChangeOfXPercentCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 104, 110, 121, 90, 60]),
                test_parameter
            ),
            percent
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_5_percent_multiple(self):
        # Arrange
        ticker = 'AAPL'
        percent = 5
        test_parameter = random.randint(1, 100)
        expected_signal = f'IntraIntervalChangeOfXPercentSignal({percent}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, True, True, False, True])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = IntraIntervalChangeOfXPercentCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 104, 110, 121, 90, 100]),
                test_parameter
            ),
            percent
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_negative_5_percent(self):
        # Arrange
        ticker = 'AAPL'
        percent = -5
        test_parameter = random.randint(1, 100)
        expected_signal = f'IntraIntervalChangeOfXPercentSignal({percent}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, True, False, False, False])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = IntraIntervalChangeOfXPercentCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 100, 95, 121, 116, 112]),
                test_parameter
            ),
            percent
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_negative_10_percent_multiple(self):
        # Arrange
        ticker = 'AAPL'
        percent = -10
        test_parameter = random.randint(1, 100)
        expected_signal = f'IntraIntervalChangeOfXPercentSignal({percent}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, True, False, True, True])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = IntraIntervalChangeOfXPercentCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 104, 92, 121, 90, 60]),
                test_parameter
            ),
            percent
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_to_string(self):
        # Arrange
        ticker = 'AAPL'
        percent = 10
        test_parameter = random.randint(1, 100)

        expected_string = f'IntraIntervalChangeOfXPercentCondition({percent}, {ticker}_TEST_{test_parameter})'

        # Act
        condition = IntraIntervalChangeOfXPercentCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 104, 110, 121, 90, 60]),
                test_parameter
            ),
            percent
        )

        # Assert
        self.assertEqual(condition.to_string(), expected_string)

if __name__ == '__main__':
    unittest.main()