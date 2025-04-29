import unittest
import random

from trading_strategy_tester.training_data.condition_generator import (
    process_one_trading_series,
    create_condition,
    build_logical_expression,
    get_random_condition
)


class TestConditionGenerator(unittest.TestCase):

    def setUp(self):
        """Create a seeded random generator for reproducibility."""
        self.rng = random.Random(42)

    def test_process_one_trading_series(self):
        # Arrange
        ticker = "AAPL"

        # Act
        text, param = process_one_trading_series(self.rng, ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertIn(ticker, param)  # The ticker should be inside param if not CONST

    def test_create_condition(self):
        # Arrange
        ticker = "AAPL"

        # Act
        text, param = create_condition(self.rng, ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(len(text) > 0)
        self.assertTrue(len(param) > 0)

    def test_build_logical_expression_with_and(self):
        # Arrange
        ops = ["and", "and"]
        words = ["condition1", "condition2", "condition3"]
        params = ["param1", "param2", "param3"]

        # Act
        text, param = build_logical_expression(ops, words, params)

        # Assert
        self.assertEqual(text, "condition1 and condition2 and condition3")
        self.assertEqual(param, "AND(param1, param2, param3)")

    def test_build_logical_expression_with_or(self):
        # Arrange
        ops = ["or", "and"]
        words = ["cond1", "cond2", "cond3"]
        params = ["p1", "p2", "p3"]

        # Act
        text, param = build_logical_expression(ops, words, params)

        # Assert
        self.assertEqual(text, "cond1 or cond2 and cond3")
        self.assertTrue(param.startswith("OR("))

    def test_get_random_condition(self):
        # Arrange
        ticker = "MSFT"

        # Act
        text, param = get_random_condition(self.rng, up_to_n=2, ticker=ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(len(text) > 0)
        self.assertTrue(len(param) > 0)

    def test_process_one_trading_series_basic(self):
        # Arrange
        ticker = "AAPL"

        # Act
        text, param = process_one_trading_series(self.rng, ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)

    def test_process_one_trading_series_includes_ticker_in_param(self):
        # Arrange
        ticker = "GOOG"

        # Act
        text, param = process_one_trading_series(self.rng, ticker)

        # Assert
        self.assertTrue(ticker in param or 'CONST' in param)

    def test_process_one_trading_series_multiple_calls_different_output(self):
        # Arrange
        ticker = "TSLA"

        # Act
        outputs = {process_one_trading_series(self.rng, ticker) for _ in range(5)}

        # Assert
        self.assertGreater(len(outputs), 1)

    # --- Tests for create_condition ---

    def test_create_condition_basic(self):
        # Arrange
        ticker = "AAPL"

        # Act
        text, param = create_condition(self.rng, ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)

    def test_create_condition_multiple_calls_unique_texts(self):
        # Arrange
        ticker = "META"

        # Act
        outputs = {create_condition(self.rng, ticker)[0] for _ in range(5)}

        # Assert
        self.assertGreater(len(outputs), 1)

    # --- Tests for build_logical_expression ---

    def test_build_logical_expression_all_and(self):
        # Arrange
        ops = ["and", "and"]
        words = ["cond1", "cond2", "cond3"]
        params = ["p1", "p2", "p3"]

        # Act
        text, param = build_logical_expression(ops, words, params)

        # Assert
        self.assertEqual(text, "cond1 and cond2 and cond3")
        self.assertTrue(param.startswith("AND("))

    def test_build_logical_expression_all_or(self):
        # Arrange
        ops = ["or", "or"]
        words = ["cond1", "cond2", "cond3"]
        params = ["p1", "p2", "p3"]

        # Act
        text, param = build_logical_expression(ops, words, params)

        # Assert
        self.assertEqual(text, "cond1 or cond2 or cond3")
        self.assertTrue(param.startswith("OR("))

    def test_build_logical_expression_mixed_and_or(self):
        # Arrange
        ops = ["and", "or"]
        words = ["a", "b", "c"]
        params = ["p1", "p2", "p3"]

        # Act
        text, param = build_logical_expression(ops, words, params)

        # Assert
        self.assertIn("or", text)
        self.assertIn("and", text)

    def test_build_logical_expression_single_element(self):
        # Arrange
        ops = []
        words = ["one"]
        params = ["p1"]

        # Act
        text, param = build_logical_expression(ops, words, params)

        # Assert
        self.assertEqual(text, "one")
        self.assertEqual(param, "p1")

    # --- Tests for get_random_condition ---

    def test_get_random_condition_basic(self):
        # Arrange
        ticker = "AMZN"

        # Act
        text, param = get_random_condition(self.rng, ticker=ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)

    def test_get_random_condition_up_to_1(self):
        # Arrange
        ticker = "AMZN"

        # Act
        text, param = get_random_condition(self.rng, up_to_n=1, ticker=ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)

    def test_get_random_condition_large_n(self):
        # Arrange
        ticker = "MSFT"

        # Act
        text, param = get_random_condition(self.rng, up_to_n=10, ticker=ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)

    def test_get_random_condition_multiple_runs_different_outputs(self):
        # Arrange
        ticker = "BTC"

        # Act
        outputs = {get_random_condition(self.rng, ticker=ticker)[0] for _ in range(5)}

        # Assert
        self.assertGreater(len(outputs), 1)

    def test_get_random_condition_handles_empty_ops(self):
        # Arrange
        ticker = "ETH"

        # Act
        text, param = get_random_condition(self.rng, up_to_n=1, ticker=ticker)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)

    def test_process_one_trading_series_seeded_consistency(self):
        # Arrange
        ticker = "AAPL"
        rng1 = random.Random(123)
        rng2 = random.Random(123)

        # Act
        text1, param1 = process_one_trading_series(rng1, ticker)
        text2, param2 = process_one_trading_series(rng2, ticker)

        # Assert
        self.assertEqual(text1, text2)
        self.assertEqual(param1, param2)

    def test_create_condition_seeded_consistency(self):
        # Arrange
        ticker = "AAPL"
        rng1 = random.Random(123)
        rng2 = random.Random(123)

        # Act
        text1, param1 = create_condition(rng1, ticker)
        text2, param2 = create_condition(rng2, ticker)

        # Assert
        self.assertEqual(text1, text2)
        self.assertEqual(param1, param2)


if __name__ == '__main__':
    unittest.main()
