import random
from enum import Enum

# Importing random generation utilities for various trading strategy parts
from trading_strategy_tester.training_data.stop_loss_take_profit_generator import get_random_stop_loss, get_random_take_profit
from trading_strategy_tester.training_data.start_end_date_generator import get_random_start_end_dates, get_random_period
from trading_strategy_tester.training_data.strategy_type_generator import get_random_strategy_type
from trading_strategy_tester.training_data.ticker_generator import get_random_ticker
from trading_strategy_tester.training_data.condition_generator import get_random_condition
from trading_strategy_tester.training_data.prompt_data.string_options import prompt_starts, buy_sell_action_conditions, buy_actions, sell_actions
from trading_strategy_tester.training_data.interval_generator import get_random_interval
from trading_strategy_tester.training_data.capital_size_commission_generator import get_random_initial_capital, get_random_commission, get_random_order_size

# Enum for choosing whether to add start/end dates, a trading period, or none
class DateORPeriodEnum(Enum):
    DATE = 0
    PERIOD = 1
    NOTHING = 2

class PromptBuilder:
    """
    A class responsible for dynamically generating random trading strategy prompts
    along with the corresponding strategy object and a structured dictionary of parameters.
    """

    def __init__(self, random_seed: int = 42):
        """
        Initialize the PromptBuilder with a random seed for reproducibility.

        :param random_seed: Seed value for the random number generator.
        """
        self.random_seed = random_seed
        self.rng = random.Random(self.random_seed)

        # Flags controlling which optional parts are included
        self.take_profit_bool = False
        self.stop_loss_bool = False
        self.date_or_period = DateORPeriodEnum.NOTHING
        self.start_date_bool = False
        self.end_date_bool = False
        self.interval_bool = False
        self.period_bool = False
        self.initial_capital_bool = False
        self.order_size_bool = False
        self.trade_commissions_bool = False

        # Weights for random true/false decisions
        self.true_weight = 40
        self.false_weight = 60

        self.max_number_of_conditions = 3

    def _get_random_true_false_with_weights(self, true_weight: int, false_weight: int) -> bool:
        """
        Randomly return True or False based on specified weights.

        :param true_weight: Weight for selecting True.
        :param false_weight: Weight for selecting False.
        :return: Boolean decision.
        """
        return self.rng.choices([True, False], weights=[true_weight, false_weight])[0]

    def regenerate_bools(self):
        """
        Randomly regenerate the set of booleans controlling which strategy fields are included.
        """
        self.take_profit_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.stop_loss_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.interval_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.initial_capital_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.order_size_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.trade_commissions_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)

        # Randomly select whether to use date range, period, or nothing
        self.date_or_period = self.rng.choices(
            [DateORPeriodEnum.DATE, DateORPeriodEnum.PERIOD, DateORPeriodEnum.NOTHING],
            weights=[35, 25, 40]
        )[0]

        # Configure date-related booleans
        if self.date_or_period == DateORPeriodEnum.DATE:
            self.start_date_bool = self._get_random_true_false_with_weights(60, 40)
            self.end_date_bool = self._get_random_true_false_with_weights(60, 40)
            if not self.start_date_bool and not self.end_date_bool:
                self.date_or_period = DateORPeriodEnum.NOTHING
                self.period_bool = False
        elif self.date_or_period == DateORPeriodEnum.PERIOD:
            self.start_date_bool = False
            self.end_date_bool = False
            self.period_bool = True
        else:
            self.start_date_bool = False
            self.end_date_bool = False
            self.period_bool = False

    def generate_prompt(self) -> (str, str, dict):
        """
        Generate a random prompt describing a trading strategy, the associated Strategy object,
        and a dictionary of its parameters.

        :return: Tuple of (natural language prompt, Strategy object string, parameters dictionary)
        """
        self.regenerate_bools()
        strategy_object_dict = {}

        # Initialize all parameters
        stop_loss_param = None
        take_profit_param = None
        start_date_param = None
        end_date_param = None
        period_param = None
        interval_param = None
        initial_capital_param = None
        order_size_param = None
        trade_commissions_param = None

        # Generate ticker, strategy type, buy and sell conditions
        ticker_text, ticker_param = get_random_ticker(self.rng)
        strategy_type_text, strategy_type_param = get_random_strategy_type(self.rng)
        buy_condition_text, buy_condition_param = get_random_condition(self.rng, up_to_n=self.max_number_of_conditions, ticker=ticker_param)
        sell_condition_text, sell_condition_param = get_random_condition(self.rng, up_to_n=self.max_number_of_conditions, ticker=ticker_param)

        # Build the initial part of the prompt
        prompt = f'{self.rng.choice(prompt_starts).format(strategy_type=strategy_type_text, ticker=ticker_text)}'
        buy_condition_text = f'{self.rng.choice(buy_sell_action_conditions).format(action=self.rng.choice(buy_actions), condition=buy_condition_text)}'
        sell_condition_text = f'{self.rng.choice(buy_sell_action_conditions).format(action=self.rng.choice(sell_actions), condition=sell_condition_text)}'

        # Randomize the order of buy/sell conditions
        if self.rng.choice([True, False]):
            prompt += f'{buy_condition_text} and {sell_condition_text}.'
        else:
            prompt += f'{sell_condition_text} and {buy_condition_text}.'

        # Start building the Strategy object string
        strategy_object = f"Strategy(ticker='{ticker_param}', position_type={strategy_type_param}, buy_condition={buy_condition_param}, sell_condition={sell_condition_param}"

        # Append optional strategy parameters if enabled
        if self.stop_loss_bool:
            stop_loss_text, stop_loss_param = get_random_stop_loss(self.rng)
            prompt += f' {stop_loss_text}.'
            strategy_object += f', stop_loss={stop_loss_param}'

        if self.take_profit_bool:
            take_profit_text, take_profit_param = get_random_take_profit(self.rng)
            prompt += f' {take_profit_text}.'
            strategy_object += f', take_profit={take_profit_param}'

        if self.date_or_period == DateORPeriodEnum.DATE:
            if self.start_date_bool:
                start_date_text, start_date_param = get_random_start_end_dates(self.rng, start=True)
                prompt += f' {start_date_text}.'
                strategy_object += f', start_date={start_date_param}'
            if self.end_date_bool and self.start_date_bool:
                end_date_text, end_date_param = get_random_start_end_dates(self.rng, start=False)
                prompt += f' {end_date_text}.'
                strategy_object += f', end_date={end_date_param}'
        elif self.date_or_period == DateORPeriodEnum.PERIOD:
            period_text, period_param = get_random_period(self.rng)
            prompt += f' {period_text}.'
            strategy_object += f', period={period_param}'

        if self.interval_bool:
            interval_text, interval_param = get_random_interval(self.rng)
            prompt += f' {interval_text}.'
            strategy_object += f', interval={interval_param}'

        if self.initial_capital_bool:
            initial_capital_text, initial_capital_param = get_random_initial_capital(self.rng)
            prompt += f' {initial_capital_text}.'
            strategy_object += f', initial_capital={initial_capital_param}'

        if self.order_size_bool:
            order_size_text, order_size_param = get_random_order_size(self.rng)
            prompt += f' {order_size_text}.'
            strategy_object += f', order_size={order_size_param}'

        if self.trade_commissions_bool:
            trade_commissions_text, trade_commissions_param = get_random_commission(self.rng)
            prompt += f' {trade_commissions_text}.'
            strategy_object += f', trade_commissions={trade_commissions_param}'

        strategy_object += ')'

        # Create dictionary mapping
        strategy_object_dict['ticker'] = f"ticker='{ticker_param}'"
        strategy_object_dict['position_type'] = f'position_type={strategy_type_param}'
        strategy_object_dict['conditions'] = f'buy_condition={buy_condition_param}, sell_condition={sell_condition_param}'
        strategy_object_dict['stop_loss'] = f'stop_loss={stop_loss_param}' if stop_loss_param else ''
        strategy_object_dict['take_profit'] = f'take_profit={take_profit_param}' if take_profit_param else ''
        strategy_object_dict['start_date'] = f'start_date={start_date_param}' if start_date_param else ''
        strategy_object_dict['end_date'] = f'end_date={end_date_param}' if end_date_param else ''
        strategy_object_dict['period'] = f'period={period_param}' if period_param else ''
        strategy_object_dict['interval'] = f'interval={interval_param}' if interval_param else ''
        strategy_object_dict['initial_capital'] = f'initial_capital={initial_capital_param}' if initial_capital_param else ''
        strategy_object_dict['order_size'] = f'order_size={order_size_param}' if order_size_param else ''
        strategy_object_dict['trade_commissions'] = f'trade_commissions={trade_commissions_param}' if trade_commissions_param else ''

        return prompt, strategy_object, strategy_object_dict
