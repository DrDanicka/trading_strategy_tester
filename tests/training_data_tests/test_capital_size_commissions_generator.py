import unittest
import random

from trading_strategy_tester.training_data.capital_size_commission_generator import (
    get_random_initial_capital,
    get_random_order_size,
    get_random_commission
)


class TestCapitalSizeCommissionGenerators(unittest.TestCase):

    def setUp(self):
        """Create a seeded random generator for reproducibility."""
        self.rng = random.Random(42)

    def test_get_random_initial_capital_seeded(self):
        # Arrange

        # Act
        text, param = get_random_initial_capital(self.rng)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(1000 <= int(param) <= 1000000)
        self.assertIn('initial capital', text.format(capital=int(param)))

    def test_get_random_initial_capital_unseeded(self):
        # Arrange

        # Act
        text, param = get_random_initial_capital()  # No RNG passed

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(1000 <= int(param) <= 1000000)

    def test_get_random_order_size_seeded(self):
        # Arrange

        # Act
        text, param = get_random_order_size(self.rng)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(
            param.startswith('USD(') or
            param.startswith('PercentOfEquity(') or
            param.startswith('Contracts(')
        )

    def test_get_random_order_size_unseeded(self):
        # Arrange

        # Act
        text, param = get_random_order_size()  # No RNG passed

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(
            param.startswith('USD(') or
            param.startswith('PercentOfEquity(') or
            param.startswith('Contracts(')
        )

    def test_get_random_commission_seeded(self):
        # Arrange

        # Act
        text, param = get_random_commission(self.rng)

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(
            param.startswith('MoneyCommissions(') or
            param.startswith('PercentageCommissions(')
        )

    def test_get_random_commission_unseeded(self):
        # Arrange

        # Act
        text, param = get_random_commission()  # No RNG passed

        # Assert
        self.assertIsInstance(text, str)
        self.assertIsInstance(param, str)
        self.assertTrue(
            param.startswith('MoneyCommissions(') or
            param.startswith('PercentageCommissions(')
        )


if __name__ == '__main__':
    unittest.main()
