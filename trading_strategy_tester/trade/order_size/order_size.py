from abc import ABC, abstractmethod

class OrderSize(ABC):
    """
    Abstract base class to define the structure for different order size strategies in trading.

    This class is intended to be subclassed by specific order size calculation strategies,
    such as fixed dollar amounts, percentage-based sizing, etc.
    """

    def __init__(self, value: float):
        """
        Initializes the OrderSize object with a specific value for order size.

        :param value: The size of the order. This value could represent a fixed dollar amount or a percentage of capital.
        :type value: float
        """
        self.value = value

    @abstractmethod
    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        """
        Abstract method to calculate the invested amount based on the share price and current capital.

        This method must be implemented by subclasses to define how much capital should be invested
        and how many contracts or shares are purchased.

        :param share_price: The price of a single share or contract.
        :type share_price: float
        :param current_capital: The available capital for the trade.
        :type current_capital: float

        :return: A tuple containing:
                 - The total invested amount (float).
                 - The number of contracts or shares purchased (float).
        :rtype: tuple(float, float)
        """
        pass

    def to_dict(self):
        """
        Converts the OrderSize object to a dictionary representation.

        :return: A dictionary containing the order size value.
        :rtype: dict
        """
        return {'value': self.value}