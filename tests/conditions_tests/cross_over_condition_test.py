import unittest

import pandas as pd

from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries


class TestCrossOverCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame()

    def test_single_cross_over(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 12
        expected_signal = f'CrossOverSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([0, 3, 4, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_crossover = pd.Series([False, True, False, False, False])
        expected_signal_series = pd.Series([None, expected_signal, None, None, None])

        # Act
        crossover, signal_series = CrossOverCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(crossover, expected_crossover)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_no_cross_over(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 10
        series2_test_parameter = 23

        series1 = TestingSeries(ticker, pd.Series([2, 3, 4, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_crossover = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        # Act
        crossover, signal_series = CrossOverCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(crossover, expected_crossover)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_two_cross_over(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 7
        series2_test_parameter = 8
        expected_signal = f'CrossOverSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([0, 3, 2, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_crossover = pd.Series([False, True, False, True, False])
        expected_signal_series = pd.Series([None, expected_signal, None, expected_signal, None])

        # Act
        crossover, signal_series = CrossOverCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(crossover, expected_crossover)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_one_cross_over_with_value_equality(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 90
        expected_signal = f'CrossOverSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([0, 3, 3, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_crossover = pd.Series([False, True, False, False, False])
        expected_signal_series = pd.Series([None, expected_signal, None, None, None])

        # Act
        crossover, signal_series = CrossOverCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(crossover, expected_crossover)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_equal_values(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 33

        series1 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_crossover = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        # Act
        crossover, signal_series = CrossOverCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(crossover, expected_crossover)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_cross_over_condition_with_nan_in_series1(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 33
        expected_signal = f'CrossOverSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([None, None, 2, 5, 5]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_crossover = pd.Series([False, False, False, True, False])
        expected_signal_series = pd.Series([None, None, None, expected_signal, None])

        # Act
        crossover, signal_series = CrossOverCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(crossover, expected_crossover)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_cross_over_condition_with_nan_in_series2(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 33
        expected_signal = f'CrossOverSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([1, 2, 2, 5, 5]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([None, None, 3, 4, 5]), series2_test_parameter)

        expected_crossover = pd.Series([False, False, False, True, False])
        expected_signal_series = pd.Series([None, None, None, expected_signal, None])

        # Act
        crossover, signal_series = CrossOverCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(crossover, expected_crossover)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

if __name__ == '__main__':
    unittest.main()