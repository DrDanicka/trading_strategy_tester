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

def get_random_initial_capital():
    '''
    This function returns a random initial capital from 1000 to 1000000.

    :return: A tuple containing the initial capital text and parameter.
    :rtype: tuple
    '''

    random_initial_capital = random.randint(1000, 1000000)

    initial_capital_text = random.choice(initial_capital).format(capital=random_initial_capital)
    initial_capital_param = f'{random_initial_capital}'

    return initial_capital_text, initial_capital_param

def get_random_order_size():
    '''
    This function returns a random order size.

    :return: A tuple containing the order size text and parameter.
    :rtype: tuple
    '''
    random_order_type = random.randint(1, 3)

    if random_order_type == OrderSizes.USD.value:
        order_size = random.randint(1000, 1000000)
        order_size_text = random.choice(order_size_uds).format(order_size=order_size)
        order_size_param = f'USD(value={order_size})'
    elif random_order_type == OrderSizes.PERCENT_OF_EQUITY.value:
        order_size = random.randint(1, 100)
        order_size_text = random.choice(order_size_percent_of_equity).format(order_size=order_size)
        order_size_param = f'PercentOfEquity(value={order_size})'
    else:
        order_size = random.randint(1, 50)
        order_size_text = random.choice(order_size_contracts).format(order_size=order_size)
        order_size_param = f'Contracts(value={order_size})'

    return order_size_text, order_size_param


def get_random_commission():
    random_commission = random.randint(1, 2)

    if random_commission == TradeCommissions.MONEY.value:
        commission = random.randint(1, 100)
        commission_text = random.choice(trade_commissions_money).format(commissions=commission)
        commission_param = f'MoneyCommission(value={commission})'
    else:
        commission = random.randint(1, 10)
        commission_text = random.choice(trade_commissions_percentage).format(commissions=commission)
        commission_param = f'PercentageCommission(value={commission})'

    return commission_text, commission_param