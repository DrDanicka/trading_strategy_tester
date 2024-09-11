from abc import ABC, abstractmethod

import pandas as pd


class PositionType(ABC):

    @abstractmethod
    def clean_buy_sell_columns(self, df: pd.DataFrame):
        pass