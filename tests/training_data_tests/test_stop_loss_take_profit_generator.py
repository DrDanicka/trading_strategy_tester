import unittest
import random

from trading_strategy_tester.training_data.stop_loss_take_profit_generator import (
    get_random_stop_loss,
    get_random_take_profit
)


class TestStopLossTakeProfitGenerator(unittest.TestCase):

    def setUp(self):
        """Set up a seeded random generator for reproducibility."""
        self.rng = random.Random(42)

    # --- Tests for get_random_stop_loss ---

    def test_get_random_stop_loss_with_rng(self):
        # Arrange

        # Act
        stop_loss_text, stop_loss_param = get_random_stop_loss(self.rng)

        # Assert
        self.assertIsInstance(stop_loss_text, str)
        self.assertIsInstance(stop_loss_param, str)
        self.assertTrue(stop_loss_param.startswith('StopLoss('))
        self.assertIn('percentage=', stop_loss_param)
        self.assertIn('stop_loss_type=', stop_loss_param)

    def test_get_random_stop_loss_trailing_or_normal(self):
        # Arrange

        # Act
        _, stop_loss_param = get_random_stop_loss(self.rng)

        # Assert
        self.assertTrue('StopLossType.NORMAL' in stop_loss_param or 'StopLossType.TRAILING' in stop_loss_param)

    def test_get_random_stop_loss_percentage_range(self):
        # Arrange

        # Act
        _, stop_loss_param = get_random_stop_loss(self.rng)

        # Extract percentage
        percentage_str = stop_loss_param.split('percentage=')[1].split(',')[0]
        percentage = float(percentage_str)

        # Assert
        self.assertGreaterEqual(percentage, 0.1)
        self.assertLessEqual(percentage, 50)

    # --- Tests for get_random_take_profit ---

    def test_get_random_take_profit_with_rng(self):
        # Arrange

        # Act
        take_profit_text, take_profit_param = get_random_take_profit(self.rng)

        # Assert
        self.assertIsInstance(take_profit_text, str)
        self.assertIsInstance(take_profit_param, str)
        self.assertTrue(take_profit_param.startswith('TakeProfit('))
        self.assertIn('percentage=', take_profit_param)

    def test_get_random_take_profit_percentage_range(self):
        # Arrange

        # Act
        _, take_profit_param = get_random_take_profit(self.rng)

        # Extract percentage
        percentage_str = take_profit_param.split('percentage=')[1].split(')')[0]
        percentage = float(percentage_str)

        # Assert
        self.assertGreaterEqual(percentage, 0.1)
        self.assertLessEqual(percentage, 50)

    def test_get_random_take_profit_multiple_calls_variation(self):
        # Arrange

        # Act
        profits = {get_random_take_profit(self.rng)[1] for _ in range(5)}

        # Assert
        self.assertGreater(len(profits), 1)


if __name__ == '__main__':
    unittest.main()
