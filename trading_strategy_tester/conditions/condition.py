from abc import ABC, abstractmethod
import pandas as pd

class Condition(ABC):
    @abstractmethod
    def evaluate(self) -> pd.Series:
        pass