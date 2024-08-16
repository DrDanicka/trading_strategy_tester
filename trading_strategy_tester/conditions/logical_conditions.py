import pandas as pd
from .condition import Condition
from ..download.download_module import DownloadModule


class AndCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule) -> pd.Series:
        result = self.conditions[0].evaluate(downloader)

        for condition in self.conditions[1:]:
            result &= condition.evaluate(downloader)

        return result


class OrCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self, downloader: DownloadModule) -> pd.Series:
        result = self.conditions[0].evaluate(downloader)

        for condition in self.conditions:
            result |= condition.evaluate(downloader)

        return result

class IfThenElseCondition(Condition):
    def __init__(self, if_condition: Condition, else_condition: Condition):
        self.if_condition = if_condition
        self.else_condition = else_condition

    def evaluate(self, downloader: DownloadModule) -> pd.Series:
        result = self.if_condition.evaluate(downloader)
        result |= self.else_condition.evaluate(downloader)

        return result