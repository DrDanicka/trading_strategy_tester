import random
import unittest

import numpy as np
import pandas as pd

from trading_strategy_tester.conditions.change_of_x_percent_per_y_days import ChangeOfXPercentPerYDaysCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries

class TestChangeOfXPercentPerYDays(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame(index=np.arange(6))

    def test_change_of_5_percent_per_2_days(self):
        # Arrange
        ticker = 'AAPL'
        percent = 5
        number_of_days = 2
        test_parameter = random.randint(1, 100)
        expected_signal = f'ChangeOfXPercentPerYDaysSignal({percent}, {number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, True, False, False, False])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = ChangeOfXPercentPerYDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 104, 110, 102, 90, 60]),
                test_parameter
            ),
            percent,
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_10_percent_per_3_days(self):
        # Arrange
        ticker = 'AAPL'
        percent = 10
        number_of_days = 3
        test_parameter = random.randint(1, 100)
        expected_signal = f'ChangeOfXPercentPerYDaysSignal({percent}, {number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, False, True, False, False])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = ChangeOfXPercentPerYDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 105, 110, 110, 90, 60]),
                test_parameter
            ),
            percent,
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_10_percent_per_3_days_multiple_trues(self):
        # Arrange
        ticker = 'AAPL'
        percent = 10
        number_of_days = 3
        test_parameter = random.randint(1, 100)
        expected_signal = f'ChangeOfXPercentPerYDaysSignal({percent}, {number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, False, True, False, True])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = ChangeOfXPercentPerYDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 140, 110, 110, 90, 130]),
                test_parameter
            ),
            percent,
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_10_percent_per_1_day(self):
        # Arrange
        ticker = 'AAPL'
        percent = 10
        number_of_days = 1
        test_parameter = random.randint(1, 100)
        expected_signal = f'ChangeOfXPercentPerYDaysSignal({percent}, {number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, False, True, False, False])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = ChangeOfXPercentPerYDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 105, 110, 125, 90, 60]),
                test_parameter
            ),
            percent,
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_negative_10_percent_per_2_days(self):
        # Arrange
        ticker = 'AAPL'
        percent = -10
        number_of_days = 2
        test_parameter = random.randint(1, 100)
        expected_signal = f'ChangeOfXPercentPerYDaysSignal({percent}, {number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, True, True, False, True])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = ChangeOfXPercentPerYDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 105, 90, 85, 90, 60]),
                test_parameter
            ),
            percent,
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_change_of_negative_5_percent_per_3_days(self):
        # Arrange
        ticker = 'AAPL'
        percent = -15
        number_of_days = 3
        test_parameter = random.randint(1, 100)
        expected_signal = f'ChangeOfXPercentPerYDaysSignal({percent}, {number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, False, True, False, False])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = ChangeOfXPercentPerYDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 50, 60, 70, 90, 60]),
                test_parameter
            ),
            percent,
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_change_of_10_percent_per_3_days_no_true(self):
        # Arrange
        ticker = 'AAPL'
        percent = 10
        number_of_days = 3
        test_parameter = random.randint(1, 100)
        expected_signal = f'ChangeOfXPercentPerYDaysSignal({percent}, {number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_result = pd.Series([False, False, False, False, False, False])
        expected_signal_series = expected_result.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        result, signal_series = ChangeOfXPercentPerYDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([100, 105, 110, 109, 90, 60]),
                test_parameter
            ),
            percent,
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(result, expected_result)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


if __name__ == '__main__':
    unittest.main()