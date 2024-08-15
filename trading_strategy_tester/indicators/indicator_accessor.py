import pandas as pd
from pandas.api.extensions import register_dataframe_accessor
from .rsi import rsi

@register_dataframe_accessor('indicator')
class IndicatorAccessor:
    def __init__(self, df):
        self._df = df

    def rsi(self, column:str ='Close', length:int = 14) -> pd.DataFrame:
        rsi_values = rsi(self._df[column], length)
        self._df[f'RSI_{column}_{length}'] = rsi_values
        return self._df