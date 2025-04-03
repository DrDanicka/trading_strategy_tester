import unittest
import ast
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.validation.parameter_validations.period_validator import validate_period


class TestValidatePeriod(unittest.TestCase):

    def test_valid_period(self):
        # Arrange: Valid period value
        period = ast.Attribute(value=ast.Name(id='Period', ctx=ast.Load()), attr='ONE_DAY', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_period, updated_changes = validate_period(period, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_period)
        self.assertEqual(updated_changes, {})

    def test_valid_period_other(self):
        # Arrange: Valid period value (other than 'ONE_DAY')
        period = ast.Attribute(value=ast.Name(id='Period', ctx=ast.Load()), attr='FIVE_DAYS', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_period, updated_changes = validate_period(period, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_period)
        self.assertEqual(updated_changes, {})

    def test_invalid_period_enum(self):
        # Arrange: Invalid period enum (not 'Period')
        period = ast.Attribute(value=ast.Name(id='InvalidEnum', ctx=ast.Load()), attr='ONE_DAY', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_period, updated_changes = validate_period(period, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_period, Period.NOT_PASSED)  # Default period
        self.assertIn('period', updated_changes)
        self.assertEqual(updated_changes['period'],
                         "period argument should be of type Period. Defaulting to no period.")


    def test_invalid_period_attr(self):
        # Arrange: Invalid period attribute (not in the valid list)
        period = ast.Attribute(value=ast.Name(id='Period', ctx=ast.Load()), attr='INVALID', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_period, updated_changes = validate_period(period, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_period, Period.NOT_PASSED)  # Default period
        self.assertIn('period', updated_changes)
        self.assertEqual(updated_changes['period'],
                         "Valid periods are: ONE_DAY, FIVE_DAYS, ONE_MONTH, THREE_MONTHS, SIX_MONTHS, ONE_YEAR, "
                         "TWO_YEARS, FIVE_YEARS, TEN_YEARS, YEAR_TO_DATE, MAX, NOT_PASSED. Defaulting to no period.")


    def test_invalid_type_for_period(self):
        # Arrange: period is a string instead of an ast.Attribute
        period = 'ONE_DAY'
        changes = {}
        logs = False

        # Act
        result, new_period, updated_changes = validate_period(period, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_period, Period.NOT_PASSED)  # Default period
        self.assertIn('period', updated_changes)


if __name__ == '__main__':
    unittest.main()
