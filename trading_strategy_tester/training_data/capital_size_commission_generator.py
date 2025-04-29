import random
from trading_strategy_tester.training_data.prompt_data.string_options import (
    initial_capital,
    order_size_uds,
    order_size_percent_of_equity,
    order_size_contracts,
    trade_commissions_money,
    trade_commissions_percentage
)
from enum import Enum

# Enum for different order sizing methods
class OrderSizes(Enum):
    USD = 0  # Fixed amount in USD
    PERCENT_OF_EQUITY = 1  # Percentage of account equity
    CONTRACTS = 2  # Fixed number of contracts

# Enum for different commission calculation methods
class TradeCommissions(Enum):
    MONEY = 0  # Fixed monetary commission
    PERCENTAGE = 1  # Percentage-based commission

def get_random_initial_capital(rng: random.Random = None):
    '''
    Generate a random initial capital value for the trading account.

    The capital is randomly selected between 1,000 and 1,000,000 USD.
    A textual description and the actual numeric parameter are both returned.

    :param rng: Optional random number generator instance for reproducibility.
    :type rng: random.Random
    :return: A tuple (description_text, parameter_value).
    :rtype: tuple[str, str]
    '''
    rng = rng or random
    random_initial_capital = rng.randint(1000, 1000000)

    initial_capital_text = rng.choice(initial_capital).format(capital=random_initial_capital)
    initial_capital_param = f'{random_initial_capital}'

    return initial_capital_text, initial_capital_param

def get_random_order_size(rng: random.Random = None):
    '''
    Generate a random order size setting for a trading strategy.

    Randomly chooses among fixed USD, percent of equity, or number of contracts.
    Returns both a human-readable text and the machine-usable parameter.

    :param rng: Optional random number generator instance for reproducibility.
    :type rng: random.Random
    :return: A tuple (description_text, parameter_value).
    :rtype: tuple[str, str]
    '''
    rng = rng or random
    random_order_type = rng.randint(1, 3) - 1

    if random_order_type == OrderSizes.USD.value:
        order_size = rng.randint(1000, 1000000)
        order_size_text = rng.choice(order_size_uds).format(order_size=order_size)
        order_size_param = f'USD({order_size})'
    elif random_order_type == OrderSizes.PERCENT_OF_EQUITY.value:
        order_size = rng.randint(1, 100)
        order_size_text = rng.choice(order_size_percent_of_equity).format(order_size=order_size)
        order_size_param = f'PercentOfEquity({order_size})'
    else:  # OrderSizes.CONTRACTS
        order_size = rng.randint(1, 50)
        order_size_text = rng.choice(order_size_contracts).format(order_size=order_size)
        order_size_param = f'Contracts({order_size})'

    return order_size_text, order_size_param

def get_random_commission(rng: random.Random = None):
    '''
    Generate a random commission structure for trading operations.

    Randomly decides between a fixed money commission and a percentage-based commission.
    Returns both a human-readable text and the machine-usable parameter.

    :param rng: Optional random number generator instance for reproducibility.
    :type rng: random.Random
    :return: A tuple (description_text, parameter_value).
    :rtype: tuple[str, str]
    '''
    rng = rng or random
    random_commission = rng.randint(1, 2) - 1

    if random_commission == TradeCommissions.MONEY.value:
        commission = rng.randint(1, 100)
        commission_text = rng.choice(trade_commissions_money).format(commissions=commission)
        commission_param = f'MoneyCommissions({commission})'
    else:  # TradeCommissions.PERCENTAGE
        commission = rng.randint(1, 10)
        commission_text = rng.choice(trade_commissions_percentage).format(commissions=commission)
        commission_param = f'PercentageCommissions({commission})'

    return commission_text, commission_param
