import unittest
import ast
from trading_strategy_tester.validation.parameter_validations.condition_validator import validate_condition


class TestValidateCondition(unittest.TestCase):

    def test_valid_cross_over_condition1(self):
        # Arrange: Valid condition (CrossOverCondition)
        ticker = 'AAPL'
        condition = ast.Call(
            func=ast.Name(id='CrossOverCondition', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='first_series',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='second_series',
                            value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()), args=[ast.Constant(value=70)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)

    def test_valid_cross_over_condition2(self):
        # Arrange: Valid condition (CrossOverCondition)
        ticker = 'AAPL'
        condition = ast.Call(
            func=ast.Name(id='CrossOverCondition', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='first_series',
                            value=ast.Call(func=ast.Name(id='ATR', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='second_series',
                            value=ast.Call(func=ast.Name(id='CLOSE', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)


    def test_valid_cross_over_condition3(self):
        # Arrange: Valid condition (CrossOverCondition)
        ticker = 'AAPL'
        condition = ast.Call(
            func=ast.Name(id='CrossOverCondition', ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='first_series',
                            value=ast.Call(func=ast.Name(id='SMA', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[
                                                ast.keyword(arg='offset', value=ast.Constant(value=0)),
                                                ast.keyword(arg='length', value=ast.Constant(value=14)),
                                                ast.keyword(arg='source', value=ast.Attribute(
                                                    value=ast.Name(id='SourceType', ctx=ast.Load()),
                                                    attr='CLOSE',
                                                    ctx=ast.Load()
                                                ))
                                           ])),
                ast.keyword(arg='second_series',
                            value=ast.Call(func=ast.Name(id='TRIX', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[
                                               ast.keyword(arg='length', value=ast.Constant(value=9)),
                                           ]))
            ]
        )

        changes = {}
        logs = False
        buy = True

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)


if __name__ == '__main__':
    unittest.main()
