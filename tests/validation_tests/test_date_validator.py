import unittest
import ast
from datetime import datetime
from trading_strategy_tester.validation.parameter_validations.date_validator import validate_date


class TestValidateDate(unittest.TestCase):

    def test_valid_date_with_ast_call(self):
        # Arrange
        date = ast.Call(func=ast.Name(id='datetime', ctx=ast.Load()),
                        args=[ast.Constant(value=2024), ast.Constant(value=1), ast.Constant(value=1)],
                        keywords=[])
        changes = {}
        logs = False
        start = True

        # Act
        result, new_date, updated_changes = validate_date(date, changes, logs, start)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_date)
        self.assertEqual(updated_changes, {})

    def test_invalid_date_with_ast_call(self):
        # Arrange
        date = ast.Call(func=ast.Name(id='datetime', ctx=ast.Load()),
                        args=[ast.Constant(value=2024), ast.Constant(value=13), ast.Constant(value=1)],
                        keywords=[])
        changes = {}
        logs = False
        start = True

        # Act
        result, new_date, updated_changes = validate_date(date, changes, logs, start)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_date, datetime(2024, 1, 1))
        self.assertIn('start_date', updated_changes)
        self.assertEqual(updated_changes['start_date'],
                         "Date argument should be of type datetime. Using default date '2024-01-01'.")

    def test_future_date_with_ast_call(self):
        # Arrange
        date = ast.Call(func=ast.Name(id='datetime', ctx=ast.Load()),
                        args=[ast.Constant(value=2050), ast.Constant(value=1), ast.Constant(value=1)],
                        keywords=[])
        changes = {}
        logs = False
        start = True

        # Act
        result, new_date, updated_changes = validate_date(date, changes, logs, start)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_date, datetime(2024, 1, 1))
        self.assertIn('start_date', updated_changes)
        self.assertEqual(updated_changes['start_date'],
                         "Date argument should be a date in the past. Using default date '2024-01-01'.")

    def test_invalid_type_for_date(self):
        # Arrange
        date = '2024-01-01'
        changes = {}
        logs = False
        start = True

        # Act
        result, new_date, updated_changes = validate_date(date, changes, logs, start)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_date, datetime(2024, 1, 1))
        self.assertIn('start_date', updated_changes)


    def test_invalid_type_for_date_start_true(self):
        # Arrange
        date = '2024-01-01'
        changes = {}
        logs = False
        start = False

        # Act
        result, new_date, updated_changes = validate_date(date, changes, logs, start)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_date.year, datetime.today().year)
        self.assertEqual(new_date.month, datetime.today().month)
        self.assertEqual(new_date.day, datetime.today().day)
        self.assertIn('end_date', updated_changes)


    def test_not_datetime_object(self):
        # Arrange
        date = ast.Call(func=ast.Name(id='invalid', ctx=ast.Load()),
                        args=[ast.Constant(value=2024), ast.Constant(value=1), ast.Constant(value=1)],
                        keywords=[])
        changes = {}
        logs = False
        start = True

        # Act
        result, new_date, updated_changes = validate_date(date, changes, logs, start)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_date, datetime(2024, 1, 1))
        self.assertIn('start_date', updated_changes)


if __name__ == '__main__':
    unittest.main()
