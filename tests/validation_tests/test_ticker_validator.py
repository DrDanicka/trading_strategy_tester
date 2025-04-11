import unittest
import ast
from trading_strategy_tester.validation.parameter_validations.ticker_validator import validate_ticker

class TestValidateTicker(unittest.TestCase):

    def test_valid_ticker(self):
        # Arrange
        ticker = ast.Constant(value='AAPL')
        changes = {}
        logs = False

        # Act
        result, new_ticker, updated_changes = validate_ticker(ticker, changes, logs)

        # Assert
        self.assertTrue(result)
        self.assertEqual(new_ticker.value, 'AAPL')
        self.assertEqual(updated_changes, {})


    def test_number_as_ticker(self):
        # Arrange
        ticker = ast.Constant(value=123)
        changes = {}
        logs = False

        # Act
        result, new_ticker, updated_changes = validate_ticker(ticker, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_ticker, 'AAPL')
        self.assertIn('ticker', updated_changes)
        self.assertEqual(updated_changes['ticker'], "ticker argument should be a string. Using default ticker 'AAPL'.")


    def test_missing_ticker_value(self):
        # Arrange
        ticker = ast.Constant(value=None)
        changes = {}
        logs = False

        # Act
        result, new_ticker, updated_changes = validate_ticker(ticker, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_ticker, 'AAPL')
        self.assertIn('ticker', updated_changes)


    def test_ticker_not_ast_constant(self):
        # Arrange
        ticker = 'TSLA'
        changes = {}
        logs = False

        # Act
        result, new_ticker, updated_changes = validate_ticker(ticker, changes, logs)

        # Assert
        self.assertFalse(result)
        self.assertEqual(new_ticker, 'AAPL')
        self.assertIn('ticker', updated_changes)


if __name__ == '__main__':
    unittest.main()
