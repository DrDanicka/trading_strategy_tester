import unittest
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.position_types.long import Long
from trading_strategy_tester.position_types.short import Short
from trading_strategy_tester.position_types.long_short_combination import LongShortCombination
from trading_strategy_tester.utils.validations import (
    get_length,
    get_offset,
    get_std_dev,
    get_base_sources,
    get_position_type_from_enum
)


class TestValidationUtils(unittest.TestCase):

    # ---- get_length ----
    def test_get_length_valid(self):
        self.assertEqual(get_length(10, 5), 10)

    def test_get_length_invalid_type(self):
        self.assertEqual(get_length("10", 5), 5)

    def test_get_length_negative(self):
        self.assertEqual(get_length(-1, 7), 7)

    def test_get_length_zero(self):
        self.assertEqual(get_length(0, 3), 3)

    # ---- get_offset ----
    def test_get_offset_valid(self):
        self.assertEqual(get_offset(5), 5)

    def test_get_offset_negative(self):
        self.assertEqual(get_offset(-2), 0)

    def test_get_offset_invalid_type(self):
        self.assertEqual(get_offset("4"), 0)

    def test_get_offset_zero(self):
        self.assertEqual(get_offset(0), 0)

    # ---- get_std_dev ----
    def test_get_std_dev_valid(self):
        self.assertEqual(get_std_dev(1.5, 0.5), 1.5)

    def test_get_std_dev_zero(self):
        self.assertEqual(get_std_dev(0.0, 0.2), 0.2)

    def test_get_std_dev_negative(self):
        self.assertEqual(get_std_dev(-1.0, 0.1), 0.1)

    # ---- get_base_sources ----
    def test_get_base_sources_valid(self):
        self.assertEqual(get_base_sources(SourceType.CLOSE, SourceType.OPEN), SourceType.CLOSE)

    def test_get_base_sources_invalid_custom_enum(self):
        self.assertEqual(get_base_sources(SourceType.HLCC4, SourceType.LOW), SourceType.LOW)

    # ---- get_position_type_from_enum ----
    def test_position_type_long(self):
        result = get_position_type_from_enum(PositionTypeEnum.LONG)
        self.assertIsInstance(result, Long)

    def test_position_type_short(self):
        result = get_position_type_from_enum(PositionTypeEnum.SHORT)
        self.assertIsInstance(result, Short)

    def test_position_type_combination_default(self):
        class FakeEnum:
            pass
        result = get_position_type_from_enum(FakeEnum())
        self.assertIsInstance(result, LongShortCombination)


