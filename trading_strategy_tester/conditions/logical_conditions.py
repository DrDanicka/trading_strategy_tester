import pandas as pd
from .condition import Condition

class AndCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self) -> pd.Series:
        result = self.conditions[0].evaluate()

        for condition in self.conditions[1:]:
            result &= condition.evaluate()

        return result


class OrCondition(Condition):
    def __init__(self, *conditions: Condition):
        self.conditions = conditions

    def evaluate(self) -> pd.Series:
        result = self.conditions[0].evaluate()

        for condition in self.conditions:
            result |= condition.evaluate()

        return result

class IfThenElseCondition(Condition):
    def __init__(self, if_condition: Condition, else_condition: Condition):
        self.if_condition = if_condition
        self.else_condition = else_condition

    def evaluate(self) -> pd.Series:
        result = self.if_condition.evaluate()
        result |= self.else_condition.evaluate()

        return result

