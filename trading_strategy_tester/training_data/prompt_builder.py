import random
from enum import Enum

from trading_strategy_tester.training_data.stop_loss_take_profit_generator import get_random_stop_loss, get_random_take_profit
from trading_strategy_tester.training_data.start_end_date_generator import get_random_start_end_dates, get_random_period
from trading_strategy_tester.training_data.strategy_type_generator import get_random_strategy_type
from trading_strategy_tester.training_data.ticker_generator import get_random_ticker
from trading_strategy_tester.training_data.condition_generator import get_random_condition
from trading_strategy_tester.training_data.prompt_data.string_options import prompt_starts, buy_sell_action_conditions, buy_actions, sell_actions
from trading_strategy_tester.training_data.interval_generator import get_random_interval
from trading_strategy_tester.training_data.capital_size_commission_generator import get_random_initial_capital, get_random_commission, get_random_order_size


class DateORPeriodEnum(Enum):
    DATE = 0
    PERIOD = 1
    NOTHING = 2


class PromptBuilder:

    def __init__(self, random_seed: int = 42):
        self.random_seed = random_seed
        self.rng = random.Random(self.random_seed)

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

        self.true_weight = 40
        self.false_weight = 60

        self.max_number_of_conditions = 3

    def _get_random_true_false_with_weights(self, true_weight: int, false_weight: int) -> bool:
        return self.rng.choices([True, False], weights=[true_weight, false_weight])[0]

    def regenerate_bools(self):
        self.take_profit_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.stop_loss_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.interval_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.initial_capital_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.order_size_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)
        self.trade_commissions_bool = self._get_random_true_false_with_weights(self.true_weight, self.false_weight)

        self.date_or_period = self.rng.choices(
            [DateORPeriodEnum.DATE, DateORPeriodEnum.PERIOD, DateORPeriodEnum.NOTHING],
            weights=[35, 25, 40]
        )[0]

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

    def generate_prompt(self) -> (str, str):
        self.regenerate_bools()

        ticker_text, ticker_param = get_random_ticker(self.rng)
        strategy_type_text, strategy_type_param = get_random_strategy_type(self.rng)
        buy_condition_text, buy_condition_param = get_random_condition(self.rng, up_to_n=self.max_number_of_conditions, ticker=ticker_param)
        sell_condition_text, sell_condition_param = get_random_condition(self.rng, up_to_n=self.max_number_of_conditions, ticker=ticker_param)

        prompt = f'{self.rng.choice(prompt_starts).format(strategy_type=strategy_type_text, ticker=ticker_text)}'
        buy_condition_text = f'{self.rng.choice(buy_sell_action_conditions).format(action=self.rng.choice(buy_actions), condition=buy_condition_text)}'
        sell_condition_text = f'{self.rng.choice(buy_sell_action_conditions).format(action=self.rng.choice(sell_actions), condition=sell_condition_text)}'

        if self.rng.choice([True, False]):
            prompt += f'{buy_condition_text} and {sell_condition_text}.'
        else:
            prompt += f'{sell_condition_text} and {buy_condition_text}.'

        strategy_object = f"Strategy(ticker='{ticker_param}', position_type={strategy_type_param}, buy_condition={buy_condition_param}, sell_condition={sell_condition_param}"

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
            if self.end_date_bool:
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
        return prompt, strategy_object
