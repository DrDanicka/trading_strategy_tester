import pandas as pd
import random
import os

def get_random_ticker(rng: random.Random=None):
    '''
    This function returns a random ticker from a csv file containing a list of tickers.

    :param rng: A random number generator.
    :type rng: random.Random
    :return: A tuple containing the chosen ticker.
    :rtype: tuple
    '''

    script_dir = os.path.dirname(__file__)
    sp500_path = os.path.join(script_dir, 'prompt_data', 'sp500.csv')

    tickers = pd.read_csv(sp500_path)

    random_ticker_index = rng.randint(0, len(tickers) - 1)

    ticker_param_and_text = tickers.iloc[random_ticker_index]['Ticker']

    return ticker_param_and_text, ticker_param_and_text