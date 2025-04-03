import unittest
import ast
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.validation.parameter_validations.interval_validator import validate_interval


class TestValidateInterval(unittest.TestCase):

    def test_valid_interval(self):
        # Arrange
        interval = ast.Attribute(value=ast.Name(id='Interval', ctx=ast.Load()), attr='ONE_DAY', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_interval, updated_changes = validate_interval(interval, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_interval)
        self.assertEqual(updated_changes, {})

    def test_invalid_interval_enum(self):
        # Arrange
        interval = ast.Attribute(value=ast.Name(id='InvalidEnum', ctx=ast.Load()), attr='ONE_DAY', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_interval, updated_changes = validate_interval(interval, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_interval, Interval.ONE_DAY)
        self.assertIn('interval', updated_changes)
        self.assertEqual(updated_changes['interval'],
                         "interval argument should be of type Interval. Defaulting to Interval.ONE_DAY.")

    def test_invalid_interval_attr(self):
        # Arrange
        interval = ast.Attribute(value=ast.Name(id='Interval', ctx=ast.Load()), attr='INVALID', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_interval, updated_changes = validate_interval(interval, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_interval, Interval.ONE_DAY)
        self.assertIn('interval', updated_changes)
        self.assertEqual(updated_changes['interval'],
                         "Valid intervals are: ONE_DAY, FIVE_DAYS, ONE_WEEK, ONE_MONTH, THREE_MONTHS. Defaulting to Interval.ONE_DAY.")

    def test_invalid_type_for_interval(self):
        # Arrange
        interval = 'ONE_DAY'
        changes = {}
        logs = False

        # Act
        result, new_interval, updated_changes = validate_interval(interval, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_interval, Interval.ONE_DAY)
        self.assertIn('interval', updated_changes)


if __name__ == '__main__':
    unittest.main()
