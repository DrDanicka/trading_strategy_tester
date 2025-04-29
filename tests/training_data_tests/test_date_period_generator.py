import unittest
import random

from trading_strategy_tester.training_data.start_end_date_generator import (
    get_random_start_end_dates,
    get_random_period
)
from trading_strategy_tester.enums.period_enum import Period


class TestStartEndDateGenerator(unittest.TestCase):

    def setUp(self):
        """Set up a seeded random generator for reproducibility."""
        self.rng = random.Random(42)

    # --- Tests for get_random_start_end_dates ---

    def test_get_random_start_date_seeded(self):
        # Arrange

        # Act
        date_text, date_param = get_random_start_end_dates(self.rng, start=True)

        # Assert
        self.assertIsInstance(date_text, str)
        self.assertIsInstance(date_param, str)
        self.assertIn('start', date_text.lower())
        self.assertTrue(date_param.startswith('datetime('))

    def test_get_random_end_date_seeded(self):
        # Arrange

        # Act
        date_text, date_param = get_random_start_end_dates(self.rng, start=False)

        # Assert
        self.assertIsInstance(date_text, str)
        self.assertIsInstance(date_param, str)
        self.assertIn('end', date_text.lower())
        self.assertTrue(date_param.startswith('datetime('))

    def test_get_random_start_end_date_values_are_different(self):
        # Arrange

        # Act
        start_text, start_param = get_random_start_end_dates(self.rng, start=True)
        end_text, end_param = get_random_start_end_dates(self.rng, start=False)

        # Assert
        self.assertNotEqual(start_text, end_text)
        self.assertNotEqual(start_param, end_param)

    # --- Tests for get_random_period ---

    def test_get_random_period_seeded(self):
        # Arrange

        # Act
        period_text, period_param = get_random_period(self.rng)

        # Assert
        self.assertIsInstance(period_text, str)
        self.assertIsInstance(period_param, str)
        self.assertTrue(period_param.startswith('Period.'))

    def test_get_random_period_returns_valid_enum(self):
        # Arrange

        # Act
        _, period_param = get_random_period(self.rng)

        # Assert
        valid_periods = [str(period) for period in Period]
        self.assertIn(period_param, valid_periods)

    def test_get_random_period_multiple_unique(self):
        # Arrange

        # Act
        results = {get_random_period(self.rng)[1] for _ in range(10)}

        # Assert
        self.assertGreater(len(results), 1)


if __name__ == '__main__':
    unittest.main()
