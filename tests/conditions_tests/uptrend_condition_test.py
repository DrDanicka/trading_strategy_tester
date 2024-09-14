import random
import unittest

import pandas as pd

from trading_strategy_tester.conditions.uptrend_for_x_days import UptrendForXDaysCondition
from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.trading_series.testing_series import TestingSeries

class TestUptrendCondition(unittest.TestCase):

    def setUp(self):
        self.downloader = DownloadModule()
        self.df = pd.DataFrame()

    def test_uptrend_for_2_days(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 2
        test_parameter = random.randint(1, 100)
        expected_signal = f'UptrendForXDaysSignal({number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_uptrend = pd.Series([False, True, True, True, True, False, True, True, True, False])
        expected_signal_series = expected_uptrend.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        uptrend_series, signal_series = UptrendForXDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([1, 2, 3, 4, 6, 2, 4, 5, 6, 4]),
                test_parameter
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(uptrend_series, expected_uptrend)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_uptrend_for_6_days(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 6
        test_parameter = random.randint(1, 100)
        expected_signal = f'UptrendForXDaysSignal({number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_uptrend = pd.Series([False, False, False, False, False, True, True, False, False, False, False, False])
        expected_signal_series = expected_uptrend.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        uptrend_series, signal_series = UptrendForXDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([1, 2, 3, 4, 5, 6, 7, 3, 9, 10, 11, 12]),
                test_parameter
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(uptrend_series, expected_uptrend)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


    def test_uptrend_for_4_days_with_non_decreasing_values(self):
        # Arrange
        ticker = 'AAPL'
        number_of_days = 4
        test_parameter = random.randint(1, 100)
        expected_signal = f'UptrendForXDaysSignal({number_of_days}, {ticker}_TEST_{test_parameter})'

        expected_uptrend = pd.Series([False, False, False, True, True, False, False, False, True, True, False, False])
        expected_signal_series = expected_uptrend.apply(
            lambda x: expected_signal if x else None
        )

        # Act
        uptrend_series, signal_series = UptrendForXDaysCondition(
            TestingSeries(
                ticker,
                pd.Series([1, 2, 2, 4, 5, 1, 7, 8, 9, 10, 3, 12]),
                test_parameter
            ),
            number_of_days
        ).evaluate(self.downloader, self.df)

        # Assert
        pd.testing.assert_series_equal(uptrend_series, expected_uptrend)
        pd.testing.assert_series_equal(signal_series, expected_signal_series)


if __name__ == '__main__':
    unittest.main()