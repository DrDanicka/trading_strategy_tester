import unittest
import ast
from trading_strategy_tester.validation.parameter_validations.trade_commissions_validator import \
    validate_trade_commissions


class TestValidateTradeCommissions(unittest.TestCase):

    def test_valid_money_commissions(self):
        # Arrange
        trade_commissions = ast.Call(func=ast.Name(id='MoneyCommissions', ctx=ast.Load()), args=[ast.Constant(value=5)],
                                     keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_trade_commissions, updated_changes = validate_trade_commissions(trade_commissions, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_trade_commissions)
        self.assertEqual(updated_changes, {})

    def test_valid_percentage_commissions(self):
        # Arrange
        trade_commissions = ast.Call(func=ast.Name(id='PercentageCommissions', ctx=ast.Load()),
                                     args=[ast.Constant(value=0.5)], keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_trade_commissions, updated_changes = validate_trade_commissions(trade_commissions, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_trade_commissions)
        self.assertEqual(updated_changes, {})

    def test_invalid_commissions_type(self):
        # Arrange
        trade_commissions = ast.Call(func=ast.Name(id='InvalidCommissions', ctx=ast.Load()),
                                     args=[ast.Constant(value=5)], keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_trade_commissions, updated_changes = validate_trade_commissions(trade_commissions, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_trade_commissions)
        self.assertIn('trade_commissions', updated_changes)
        self.assertEqual(updated_changes['trade_commissions'],
                         "Invalid trade_commissions type. Available commissions are: MoneyCommissions, PercentageCommissions. Defaulting to no commissions.")

    def test_invalid_commissions_value_money(self):
        # Arrange
        trade_commissions = ast.Call(func=ast.Name(id='MoneyCommissions', ctx=ast.Load()),
                                     args=[ast.Constant(value='invalid')], keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_trade_commissions, updated_changes = validate_trade_commissions(trade_commissions, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_trade_commissions)
        self.assertIn('trade_commissions', updated_changes)
        self.assertEqual(updated_changes['trade_commissions'],
                         "trade_commissions argument percentage should be a number. Defaulting to no commissions.")


    def test_invalid_commissions_value_percentage(self):
        # Arrange
        trade_commissions = ast.Call(func=ast.Name(id='PercentageCommissions', ctx=ast.Load()),
                                     args=[ast.Constant(value='invalid')], keywords=[])
        changes = {}
        logs = False

        # Act
        result, new_trade_commissions, updated_changes = validate_trade_commissions(trade_commissions, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_trade_commissions)
        self.assertIn('trade_commissions', updated_changes)
        self.assertEqual(updated_changes['trade_commissions'],
                         "trade_commissions argument percentage should be a number. Defaulting to no commissions.")


    def test_invalid_type_for_trade_commissions(self):
        # Arrange
        trade_commissions = 'MoneyCommissions(5)'  # Not an ast.Call object
        changes = {}
        logs = False

        # Act
        result, new_trade_commissions, updated_changes = validate_trade_commissions(trade_commissions, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_trade_commissions)
        self.assertIn('trade_commissions', updated_changes)


if __name__ == '__main__':
    unittest.main()
