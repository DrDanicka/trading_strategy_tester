import random
from trading_strategy_tester.training_data.prompt_data.string_options import stop_loss_normal, stop_loss_trailing, take_profit

def get_random_stop_loss():
    '''
    This function returns a random stop loss text and parameter.

    :return: A tuple containing the stop loss text and parameter.
    :rtype: tuple
    '''
    trailing_stop_loss = random.choices([True, False], weights=[20, 80])[0]

    # Generate random percentage from 0.1 to 50
    random_percentage = round(random.uniform(0.1, 50), 2)

    if not trailing_stop_loss:
        # We set normal stop loss
        stop_loss_text = f'{random.choice(stop_loss_normal).format(percentage=random_percentage)}'
        stop_loss_param = f'StopLoss(percentage={random_percentage}, stop_loss_type=StopLossType.NORMAL)'
    else:
        # We set trailing stop loss
        stop_loss_text = f'{random.choice(stop_loss_trailing).format(percentage=random_percentage)}'
        stop_loss_param = f'StopLoss(percentage={random_percentage}, stop_loss_type=StopLossType.TRAILING)'

    return stop_loss_text, stop_loss_param


def get_random_take_profit():
    '''
    This function returns a random take profit text and parameter.

    :return: A tuple containing the take profit text and parameter.
    :rtype: tuple
    '''
    # Generate random percentage from 0.1 to 50
    random_percentage = round(random.uniform(0.1, 50), 2)

    take_profit_text = f'{random.choice(take_profit).format(percentage=random_percentage)}'
    take_profit_param = f'TakeProfit(percentage={random_percentage})'

    return take_profit_text, take_profit_param