from abc import ABC, abstractmethod


class OrderSize(ABC):

    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        pass