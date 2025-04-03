import unittest
import ast
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.validation.parameter_validations.position_type_validator import validate_position_type


class TestValidatePositionType(unittest.TestCase):

    def test_valid_position_type(self):
        # Arrange
        position_type = ast.Attribute(value=ast.Name(id='PositionTypeEnum', ctx=ast.Load()), attr='LONG', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_position_type, updated_changes = validate_position_type(position_type, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertIsNone(new_position_type)
        self.assertEqual(updated_changes, {})


    def test_invalid_position_type_enum(self):
        # Arrange
        position_type = ast.Attribute(value=ast.Name(id='InvalidEnum', ctx=ast.Load()), attr='LONG', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_position_type, updated_changes = validate_position_type(position_type, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_position_type, PositionTypeEnum.LONG)
        self.assertIn('position_type', updated_changes)
        self.assertEqual(updated_changes['position_type'],
                         "position_type argument should be of type PositionTypeEnum. Using default position type 'PositionTypeEnum.LONG'.")


    def test_invalid_position_type_attr(self):
        # Arrange
        position_type = ast.Attribute(value=ast.Name(id='PositionTypeEnum', ctx=ast.Load()), attr='INVALID', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_position_type, updated_changes = validate_position_type(position_type, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_position_type, PositionTypeEnum.LONG)
        self.assertIn('position_type', updated_changes)
        self.assertEqual(updated_changes['position_type'],
                         "Valid PositionTypeEnums are: 'LONG', 'SHORT', 'LONG_SHORT_COMBINATION'. Using default position type 'PositionTypeEnum.LONG'.")


    def test_missing_position_type_value(self):
        # Arrange
        position_type = ast.Attribute(value=None, attr='LONG', ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_position_type, updated_changes = validate_position_type(position_type, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_position_type, PositionTypeEnum.LONG)
        self.assertIn('position_type', updated_changes)


    def test_missing_position_type_attr(self):
        # Arrange
        position_type = ast.Attribute(value=ast.Name(id='PositionTypeEnum', ctx=ast.Load()), attr=None, ctx=ast.Load())
        changes = {}
        logs = False

        # Act
        result, new_position_type, updated_changes = validate_position_type(position_type, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_position_type, PositionTypeEnum.LONG)
        self.assertIn('position_type', updated_changes)


    def test_invalid_type_for_position_type(self):
        # Arrange
        position_type = 'LONG'
        changes = {}
        logs = False

        # Act
        result, new_position_type, updated_changes = validate_position_type(position_type, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_position_type, PositionTypeEnum.LONG)
        self.assertIn('position_type', updated_changes)

if __name__ == '__main__':
    unittest.main()
