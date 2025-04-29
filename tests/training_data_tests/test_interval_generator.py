import unittest
import random

from trading_strategy_tester.training_data.interval_generator import get_random_interval
from trading_strategy_tester.enums.interval_enum import Interval


class TestGetRandomInterval(unittest.TestCase):

    def setUp(self):
        """Create a seeded random generator for reproducibility."""
        self.rng = random.Random(42)

    def test_get_random_interval_with_seeded_rng(self):
        # Arrange

        # Act
        interval_text, interval_param = get_random_interval(self.rng)

        # Assert
        self.assertIsInstance(interval_text, str)
        self.assertIsInstance(interval_param, str)
        self.assertTrue(any(interval.name in interval_param for interval in Interval))

    def test_get_random_interval_multiple_calls(self):
        # Arrange

        # Act
        results = {get_random_interval(self.rng) for _ in range(10)}

        # Assert
        self.assertGreater(len(results), 1)

    def test_get_random_interval_text_formatting(self):
        # Arrange

        # Act
        interval_text, interval_param = get_random_interval(self.rng)

        # Assert
        self.assertIn('day', interval_text.lower() or 'month' in interval_text.lower() or 'week' in interval_text.lower())

    def test_get_random_interval_returns_known_enum(self):
        # Arrange

        # Act
        _, interval_param = get_random_interval(self.rng)

        # Assert
        valid_intervals = [str(interval) for interval in Interval]
        self.assertIn(interval_param, valid_intervals)


if __name__ == '__main__':
    unittest.main()
