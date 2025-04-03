import unittest
import ast
from trading_strategy_tester.trade.order_size.contracts import Contracts
from trading_strategy_tester.validation.parameter_validations.order_size_validator import validate_order_size


class TestValidateOrderSize(unittest.TestCase):

    def test_valid_order_size_contracts(self):
        # Arrange
        order_size = ast.Call(func=ast.Name(id='Contracts', ctx=ast.Load()), args=[ast.Constant(value=1)], keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_order_size, updated_changes = validate_order_size(order_size, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_order_size)
        self.assertEqual(updated_changes, {})

    def test_valid_order_size_usd(self):
        # Arrange
        order_size = ast.Call(func=ast.Name(id='USD', ctx=ast.Load()), args=[ast.Constant(value=1000)], keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_order_size, updated_changes = validate_order_size(order_size, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_order_size)
        self.assertEqual(updated_changes, {})

    def test_valid_order_size_percent_of_equity(self):
        # Arrange
        order_size = ast.Call(func=ast.Name(id='PercentOfEquity', ctx=ast.Load()), args=[ast.Constant(value=10)],
                              keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_order_size, updated_changes = validate_order_size(order_size, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_order_size)
        self.assertEqual(updated_changes, {})

    def test_invalid_order_size_type(self):
        # Arrange
        order_size = ast.Call(func=ast.Name(id='InvalidType', ctx=ast.Load()), args=[ast.Constant(value=10)],
                              keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_order_size, updated_changes = validate_order_size(order_size, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIn('order_size', updated_changes)
        self.assertEqual(updated_changes['order_size'],
                         "order_size argument should of type OrderSize. Available order sizes are: 'Contracts', 'USD', 'PercentOfEquity'. Using default order size 'Contracts(1)'.")

    def test_invalid_order_size_value_contracts(self):
        # Arrange
        order_size = ast.Call(func=ast.Name(id='Contracts', ctx=ast.Load()), args=[ast.Constant(value='invalid')],
                              keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_order_size, updated_changes = validate_order_size(order_size, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIn('order_size', updated_changes)
        self.assertEqual(updated_changes['order_size'],
                         "order_size argument should be a number. Defaulting to 'Contracts(1)'.")


    def test_invalid_order_size_value_usd(self):
        # Arragnge
        order_size = ast.Call(func=ast.Name(id='USD', ctx=ast.Load()), args=[ast.Constant(value='invalid')],
                              keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_order_size, updated_changes = validate_order_size(order_size, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIn('order_size', updated_changes)
        self.assertEqual(updated_changes['order_size'],
                         "order_size argument should be a number. Defaulting to 'Contracts(1)'.")


    def test_invalid_order_size_percent_of_equity(self):
        # Arrange
        order_size = ast.Call(func=ast.Name(id='PercentOfEquity', ctx=ast.Load()), args=[ast.Constant(value='invalid')],
                              keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_order_size, updated_changes = validate_order_size(order_size, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIn('order_size', updated_changes)
        self.assertEqual(updated_changes['order_size'],
                         "order_size argument should be a number. Defaulting to 'Contracts(1)'.")


if __name__ == '__main__':
    unittest.main()
