import unittest
import ast
from trading_strategy_tester.validation.parameter_validations.take_profit_validator import validate_take_profit


class TestValidateTakeProfit(unittest.TestCase):

    def test_valid_take_profit(self):
        # Arrange: Valid take_profit with percentage and stop_loss_type attributes
        take_profit = ast.Call(
            func=ast.Name(id='TakeProfit', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value=5))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_take_profit, updated_changes = validate_take_profit(take_profit, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_take_profit)
        self.assertEqual(updated_changes, {})

    def test_invalid_take_profit_type(self):
        # Arrange: Invalid take_profit type (not 'TakeProfit')
        take_profit = ast.Call(
            func=ast.Name(id='InvalidTakeProfit', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value=5))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_take_profit, updated_changes = validate_take_profit(take_profit, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_take_profit, None)  # Default take profit (None)
        self.assertIn('take_profit', updated_changes)
        self.assertEqual(updated_changes['take_profit'],
                         "take_profit argument should be of type TakeProfit. Defaulting to no take profit.")

    def test_invalid_percentage_type(self):
        # Arrange: Invalid percentage type (not a number)
        take_profit = ast.Call(
            func=ast.Name(id='TakeProfit', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value='invalid')),
                ast.keyword(arg='stop_loss_type',
                            value=ast.Attribute(value=ast.Name(id='StopLossType', ctx=ast.Load()), attr='NORMAL',
                                                ctx=ast.Load()))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_take_profit, updated_changes = validate_take_profit(take_profit, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_take_profit, None)  # Default take profit (None)
        self.assertIn('take_profit', updated_changes)
        self.assertEqual(updated_changes['take_profit'],
                         "take_profit argument percentage should be a number. Defaulting to no take profit.")

    def test_missing_percentage(self):
        # Arrange: Missing 'stop_loss_type' keyword
        take_profit = ast.Call(
            func=ast.Name(id='TakeProfit', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percent', value=ast.Constant(value=5))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_take_profit, updated_changes = validate_take_profit(take_profit, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_take_profit, None)  # Default take profit (None)
        self.assertIn('take_profit', updated_changes)
        self.assertEqual(updated_changes['take_profit'],
                         "take_profit argument percentage is missing. Defaulting to no take profit.")


if __name__ == '__main__':
    unittest.main()
