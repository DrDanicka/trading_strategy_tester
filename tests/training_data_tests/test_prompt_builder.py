import unittest
import random

from trading_strategy_tester.training_data.prompt_builder import PromptBuilder, DateORPeriodEnum


class TestPromptBuilder(unittest.TestCase):

    def setUp(self):
        """Set up a seeded PromptBuilder instance for reproducibility."""
        self.pb = PromptBuilder(random_seed=42)

    # --- Tests for __init__ ---

    def test_initial_seed_is_set(self):
        # Arrange

        # Act
        seed = self.pb.random_seed

        # Assert
        self.assertEqual(seed, 42)

    def test_rng_instance_created(self):
        # Arrange

        # Act
        rng = self.pb.rng

        # Assert
        self.assertIsInstance(rng, random.Random)

    def test_default_flags_are_false(self):
        # Arrange

        # Act

        # Assert
        self.assertFalse(self.pb.take_profit_bool)
        self.assertFalse(self.pb.stop_loss_bool)
        self.assertFalse(self.pb.interval_bool)
        self.assertFalse(self.pb.initial_capital_bool)
        self.assertFalse(self.pb.order_size_bool)
        self.assertFalse(self.pb.trade_commissions_bool)

    # --- Tests for _get_random_true_false_with_weights ---

    def test_random_true_false_with_weights_bias_towards_true(self):
        # Arrange

        # Act
        result = [self.pb._get_random_true_false_with_weights(true_weight=90, false_weight=10) for _ in range(100)]

        # Assert
        self.assertGreater(result.count(True), result.count(False))

    def test_random_true_false_with_weights_bias_towards_false(self):
        # Arrange

        # Act
        result = [self.pb._get_random_true_false_with_weights(true_weight=10, false_weight=90) for _ in range(100)]

        # Assert
        self.assertGreater(result.count(False), result.count(True))

    # --- Tests for regenerate_bools ---

    def test_regenerate_bools_sets_flags(self):
        # Arrange

        # Act
        self.pb.regenerate_bools()

        # Assert
        # At least one should become True randomly
        flags = [
            self.pb.take_profit_bool,
            self.pb.stop_loss_bool,
            self.pb.interval_bool,
            self.pb.initial_capital_bool,
            self.pb.order_size_bool,
            self.pb.trade_commissions_bool
        ]
        self.assertIn(True, flags)

    def test_regenerate_bools_sets_date_or_period_enum(self):
        # Arrange

        # Act
        self.pb.regenerate_bools()

        # Assert
        self.assertIn(self.pb.date_or_period, list(DateORPeriodEnum))

    def test_regenerate_bools_date_sets_start_end_booleans(self):
        # Arrange
        self.pb.date_or_period = DateORPeriodEnum.DATE

        # Act
        self.pb.regenerate_bools()

        # Assert
        if self.pb.date_or_period == DateORPeriodEnum.DATE:
            self.assertIn(self.pb.start_date_bool, [True, False])
            self.assertIn(self.pb.end_date_bool, [True, False])

    def test_regenerate_bools_period_sets_period_flag(self):
        # Arrange
        self.pb.date_or_period = DateORPeriodEnum.PERIOD

        # Act
        self.pb.regenerate_bools()

        # Assert
        if self.pb.date_or_period == DateORPeriodEnum.PERIOD:
            self.assertTrue(self.pb.period_bool)

    # --- Tests for generate_prompt ---

    def test_generate_prompt_outputs_structure(self):
        # Arrange

        # Act
        prompt, strategy_object, strategy_dict = self.pb.generate_prompt()

        # Assert
        self.assertIsInstance(prompt, str)
        self.assertIsInstance(strategy_object, str)
        self.assertIsInstance(strategy_dict, dict)

    def test_generate_prompt_contains_ticker(self):
        # Arrange

        # Act
        prompt, strategy_object, strategy_dict = self.pb.generate_prompt()

        # Assert
        self.assertIn('ticker=', strategy_object)

    def test_generate_prompt_conditions_in_dict(self):
        # Arrange

        # Act
        prompt, strategy_object, _ = self.pb.generate_prompt()


        # Assert
        self.assertTrue('buy_condition' in strategy_object)

    def test_generate_prompt_fields_formatting(self):
        # Arrange

        # Act
        _, _, strategy_dict = self.pb.generate_prompt()

        # Assert
        for key, value in strategy_dict.items():
            self.assertIsInstance(value, str)  # All fields should be strings
            # Value can be empty if that optional field wasn't set

    def test_generate_prompt_strategy_object_valid_brackets(self):
        # Arrange

        # Act
        _, strategy_object, _ = self.pb.generate_prompt()

        # Assert
        self.assertEqual(strategy_object.count('('), strategy_object.count(')'))

    def test_multiple_generate_prompt_calls_produce_varied_prompts(self):
        # Arrange

        # Act
        prompts = {self.pb.generate_prompt()[0] for _ in range(5)}

        # Assert
        self.assertGreater(len(prompts), 1)


if __name__ == '__main__':
    unittest.main()
