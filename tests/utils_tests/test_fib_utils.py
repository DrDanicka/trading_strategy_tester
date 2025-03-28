import unittest
import pandas as pd

from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.utils.fib_utils import is_in_fib_interval


class TestFibonacciUtils(unittest.TestCase):

    def test_uptrend_fib_level_0_true_lower_case(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_0
        row_data = pd.Series({SourceType.LOW.value: 101, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)


    def test_uptrend_fib_level_0_true_upper_case(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_0
        row_data = pd.Series({SourceType.LOW.value: 199, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)


    def test_downtrend_fib_level_0_true_lower_case(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_0
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 101})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)


    def test_downtrend_fib_level_0_true_upper_case(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_0
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 199})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)


    def test_uptrend_fib_level_0_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_0
        row_data = pd.Series({SourceType.LOW.value: 201, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)


    def test_downtrend_fib_level_0_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_0
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 99})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)


    def test_uptrend_fib_level_23_6_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_23_6
        row_data = pd.Series({SourceType.LOW.value: 176, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_uptrend_fib_level_23_6_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_23_6
        row_data = pd.Series({SourceType.LOW.value: 177, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)


    def test_downtrend_fib_level_23_6_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_23_6
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 124})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)


    def test_downtrend_fib_level_23_6_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_23_6
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 123})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)


    def test_uptrend_fib_level_38_2_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_38_2
        row_data = pd.Series({SourceType.LOW.value: 161, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_uptrend_fib_level_38_2_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_38_2
        row_data = pd.Series({SourceType.LOW.value: 162, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)


    def test_downtrend_fib_level_38_2_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_38_2
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 139})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)


    def test_downtrend_fib_level_38_2_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_38_2
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 138})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)

    def test_uptrend_fib_level_50_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_50
        row_data = pd.Series({SourceType.LOW.value: 149, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_uptrend_fib_level_50_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_50
        row_data = pd.Series({SourceType.LOW.value: 151, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)

    def test_downtrend_fib_level_50_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_50
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 151})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_downtrend_fib_level_50_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_50
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 149})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)


    def test_uptrend_fib_level_61_8_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_61_8
        row_data = pd.Series({SourceType.LOW.value: 138, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_uptrend_fib_level_61_8_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_61_8
        row_data = pd.Series({SourceType.LOW.value: 139, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)

    def test_downtrend_fib_level_61_8_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_61_8
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 162})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_downtrend_fib_level_61_8_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_61_8
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 161})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)

    def test_uptrend_fib_level_100_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_100
        row_data = pd.Series({SourceType.LOW.value: 101, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_uptrend_fib_level_100_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = True
        fib_level = FibonacciLevels.LEVEL_100
        row_data = pd.Series({SourceType.LOW.value: 99, SourceType.HIGH.value: 300})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)

    def test_downtrend_fib_level_100_true(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_100
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 199})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertTrue(result)

    def test_downtrend_fib_level_100_false(self):
        # Arrange
        high = 200
        low = 100
        uptrend = False
        fib_level = FibonacciLevels.LEVEL_100
        row_data = pd.Series({SourceType.LOW.value: 80, SourceType.HIGH.value: 201})

        # Act
        result = is_in_fib_interval(high, low, row_data, fib_level, uptrend=uptrend)

        # Assert
        self.assertFalse(result)
