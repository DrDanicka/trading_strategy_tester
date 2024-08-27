import unittest

import numpy as np
import pandas as pd

from trading_strategy_tester.trading_series.testing_series import TestingSeries
from trading_strategy_tester.conditions.greater_than_condition import GreaterThanCondition
from trading_strategy_tester.download.download_module import DownloadModule

class TestGreaterThanCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame()

    def test_simple_greater_than_condition(self):
        # Arrange
        ticker = 'TSLA'
        series1_test_parameter = 9
        series2_test_parameter = 12
        expected_signal = f'GreaterThanSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([0, 3, 4, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_greater_than = pd.Series([False, True, True, True, True])
        expected_signal_series = pd.Series([None, expected_signal, expected_signal, expected_signal, expected_signal])

        # Act
        greater_than, signal_series = GreaterThanCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(greater_than, expected_greater_than)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_greater_than_condition_on_multiple_occasion(self):
        # Arrange
        ticker = 'TSLA'
        series1_test_parameter = 6
        series2_test_parameter = 17
        expected_signal = f'GreaterThanSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([0, 3, 1, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_greater_than = pd.Series([False, True, False, True, True])
        expected_signal_series = pd.Series([None, expected_signal, None, expected_signal, expected_signal])

        # Act
        greater_than, signal_series = GreaterThanCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(greater_than, expected_greater_than)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_greater_than_condition_without_cross(self):
        # Arrange
        ticker = 'TSLA'
        series1_test_parameter = 9
        series2_test_parameter = 12

        series1 = TestingSeries(ticker, pd.Series([0, 1, 2, 3, 4]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_greater_than = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        # Act
        greater_than, signal_series = GreaterThanCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(greater_than, expected_greater_than)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_greater_than_condition_all_the_time(self):
        # Arrange
        ticker = 'TSLA'
        series1_test_parameter = 67
        series2_test_parameter = 14
        expected_signal = f'GreaterThanSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([2, 3, 4, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_greater_than = pd.Series([True, True, True, True, True])
        expected_signal_series = pd.Series([expected_signal, expected_signal, expected_signal, expected_signal, expected_signal])

        # Act
        greater_than, signal_series = GreaterThanCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(greater_than, expected_greater_than)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_greater_than_condition_on_multiple_occasion_equaling_on_one(self):
        # Arrange
        ticker = 'TSLA'
        series1_test_parameter = 6
        series2_test_parameter = 13
        expected_signal = f'GreaterThanSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([0, 3, 3, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_greater_than = pd.Series([False, True, False, True, True])
        expected_signal_series = pd.Series([None, expected_signal, None, expected_signal, expected_signal])

        # Act
        greater_than, signal_series = GreaterThanCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(greater_than, expected_greater_than)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_greater_than_condition_with_nan_in_series1(self):
        # Arrange
        ticker = 'TSLA'
        series1_test_parameter = 6
        series2_test_parameter = 13
        expected_signal = f'GreaterThanSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([None, None, 3, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_greater_than = pd.Series([False, False, False, True, True])
        expected_signal_series = pd.Series([None, None, None, expected_signal, expected_signal])

        # Act
        greater_than, signal_series = GreaterThanCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(greater_than, expected_greater_than)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_greater_than_condition_with_nan_in_series2(self):
        # Arrange
        ticker = 'TSLA'
        series1_test_parameter = 66
        series2_test_parameter = 15
        expected_signal = f'GreaterThanSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([4, 5, 3, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([None, None, 3, 4, 5]), series2_test_parameter)

        expected_greater_than = pd.Series([False, False, False, True, True])
        expected_signal_series = pd.Series([None, None, None, expected_signal, expected_signal])

        # Act
        greater_than, signal_series = GreaterThanCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(greater_than, expected_greater_than)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

if __name__ == '__main__':
    unittest.main()