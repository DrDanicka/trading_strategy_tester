import unittest
import ast
from trading_strategy_tester.validation.parameter_validations.capital_validator import validate_initial_capital


class TestValidateInitialCapital(unittest.TestCase):

    def test_valid_initial_capital(self):
        # Arrange
        initial_capital = ast.Constant(value=1000000)
        changes = {}
        logs = False

        # Act
        result, new_initial_capital, updated_changes = validate_initial_capital(initial_capital, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_initial_capital)
        self.assertEqual(updated_changes, {})

    def test_valid_initial_capital_float(self):
        # Arrange
        initial_capital = ast.Constant(value=1000000.50)
        changes = {}
        logs = False

        # Act
        result, new_initial_capital, updated_changes = validate_initial_capital(initial_capital, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_initial_capital)
        self.assertEqual(updated_changes, {})

    def test_invalid_initial_capital(self):
        # Arrange: Invalid initial_capital (not a number)
        initial_capital = ast.Constant(value="invalid")
        changes = {}
        logs = False

        # Act
        result, new_initial_capital, updated_changes = validate_initial_capital(initial_capital, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_initial_capital, 1_000_000)
        self.assertIn('initial_capital', updated_changes)
        self.assertEqual(updated_changes['initial_capital'],
                         "initial_capital argument should be a number. Using default initial capital '1000000'.")

    def test_missing_value_attribute(self):
        # Arrange
        initial_capital = ast.Constant(value=None)
        changes = {}
        logs = False

        # Act
        result, new_initial_capital, updated_changes = validate_initial_capital(initial_capital, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_initial_capital, 1_000_000)  # Default initial capital
        self.assertIn('initial_capital', updated_changes)

    def test_invalid_type_for_initial_capital(self):
        # Arrange
        initial_capital = "1000000"
        changes = {}
        logs = False

        # Act
        result, new_initial_capital, updated_changes = validate_initial_capital(initial_capital, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_initial_capital, 1_000_000)  # Default initial capital
        self.assertIn('initial_capital', updated_changes)


if __name__ == '__main__':
    unittest.main()
