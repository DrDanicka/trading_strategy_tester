from datetime import datetime

from conditions.indicator_conditions import RSICondition
import yfinance as yf

from trading_strategy_tester.conditions.logical_conditions import AndCondition
from trading_strategy_tester.conditions.technical_conditions import CrossOverCondition
from trading_strategy_tester.trade.trade import Trade
from trading_strategy_tester.trade.trading_series import TradingSeries
from trading_strategy_tester.indicators.rsi import rsi
from functools import partial

trade = Trade('AAPL',
              CrossOverCondition(
                                TradingSeries(ticker='AAPL', dataframe_func=partial(rsi, column='Open', length=21)),
                                TradingSeries(ticker='AAPL', dataframe_func=partial(rsi, column='Close', length=14))),
              CrossOverCondition(
                                TradingSeries(ticker='AAPL', dataframe_func=partial(rsi, column='Open', length=12)),
                                TradingSeries(ticker='AAPL', dataframe_func=partial(rsi, column='Close', length=17))),
              start_date=datetime(2020, 1, 1),
              end_date=datetime(2024, 1, 1),
              interval='1d')

df = trade.evaluate()

print(df)