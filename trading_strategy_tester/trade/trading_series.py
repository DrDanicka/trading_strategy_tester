from datetime import datetime
from enum import Enum
import yfinance as yf
import pandas as pd
from typing import Callable, Optional

class Interval(Enum):
    ONE_MINUTE = '1m'
    TWO_MINUTES = '2m'
    FIVE_MINUTES = '5m'
    FIFTEEN_MINUTES = '15m'
    THIRTY_MINUTES = '30m'
    SIXTY_MINUTES = '60m'
    NINETY_MINUTES = '90m'
    ONE_HOUR = '1h'
    ONE_DAY = '1d'
    FIVE_DAYS = '5d'
    ONE_WEEK = '1wk'
    ONE_MONTH = '1mo'
    THREE_MONTHS = '3mo'

class TradingSeries:
    def __init__(
            self, ticker: str,
            interval: Interval = Interval.ONE_DAY,
            start_date: datetime = datetime(1970, 1, 1),
            end_date: datetime = datetime.today(),
            dataframe_func: Optional[Callable[[pd.DataFrame], pd.Series]] = None):

        #TODO check Interval with value of start and end date

        self.ticker = ticker
        self.interval = interval
        self.start_date = start_date
        self.end_date = end_date
        self.dataframe_func = dataframe_func

        self.df = yf.download(ticker, interval=self.interval.value, start=self.start_date, end=self.end_date)


    def get_data(self) -> pd.Series:
        if self.dataframe_func:
            return self.dataframe_func(self.df)
        return pd.Series([False] * len(self.df), index=self.df.index)
