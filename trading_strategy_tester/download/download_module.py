import pandas as pd
import yfinance as yf
from datetime import datetime
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.enums.period_enum import Period

class DownloadModule:
    def __init__(self, start_date:datetime, end_date:datetime, interval: Interval, period: Period):
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval.value
        self.period = period.value

    def download_ticker(self, ticker: str) -> pd.DataFrame:
        if self.period == 'not_passed':
            return yf.download(ticker, start=self.start_date, end=self.end_date, interval=self.interval)
        else:
            return yf.download(ticker, interval=self.interval, period=self.period)