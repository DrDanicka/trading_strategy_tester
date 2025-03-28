import unittest

import pandas as pd
import numpy as np

from trading_strategy_tester.conditions.threshold_conditions.cross_under_condition import CrossUnderCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries


class TestCrossUnderCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame()

    def test_single_cross_under(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 12
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([2, 1, 4, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, True, False, False, False])
        expected_signal_series = pd.Series([None, expected_signal, None, None, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_no_cross_under(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 12
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([2, 3, 4, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_two_cross_under(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 7
        series2_test_parameter = 8
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([2, 1, 4, 2, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, True, False, True, False])
        expected_signal_series = pd.Series([None, expected_signal, None, expected_signal, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_one_cross_under_with_value_equality(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 7
        series2_test_parameter = 8
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([2, 1, 4, 4, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, True, False, False, False])
        expected_signal_series = pd.Series([None, expected_signal, None, None, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_equal_values(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 7
        series2_test_parameter = 8
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_cross_under_condition_with_nan_in_series1(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 7
        series2_test_parameter = 8
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([np.nan, np.nan, 4, 2, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, False, False, True, False])
        expected_signal_series = pd.Series([None, None, None, expected_signal, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_cross_under_condition_with_nan_in_series2(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 7
        series2_test_parameter = 8
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([1, 2, 4, 2, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([np.nan, np.nan, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, False, False, True, False])
        expected_signal_series = pd.Series([None, None, None, expected_signal, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_cross_over_in_cross_under_condition(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 7
        series2_test_parameter = 8
        expected_signal = f'CrossUnderSignal({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        series1 = TestingSeries(ticker, pd.Series([0, 1, 4, 5, 6]), series1_test_parameter)
        series2 = TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)

        expected_cross_under = pd.Series([False, False, False, False, False])
        expected_signal_series = pd.Series([None, None, None, None, None])

        # Act
        cross_under, signal_series = CrossUnderCondition(series1, series2).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(cross_under, expected_cross_under)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)

    def test_to_string(self):
        # Arrange
        ticker = 'AAPL'
        series1_test_parameter = 9
        series2_test_parameter = 33

        expected_string = f'CrossUnderCondition({ticker}_TEST_{series1_test_parameter}, {ticker}_TEST_{series2_test_parameter})'

        # Act
        condition = CrossUnderCondition(
            TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series1_test_parameter),
            TestingSeries(ticker, pd.Series([1, 2, 3, 4, 5]), series2_test_parameter)
        )

        # Assert
        self.assertEqual(condition.to_string(), expected_string)

if __name__ == '__main__':
    unittest.main()