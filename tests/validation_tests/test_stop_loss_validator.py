import unittest
import ast
from trading_strategy_tester.validation.parameter_validations.stop_loss_validator import validate_stop_loss


class TestValidateStopLoss(unittest.TestCase):

    def test_valid_stop_loss(self):
        # Arrange: Valid stop_loss with percentage and stop_loss_type attributes
        stop_loss = ast.Call(
            func=ast.Name(id='StopLoss', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value=5)),
                ast.keyword(arg='stop_loss_type',
                            value=ast.Attribute(value=ast.Name(id='StopLossType', ctx=ast.Load()), attr='NORMAL',
                                                ctx=ast.Load()))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_stop_loss, updated_changes = validate_stop_loss(stop_loss, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_stop_loss)
        self.assertEqual(updated_changes, {})


    def test_invalid_stop_loss_type(self):
        # Arrange: Invalid stop_loss type (not 'StopLoss')
        stop_loss = ast.Call(
            func=ast.Name(id='InvalidStopLoss', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value=5)),
                ast.keyword(arg='stop_loss_type',
                            value=ast.Attribute(value=ast.Name(id='StopLossType', ctx=ast.Load()), attr='NORMAL',
                                                ctx=ast.Load()))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_stop_loss, updated_changes = validate_stop_loss(stop_loss, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_stop_loss, None)  # Default stop loss (None)
        self.assertIn('stop_loss', updated_changes)
        self.assertEqual(updated_changes['stop_loss'],
                         f"stop_loss argument should be of type StopLoss with percentage and stop_loss_type arguments. Defaulting to no stop loss.")


    def test_missing_percentage(self):
        # Arrange: Missing 'percentage' keyword
        stop_loss = ast.Call(
            func=ast.Name(id='StopLoss', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percent', value=ast.Constant(value=5)),
                ast.keyword(
                    arg='stop_loss_type',
                            value=ast.Attribute(value=ast.Name(id='StopLossType', ctx=ast.Load()), attr='NORMAL',
                                                ctx=ast.Load()))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_stop_loss, updated_changes = validate_stop_loss(stop_loss, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_stop_loss, None)  # Default stop loss (None)
        self.assertIn('stop_loss', updated_changes)
        self.assertEqual(updated_changes['stop_loss'],
                         f"stop_loss argument percentage is missing. Defaulting to no stop loss.")


    def test_missing_stop_loss_type(self):
        # Arrange: Missing 'stop_loss_type' keyword
        stop_loss = ast.Call(
            func=ast.Name(id='StopLoss', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value=5)),
                ast.keyword(
                    arg='stop_loss_type_missing',
                            value=ast.Attribute(value=ast.Name(id='StopLossType', ctx=ast.Load()),attr='NORMAL',
                                                ctx=ast.Load())
                )
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_stop_loss, updated_changes = validate_stop_loss(stop_loss, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_stop_loss, None)  # Default stop loss (None)
        self.assertIn('stop_loss', updated_changes)
        self.assertEqual(updated_changes['stop_loss'],
                         "stop_loss argument stop_loss_type is missing. Defaulting to no stop loss.")

    def test_invalid_stop_loss_type_enum(self):
        # Arrange: Invalid stop_loss_type enum (not 'StopLossType')
        stop_loss = ast.Call(
            func=ast.Name(id='StopLoss', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value=5)),
                ast.keyword(arg='stop_loss_type',
                            value=ast.Attribute(value=ast.Name(id='InvalidEnum', ctx=ast.Load()), attr='NORMAL',
                                                ctx=ast.Load()))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_stop_loss, updated_changes = validate_stop_loss(stop_loss, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_stop_loss, None)  # Default stop loss (None)
        self.assertIn('stop_loss', updated_changes)
        self.assertEqual(updated_changes['stop_loss'],
                            "stop_loss argument stop_loss_type should be of type StopLossType. Defaulting to no stop loss.")


    def test_invalid_stop_loss_type_value(self):
        # Arrange: Invalid stop_loss_type value (not 'NORMAL' or 'TRAILING')
        stop_loss = ast.Call(
            func=ast.Name(id='StopLoss', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='percentage', value=ast.Constant(value=5)),
                ast.keyword(arg='stop_loss_type',
                            value=ast.Attribute(value=ast.Name(id='StopLossType', ctx=ast.Load()), attr='INVALID',
                                                ctx=ast.Load()))
            ]
        )
        changes = {}
        logs = False

        # Act
        result, new_stop_loss, updated_changes = validate_stop_loss(stop_loss, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_stop_loss, None)  # Default stop loss (None)
        self.assertIn('stop_loss', updated_changes)
        self.assertEqual(updated_changes['stop_loss'],
                         "Valid stop_loss_types are: 'NORMAL', 'TRAILING'. Defaulting to no stop loss.")


    def test_invalid_percentage_type(self):
        # Arrange: Invalid percentage type (not a number)
        stop_loss = ast.Call(
            func=ast.Name(id='StopLoss', ctx=ast.Load()),
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
        result, new_stop_loss, updated_changes = validate_stop_loss(stop_loss, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_stop_loss, None)  # Default stop loss (None)
        self.assertIn('stop_loss', updated_changes)
        self.assertEqual(updated_changes['stop_loss'],
                         "stop_loss argument percentage should be a number. Defaulting to no stop loss.")


if __name__ == '__main__':
    unittest.main()
