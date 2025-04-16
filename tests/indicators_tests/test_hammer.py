import os.path
import unittest
import pandas as pd
import numpy as np
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.candlestick_patterns.hammer import hammer


class TestHammer(unittest.TestCase):

    def setUp(self):
        """
        Testing on AAPL stock from 2020-1-1 until 2024-1-1
        """
        self.data = pd.read_csv(os.path.join('testing_data', 'AAPL_testing_data.csv'))
        self.downloader = DownloadModule(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2024, 1, 1)
        )

    def test_detects_known_hammer(self):
        # Arrange
        df = pd.DataFrame({
            SourceType.HIGH.value: [105],
            SourceType.LOW.value: [90],
            SourceType.OPEN.value: [104],
            SourceType.CLOSE.value: [103.5]
        })
        expected = pd.Series([False], name='HAMMER-CANDLESTICK-PATTERN')

        # Act
        result = hammer(
            df[SourceType.HIGH.value],
            df[SourceType.LOW.value],
            df[SourceType.OPEN.value],
            df[SourceType.CLOSE.value]
        )

        # Assert
        pd.testing.assert_series_equal(result.reset_index(drop=True), expected)

    def test_does_not_detect_false_pattern(self):
        # Arrange
        df = pd.DataFrame({
            SourceType.HIGH.value: [105],
            SourceType.LOW.value: [100],
            SourceType.OPEN.value: [101],
            SourceType.CLOSE.value: [102]
        })
        expected = pd.Series([False], name='HAMMER-CANDLESTICK-PATTERN')

        # Act
        result = hammer(
            df[SourceType.HIGH.value],
            df[SourceType.LOW.value],
            df[SourceType.OPEN.value],
            df[SourceType.CLOSE.value]
        )

        # Assert
        pd.testing.assert_series_equal(result.reset_index(drop=True), expected)

    def test_multiple_mixed_patterns(self):
        # Arrange
        df = pd.DataFrame({
            SourceType.HIGH.value: [110, 120, 130],
            SourceType.LOW.value: [90, 100, 120],
            SourceType.OPEN.value: [109, 119, 129],
            SourceType.CLOSE.value: [109, 117, 128]
        })
        expected = pd.Series([False, False, False], name='HAMMER-CANDLESTICK-PATTERN')

        # Act
        result = hammer(
            df[SourceType.HIGH.value],
            df[SourceType.LOW.value],
            df[SourceType.OPEN.value],
            df[SourceType.CLOSE.value]
        )

        # Assert
        pd.testing.assert_series_equal(result.reset_index(drop=True), expected)

    def test_handles_missing_data(self):
        # Arrange
        df = pd.DataFrame({
            SourceType.HIGH.value: [105, np.nan],
            SourceType.LOW.value: [90, 95],
            SourceType.OPEN.value: [104, 97],
            SourceType.CLOSE.value: [103.5, np.nan]
        })
        expected = pd.Series([False, False], name='HAMMER-CANDLESTICK-PATTERN')

        # Act
        result = hammer(
            df[SourceType.HIGH.value],
            df[SourceType.LOW.value],
            df[SourceType.OPEN.value],
            df[SourceType.CLOSE.value]
        )

        # Assert
        pd.testing.assert_series_equal(result.reset_index(drop=True), expected)

    def test_output_series_name(self):
        # Arrange
        df = pd.DataFrame({
            SourceType.HIGH.value: [105],
            SourceType.LOW.value: [90],
            SourceType.OPEN.value: [104],
            SourceType.CLOSE.value: [103.5]
        })

        # Act
        result = hammer(
            df[SourceType.HIGH.value],
            df[SourceType.LOW.value],
            df[SourceType.OPEN.value],
            df[SourceType.CLOSE.value]
        )

        # Assert
        self.assertEqual(result.name, 'HAMMER-CANDLESTICK-PATTERN')


if __name__ == '__main__':
    unittest.main()
