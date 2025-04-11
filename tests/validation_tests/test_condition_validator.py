import unittest
import ast

from trading_strategy_tester.validation.parameter_validations.condition_validator import validate_condition, \
    validate_trading_series


class TestValidateCondition(unittest.TestCase):

    def test_valid_downtrend_fib_retracement_level_condition1(self):
        # Arrange: Valid condition (DowntrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_50',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=14))
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


    def test_valid_downtrend_fib_retracement_level_condition2(self):
        # Arrange: Valid condition (DowntrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_23_6',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=21))
            ]
        )
        changes = {}
        logs = False
        buy = False

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)


    def test_valid_downtrend_fib_retracement_level_condition3(self):
        # Arrange: Valid condition (DowntrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_100',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=14)),
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


    def test_invalid_param_name_downtrend_fib_retracement_level_condition(self):
        # Arrange: Invalid condition (DowntrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fiblevel',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_0',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=14))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: fib_level."})


    def test_invalid_enum_value_downtrend_fib_retracement_level_condition(self):
        # Arrange: Invalid condition (DowntrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_999',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=14)),
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.maxDiff = None
        self.assertTrue(result)
        default_fib_level = ast.Attribute(
            value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
            attr='LEVEL_38_2',
            ctx=ast.Load()
        )
        self.assertEqual(new_condition.keywords[0].value.value.id, default_fib_level.value.id)
        self.assertEqual(new_condition.keywords[0].value.attr, default_fib_level.attr)
        self.assertEqual(updated_changes, {f'{changes_key}_{condition_id}_fib_level': f"Invalid Fibonacci levels in parameter fib_level of {condition_id}. Using defined default level 38.2%. Valid Fibonacci levels are: LEVEL_0, LEVEL_23_6, LEVEL_38_2, LEVEL_50, LEVEL_61_8, LEVEL_100."})


    def test_invalid_length_downtrend_fib_retracement_level_condition(self):
        # Arrange: Invalid condition (DowntrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_61_8',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=4.8)),
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {f'{changes_key}_{condition_id}_length': f"Invalid integer value in parameter length of {condition_id}."})


    def test_valid_uptrend_fib_retracement_level_condition1(self):
        # Arrange: Valid condition (UptrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'UptrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_0',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=14))
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


    def test_valid_uptrend_fib_retracement_level_condition2(self):
        # Arrange: Valid condition (UptrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'UptrendFibRetracementLevelCondition'
        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_23_6',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=21))
            ]
        )
        changes = {}
        logs = False
        buy = False

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)


    def test_valid_uptrend_fib_retracement_level_condition3(self):
        # Arrange: Valid condition (UptrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'UptrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                attr='LEVEL_38_2',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=14)),
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


    def test_invalid_enum_fib_level_uptrend_fib_retracement_level_condition(self):
        # Arrange: Invalid condition (UptrendFibRetracementLevelCondition)
        ticker = 'AAPL'
        condition_id = 'UptrendFibRetracementLevelCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='fib_level',
                            value=ast.Attribute(
                                value=ast.Name(id='FibonacciLevelsEnum', ctx=ast.Load()),
                                attr='LEVEL_50',
                                ctx=ast.Load()
                                ),
                            ),
                ast.keyword(arg='length',
                            value=ast.Constant(value=14)),
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.maxDiff = None
        self.assertTrue(result)
        default_fib_level = ast.Attribute(
            value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
            attr='LEVEL_38_2',
            ctx=ast.Load()
        )
        self.assertEqual(new_condition.keywords[0].value.value.id, default_fib_level.value.id)
        self.assertEqual(new_condition.keywords[0].value.attr, default_fib_level.attr)
        self.assertEqual(updated_changes, {f'{changes_key}_{condition_id}_fib_level': f"fibonacci_levels should be of type FibonacciLevels in parameter fib_level of {condition_id}. Using defined default level 38.2%."})


    def test_valid_and_condition1(self):
        # Arrange: Valid condition (AND)
        ticker = 'AAPL'
        condition_id = 'AND'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[
                ast.Call(func=ast.Name(id='CrossOverCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='first_series',
                                         value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()),
                                                        args=[ast.Constant(value=ticker)],
                                                        keywords=[])),
                             ast.keyword(arg='second_series',
                                         value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()),
                                                        args=[ast.Constant(value=70)],
                                                        keywords=[]))
                         ]),
                ast.Call(func=ast.Name(id='DowntrendFibRetracementLevelCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='fib_level',
                                         value=ast.Attribute(
                                             value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                             attr='LEVEL_50',
                                             ctx=ast.Load()
                                         )),
                             ast.keyword(arg='length',
                                         value=ast.Constant(value=14))
                         ])
            ],
            keywords=[]
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


    def test_valid_and_condition2(self):
        # Arrange: Valid condition (AND)
        ticker = 'AAPL'
        condition_id = 'AND'
        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[
                ast.Call(func=ast.Name(id='IntraIntervalChangeOfXPercentCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='series',
                                         value=ast.Call(func=ast.Name(id='CCI', ctx=ast.Load()),
                                                        args=[ast.Constant(value=ticker)],
                                                        keywords=[])),
                             ast.keyword(arg='percent',
                                         value=ast.Constant(value=5.5)),
                         ]),
                ast.Call(func=ast.Name(id='UptrendFibRetracementLevelCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='fib_level',
                                         value=ast.Attribute(
                                             value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                             attr='LEVEL_50',
                                             ctx=ast.Load()
                                         )),
                             ast.keyword(arg='length',
                                         value=ast.Constant(value=14))
                         ])
            ],
            keywords=[]
        )
        changes = {}
        logs = False
        buy = False

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)


    def test_invalid_param_and_condition(self):
        # Arrange: Invalid condition (AND)
        ticker = 'AAPL'
        condition_id = 'AND'

        first_trading_series = ast.Call(func=ast.Name(id='CrossOverCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='first_series',
                                         value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()),
                                                        args=[ast.Constant(value=ticker)],
                                                        keywords=[])),
                             ast.keyword(arg='second_series',
                                         value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()),
                                                        args=[ast.Constant(value=70)],
                                                        keywords=[]))
                         ])

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[
                first_trading_series,
                ast.Call(func=ast.Name(id='NotValidCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='fib_level',
                                         value=ast.Attribute(
                                             value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                             attr='LEVEL_50',
                                             ctx=ast.Load()
                                         )),
                             ast.keyword(arg='length',
                                         value=ast.Constant(value='14'))
                         ])
            ],
            keywords=[]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(first_trading_series.func.id, new_condition.args[0].func.id)
        self.assertEqual(len(new_condition.args), 1)
        self.assertEqual(updated_changes, {changes_key: f"Condition 'NotValidCondition' does not exist."})


    def test_valid_or_condition1(self):
        # Arrange: Valid condition (OR)
        ticker = 'AAPL'
        condition_id = 'OR'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[
                ast.Call(func=ast.Name(id='CrossOverCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='first_series',
                                         value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()),
                                                        args=[ast.Constant(value=ticker)],
                                                        keywords=[])),
                             ast.keyword(arg='second_series',
                                         value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()),
                                                        args=[ast.Constant(value=70)],
                                                        keywords=[]))
                         ]),
                ast.Call(func=ast.Name(id='DowntrendFibRetracementLevelCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='fib_level',
                                         value=ast.Attribute(
                                             value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                             attr='LEVEL_50',
                                             ctx=ast.Load()
                                         )),
                             ast.keyword(arg='length',
                                         value=ast.Constant(value=14))
                         ])
            ],
            keywords=[]
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


    def test_valid_or_condition2(self):
        # Arrange: Valid condition (OR)
        ticker = 'AAPL'
        condition_id = 'OR'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[
                ast.Call(func=ast.Name(id='IntraIntervalChangeOfXPercentCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='series',
                                         value=ast.Call(func=ast.Name(id='CCI', ctx=ast.Load()),
                                                        args=[ast.Constant(value=ticker)],
                                                        keywords=[])),
                             ast.keyword(arg='percent',
                                         value=ast.Constant(value=5.5)),
                         ]),
                ast.Call(func=ast.Name(id='UptrendFibRetracementLevelCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='fib_level',
                                         value=ast.Attribute(
                                             value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                             attr='LEVEL_50',
                                             ctx=ast.Load()
                                         )),
                             ast.keyword(arg='length',
                                         value=ast.Constant(value=14))
                         ])
            ],
            keywords=[]
        )
        changes = {}
        logs = False
        buy = False

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)


    def test_invalid_param_or_condition(self):
        # Arrange: Invalid condition (OR)
        ticker = 'AAPL'
        condition_id = 'OR'

        first_trading_series = ast.Call(func=ast.Name(id='CrossOverCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='first_series',
                                         value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()),
                                                        args=[ast.Constant(value=ticker)],
                                                        keywords=[])),
                             ast.keyword(arg='second_series',
                                         value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()),
                                                        args=[ast.Constant(value=70)],
                                                        keywords=[]))
                         ])

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[
                first_trading_series,
                ast.Call(func=ast.Name(id='NotValidCondition', ctx=ast.Load()), args=[],
                         keywords=[
                             ast.keyword(arg='fib_level',
                                         value=ast.Attribute(
                                             value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                             attr='LEVEL_50',
                                             ctx=ast.Load()
                                         )),
                             ast.keyword(arg='length',
                                         value=ast.Constant(value='14'))
                         ])
            ],
            keywords=[]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(first_trading_series.func.id, new_condition.args[0].func.id)
        self.assertEqual(len(new_condition.args), 1)
        self.assertEqual(updated_changes, {changes_key: f"Condition 'NotValidCondition' does not exist."})


    def test_valid_after_x_days_condition1(self):
        # Arrange: Valid condition (AfterXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'AfterXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='condition',
                            value=ast.Call(func=ast.Name(id='CrossOverCondition', ctx=ast.Load()), args=[],
                                           keywords=[
                                               ast.keyword(arg='first_series',
                                                           value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()),
                                                                          args=[ast.Constant(value=ticker)],
                                                                          keywords=[])),
                                               ast.keyword(arg='second_series',
                                                           value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()),
                                                                          args=[ast.Constant(value=70)],
                                                                          keywords=[]))
                                           ])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
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


    def test_valid_after_x_days_condition2(self):
        # Arrange: Valid condition (AfterXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'AfterXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='condition',
                            value=ast.Call(func=ast.Name(id='IntraIntervalChangeOfXPercentCondition', ctx=ast.Load()), args=[],
                             keywords=[
                                 ast.keyword(arg='series',
                                             value=ast.Call(func=ast.Name(id='CCI', ctx=ast.Load()),
                                                            args=[ast.Constant(value=ticker)],
                                                            keywords=[])),
                                 ast.keyword(arg='percent',
                                             value=ast.Constant(value=5.5)),
                             ])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=0))
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


    def test_valid_after_x_days_condition3(self):
        # Arrange: Valid condition (AfterXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'AfterXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='condition',
                            value=ast.Call(func=ast.Name(id='UptrendFibRetracementLevelCondition', ctx=ast.Load()), args=[],
                             keywords=[
                                 ast.keyword(arg='fib_level',
                                             value=ast.Attribute(
                                                 value=ast.Name(id='FibonacciLevels', ctx=ast.Load()),
                                                 attr='LEVEL_50',
                                                 ctx=ast.Load()
                                             )),
                                 ast.keyword(arg='length',
                                             value=ast.Constant(value=14))
                             ])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=66))
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


    def test_invalid_condition_after_x_days_condition(self):
        # Arrange: Invalid condition (AfterXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'AfterXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='condition',
                            value=ast.Call(func=ast.Name(id='NotValidCondition', ctx=ast.Load()), args=[],
                                           keywords=[])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition 'NotValidCondition' does not exist."})

    def test_invalid_number_of_days_after_x_days_condition2(self):
        # Arrange: Invalid condition (AfterXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'AfterXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='condition',
                            value=ast.Call(func=ast.Name(id='CrossOverCondition', ctx=ast.Load()), args=[],
                                           keywords=[
                                               ast.keyword(arg='first_series',
                                                           value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()),
                                                                          args=[ast.Constant(value=ticker)],
                                                                          keywords=[])),
                                               ast.keyword(arg='second_series',
                                                           value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()),
                                                                          args=[ast.Constant(value=70)],
                                                                          keywords=[]))
                                           ])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=-1.4))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {f'{changes_key}_{condition_id}_number_of_days': f"Invalid integer value in parameter number_of_days of {condition_id}."})


    def test_valid_change_of_x_percent_per_y_days_condition1(self):
        # Arrange: Valid condition (ChangeOfXPercentPerYDaysCondition)
        ticker = 'AAPL'
        condition_id = 'ChangeOfXPercentPerYDaysCondition'
        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='CLOSE', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='percent',
                            value=ast.Constant(value=5.5)),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
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


    def test_valid_change_of_x_percent_per_y_days_condition2(self):
        # Arrange: Valid condition (ChangeOfXPercentPerYDaysCondition)
        ticker = 'AAPL'
        condition_id = 'ChangeOfXPercentPerYDaysCondition'
        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='ATR', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='percent',
                            value=ast.Constant(value=2)),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=0))
            ]
        )
        changes = {}
        logs = False
        buy = False

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)

    def test_invalid_series_change_of_x_percent_per_y_days_condition(self):
        # Arrange: Invalid condition (ChangeOfXPercentPerYDaysCondition)
        ticker = 'AAPL'
        condition_id = 'ChangeOfXPercentPerYDaysCondition'
        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='NotValidCondition', ctx=ast.Load()), args=[],
                                           keywords=[])),
                ast.keyword(arg='percent',
                            value=ast.Constant(value=5.5)),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {f'{changes_key}_{condition_id}_series': f"Trading series 'NotValidCondition' does not exist."})

    def test_valid_intra_interval_change_of_x_percent_condition(self):
        # Arrange: Valid condition (IntraIntervalChangeOfXPercentCondition)
        ticker = 'AAPL'
        condition_id = 'IntraIntervalChangeOfXPercentCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='CLOSE', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='percent',
                            value=ast.Constant(value=5.5))
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


    def test_invalid_intra_interval_change_of_x_percent_condition(self):
        # Arrange: Invalid condition (IntraIntervalChangeOfXPercentCondition)
        ticker = 'AAPL'
        condition_id = 'IntraIntervalChangeOfXPercentCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='NotValidCondition', ctx=ast.Load()), args=[],
                                           keywords=[])),
                ast.keyword(arg='percent',
                            value=ast.Constant(value=5.5))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {f'{changes_key}_{condition_id}_series': f"Trading series 'NotValidCondition' does not exist."})


    def test_invalid_intra_interval_change_of_x_percent_condition2(self):
        # Arrange: Invalid condition (IntraIntervalChangeOfXPercentCondition)
        ticker = 'AAPL'
        condition_id = 'IntraIntervalChangeOfXPercentCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='CLOSE', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='percent',
                            value=ast.Constant(value='non_integer_value'))
            ]
        )
        changes = {}
        logs = False
        buy = True

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {f'buy_condition_{condition_id}_percent': f"Invalid float value in parameter percent of {condition_id}. Using defined default value."})


    def test_invalid_intra_interval_change_of_x_percent_condition3(self):
        # Arrange: Invalid condition (IntraIntervalChangeOfXPercentCondition)
        ticker = 'AAPL'
        condition_id = 'IntraIntervalChangeOfXPercentCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='CLOSE', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
            ]
        )
        changes = {}
        logs = False
        buy = True

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {f'buy_condition': f"Condition '{condition_id}' is missing the following parameters: percent."})



    def test_valid_cross_over_condition1(self):
        # Arrange: Valid condition (CrossOverCondition)
        ticker = 'AAPL'
        condition_id = 'CrossOverCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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
        condition_id = 'CrossOverCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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
        condition_id = 'CrossOverCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_valid_cross_over_condition_extra_param(self):
        # Arrange: Valid condition (CrossOverCondition)
        ticker = 'AAPL'
        condition_id = 'CrossOverCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='extra_param',
                            value=ast.Constant(value='extra_value')),
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


    def test_invalid_param_name_cross_over_condition(self):
        # Arrange: Invalid condition (CrossOverCondition)
        ticker = 'AAPL'
        condition_id = 'CrossOverCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series1',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='series2',
                            value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()), args=[ast.Constant(value=70)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: first_series, second_series."})


    def test_invalid_missing_param_cross_over_condition(self):
        # Arrange: Invalid condition (CrossOverCondition)
        ticker = 'AAPL'
        condition_id = 'CrossOverCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='first_series',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: second_series."})


    def test_valid_cross_under_condition1(self):
        # Arrange: Valid condition (CrossUnderCondition)
        ticker = 'AAPL'
        condition_id = 'CrossUnderCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_valid_cross_under_condition2(self):
        # Arrange: Valid condition (CrossUnderCondition)
        ticker = 'AAPL'
        condition_id = 'CrossUnderCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_valid_cross_under_condition3(self):
        # Arrange: Valid condition (CrossUnderCondition)
        ticker = 'AAPL'
        condition_id = 'CrossUnderCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_invalid_param_name_cross_under_condition(self):
        # Arrange: Invalid condition (CrossUnderCondition)
        ticker = 'AAPL'
        condition_id = 'CrossUnderCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series1',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='series2',
                            value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()), args=[ast.Constant(value=70)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: first_series, second_series."})


    def test_invalid_missing_param_cross_under_condition(self):
        # Arrange: Invalid condition (CrossUnderCondition)
        ticker = 'AAPL'
        condition_id = 'CrossUnderCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='first_series',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: second_series."})


    def test_valid_greater_than_condition1(self):
        # Arrange: Valid condition (GreaterThanCondition)
        ticker = 'AAPL'
        condition_id = 'GreaterThanCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_valid_greater_than_condition2(self):
        # Arrange: Valid condition (GreaterThanCondition)
        ticker = 'AAPL'
        condition_id = 'GreaterThanCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_valid_less_than_condition1(self):
        # Arrange: Valid condition (LessThanCondition)
        ticker = 'AAPL'
        condition_id = 'LessThanCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_valid_less_than_condition2(self):
        # Arrange: Valid condition (LessThanCondition)
        ticker = 'AAPL'
        condition_id = 'LessThanCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
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


    def test_invalid_param_name_greater_than_condition(self):
        # Arrange: Invalid condition (GreaterThanCondition)
        ticker = 'AAPL'
        condition_id = 'GreaterThanCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series1',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='series2',
                            value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()), args=[ast.Constant(value=70)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: first_series, second_series."})


    def test_invalid_param_name_less_than_condition(self):
        # Arrange: Invalid condition (LessThanCondition)
        ticker = 'AAPL'
        condition_id = 'LessThanCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series1',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='series2',
                            value=ast.Call(func=ast.Name(id='CONST', ctx=ast.Load()), args=[ast.Constant(value=70)],
                                           keywords=[]))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: first_series, second_series."})


    def test_valid_downtrend_for_x_days_condition1(self):
        # Arrange: Valid condition (DowntrendForXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendForXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
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

    def test_valid_downtrend_for_x_days_condition2(self):
        # Arrange: Valid condition (DowntrendForXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendForXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='ATR', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=0))
            ]
        )
        changes = {}
        logs = False
        buy = False

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)

    def test_invalid_param_name_downtrend_for_x_days_condition(self):
        # Arrange: Invalid condition (DowntrendForXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'DowntrendForXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series1',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: series."})


    def test_valid_uptrend_for_x_days_condition1(self):
        # Arrange: Valid condition (UptrendForXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'UptrendForXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
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


    def test_valid_uptrend_for_x_days_condition2(self):
        # Arrange: Valid condition (UptrendForXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'UptrendForXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series',
                            value=ast.Call(func=ast.Name(id='ATR', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=0))
            ]
        )
        changes = {}
        logs = False
        buy = False

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})
        self.assertIsNotNone(new_condition)


    def test_invalid_param_name_uptrend_for_x_days_condition(self):
        # Arrange: Invalid condition (UptrendForXDaysCondition)
        ticker = 'AAPL'
        condition_id = 'UptrendForXDaysCondition'

        condition = ast.Call(
            func=ast.Name(id=condition_id, ctx=ast.Load()),
            args=[],
            keywords=[
                ast.keyword(arg='series1',
                            value=ast.Call(func=ast.Name(id='RSI', ctx=ast.Load()), args=[ast.Constant(value=ticker)],
                                           keywords=[])),
                ast.keyword(arg='number_of_days',
                            value=ast.Constant(value=14))
            ]
        )
        changes = {}
        logs = False
        buy = True
        changes_key = 'buy_condition' if buy else 'sell_condition'

        # Act
        result, new_condition, updated_changes = validate_condition(condition, changes, logs, buy)

        # Assert
        self.assertFalse(result)
        self.assertIsNone(new_condition)
        self.assertEqual(updated_changes, {changes_key: f"Condition '{condition_id}' is missing the following parameters: series."})


    def test_trading_series_with_smoothing_type(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        # Create the trading series of ATR
        trading_series = ast.Call(
            func=ast.Name(id='ATR', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='smoothing', value=ast.Attribute(
                    value=ast.Name(id='SmoothingType', ctx=ast.Load()),
                    attr='SMA',
                    ctx=ast.Load()
                ))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'param_name'
        parent_name = 'parent_name'

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy, param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})

    def test_trading_series_with_smoothing_type_invalid_type(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        # Create the trading series of ATR
        trading_series = ast.Call(
            func=ast.Name(id='ATR', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='smoothing', value=ast.Attribute(
                    value=ast.Name(id='InvalidType', ctx=ast.Load()),
                    attr='SMA',
                    ctx=ast.Load()
                ))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'smoothing'
        parent_name = 'ATR'

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy,
                                                                              param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {f'buy_condition_{parent_name}_{param_name}': f"smoothing_type should be of type SmoothingType in parameter {param_name} of {parent_name}. Using defined default value."})


    def test_trading_series_with_smoothing_type_invalid_smoothing(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        # Create the trading series of ATR
        trading_series = ast.Call(
            func=ast.Name(id='ATR', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='smoothing', value=ast.Attribute(
                    value=ast.Name(id='SmoothingType', ctx=ast.Load()),
                    attr='InvalidSmoothing',
                    ctx=ast.Load()
                ))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'smoothing'
        parent_name = 'ATR'
        valid_smoothing_types = ['RMA', 'SMA', 'EMA', 'WMA']

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy,
                                                                              param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {f'buy_condition_{parent_name}_{param_name}': f"Invalid smoothing type in parameter {param_name} of {parent_name}. Using defined default value. Valid smoothing types are: {', '.join(valid_smoothing_types)}."})


    def test_trading_series_with_source_type(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        # Create the trading series of RSI
        trading_series = ast.Call(
            func=ast.Name(id='RSI', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='source', value=ast.Attribute(
                    value=ast.Name(id='SourceType', ctx=ast.Load()),
                    attr='CLOSE',
                    ctx=ast.Load()
                ))
            ]
        )

        changes = {}
        logs = False
        buy = True
        param_name = 'source'
        parent_name = 'RSI'

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy, param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})


    def test_trading_series_with_source_type_invalid_type(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        # Create the trading series of RSI
        trading_series = ast.Call(
            func=ast.Name(id='RSI', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='source', value=ast.Attribute(
                    value=ast.Name(id='InvalidType', ctx=ast.Load()),
                    attr='CLOSE',
                    ctx=ast.Load()
                ))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'source'
        parent_name = 'RSI'

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy, param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {f'buy_condition_{parent_name}_{param_name}': f"source should be of type SourceType in parameter {param_name} of {parent_name}. Using defined default value."})


    def test_trading_series_with_source_type_invalid_source(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        # Create the trading series of RSI
        trading_series = ast.Call(
            func=ast.Name(id='RSI', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='source', value=ast.Attribute(
                    value=ast.Name(id='SourceType', ctx=ast.Load()),
                    attr='InvalidSource',
                    ctx=ast.Load()
                ))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'source'
        parent_name = 'RSI'
        valid_source_types = ['CLOSE', 'OPEN', 'HIGH', 'LOW', 'HLC3', 'HL2', 'OHLC4', 'HLCC4', 'VOLUME']

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy, param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {f'buy_condition_{parent_name}_{param_name}': f"Invalid source type in parameter {param_name} of {parent_name}. Using defined default value. Valid source types are: {', '.join(valid_source_types)}."})

    def test_trading_series_with_float(self):
        # Arrange
        ticker = 'AAPL'
        length = 14
        std_dev = 2

        trading_series = ast.Call(
            func=ast.Name(id='BB_LOWER', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='std_dev', value=ast.Constant(value=std_dev))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'param_name'
        parent_name = 'parent_name'

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy, param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})


    def test_trading_series_with_bool(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        trading_series = ast.Call(
            func=ast.Name(id='KC_UPPER', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='use_exp_ma', value=ast.Constant(value=True))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'use_exp_ma'
        parent_name = 'KC_UPPER'

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy, param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {})


    def test_trading_series_with_bool_invalid_type(self):
        # Arrange
        ticker = 'AAPL'
        length = 14

        trading_series = ast.Call(
            func=ast.Name(id='KC_UPPER', ctx=ast.Load()),
            args=[ast.Constant(value=ticker)],
            keywords=[
                ast.keyword(arg='length', value=ast.Constant(value=length)),
                ast.keyword(arg='use_exp_ma', value=ast.Attribute(
                    value=ast.Name(id='InvalidType', ctx=ast.Load()),
                    attr='CLOSE',
                    ctx=ast.Load()
                ))
            ]
        )
        changes = {}
        logs = False
        buy = True
        param_name = 'use_exp_ma'
        parent_name = 'KC_UPPER'

        # Act
        result, new_trading_series, updated_changes = validate_trading_series(trading_series, changes, logs, buy, param_name, parent_name)

        # Assert
        self.assertTrue(result)
        self.assertEqual(updated_changes, {f'buy_condition_{parent_name}_{param_name}': f"Invalid boolean value in parameter {param_name} of {parent_name}. Using defined default value."})

if __name__ == '__main__':
    unittest.main()
