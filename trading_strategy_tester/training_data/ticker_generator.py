import pandas as pd
import random

def get_random_ticker():
    '''
    This function returns a random ticker from a csv file containing a list of tickers.

    :return: A tuple containing the chosen ticker or campany name and its corresponding ticker.
    :rtype: tuple
    '''

    tickers = pd.read_csv('sp500.csv')

    random_ticker_index = random.randint(0, len(tickers) - 1)
    ticker_not_company_name = random.choice([True, False])

    ticker_text = tickers.iloc[random_ticker_index]['Ticker' if ticker_not_company_name else 'Company Name']
    ticker_param = tickers.iloc[random_ticker_index]['Ticker']

    return ticker_text, ticker_param