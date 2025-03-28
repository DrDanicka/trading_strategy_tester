import unittest
import pandas as pd
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.utils.sources import get_source_series


class TestGetSourceSeries(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            SourceType.OPEN.value: [100, 105, 110],
            SourceType.HIGH.value: [110, 115, 120],
            SourceType.LOW.value: [90, 95, 100],
            'Close': [105, 110, 115],
        })

    def test_direct_sources(self):
        for source in [SourceType.OPEN, SourceType.HIGH, SourceType.LOW, SourceType.CLOSE]:
            with self.subTest(source=source):
                result = get_source_series(self.df, source)
                expected = self.df[source.value]
                pd.testing.assert_series_equal(result, expected)

    def test_hlc3(self):
        result = get_source_series(self.df, SourceType.HLC3)
        expected = (self.df[SourceType.HIGH.value] + self.df[SourceType.LOW.value] + self.df[SourceType.CLOSE.value]) / 3.0
        pd.testing.assert_series_equal(result, expected)

    def test_hl2(self):
        result = get_source_series(self.df, SourceType.HL2)
        expected = (self.df[SourceType.HIGH.value] + self.df[SourceType.LOW.value]) / 2.0
        pd.testing.assert_series_equal(result, expected)

    def test_hlcc4(self):
        result = get_source_series(self.df, SourceType.HLCC4)
        expected = (self.df[SourceType.HIGH.value] + self.df[SourceType.LOW.value] + 2 * self.df[SourceType.CLOSE.value]) / 4.0
        pd.testing.assert_series_equal(result, expected)


    def test_ohlc4(self):
        result = get_source_series(self.df, SourceType.OHLC4)
        expected = (self.df[SourceType.OPEN.value] + self.df[SourceType.HIGH.value] + self.df[SourceType.LOW.value] + self.df[SourceType.CLOSE.value]) / 4.0
        pd.testing.assert_series_equal(result, expected)

