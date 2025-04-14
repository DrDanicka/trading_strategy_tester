import random
from trading_strategy_tester.training_data.prompt_data.string_options import initial_capital, order_size_uds, order_size_percent_of_equity, order_size_contracts, trade_commissions_money, trade_commissions_percentage
from enum import Enum

class OrderSizes(Enum):
    USD = 0
    PERCENT_OF_EQUITY = 1
    CONTRACTS = 2

class TradeCommissions(Enum):
    MONEY = 0
    PERCENTAGE = 1

def get_random_initial_capital(rng: random.Random=None):
    '''
    This function returns a random initial capital from 1000 to 1000000.

    :return: A tuple containing the initial capital text and parameter.
    :rtype: tuple
    '''

    random_initial_capital = rng.randint(1000, 1000000)

    initial_capital_text = rng.choice(initial_capital).format(capital=random_initial_capital)
    initial_capital_param = f'{random_initial_capital}'

    return initial_capital_text, initial_capital_param

def get_random_order_size(rng: random.Random=None):
    '''
    This function returns a random order size.

    :return: A tuple containing the order size text and parameter.
    :rtype: tuple
    '''
    random_order_type = rng.randint(1, 3)

    if random_order_type == OrderSizes.USD.value:
        order_size = rng.randint(1000, 1000000)
        order_size_text = rng.choice(order_size_uds).format(order_size=order_size)
        order_size_param = f'USD({order_size})'
    elif random_order_type == OrderSizes.PERCENT_OF_EQUITY.value:
        order_size = rng.randint(1, 100)
        order_size_text = rng.choice(order_size_percent_of_equity).format(order_size=order_size)
        order_size_param = f'PercentOfEquity({order_size})'
    else:
        order_size = rng.randint(1, 50)
        order_size_text = rng.choice(order_size_contracts).format(order_size=order_size)
        order_size_param = f'Contracts({order_size})'

    return order_size_text, order_size_param


def get_random_commission(rng: random.Random=None):
    random_commission = rng.randint(1, 2)

    if random_commission == TradeCommissions.MONEY.value:
        commission = rng.randint(1, 100)
        commission_text = rng.choice(trade_commissions_money).format(commissions=commission)
        commission_param = f'MoneyCommission({commission})'
    else:
        commission = rng.randint(1, 10)
        commission_text = rng.choice(trade_commissions_percentage).format(commissions=commission)
        commission_param = f'PercentageCommissions({commission})'

    return commission_text, commission_param