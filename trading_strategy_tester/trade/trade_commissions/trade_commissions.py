from abc import ABC, abstractmethod

class TradeCommissions(ABC):
    """
    An abstract base class to represent the concept of trade commissions.
    This class should be subclassed to implement specific commission calculation strategies.
    """

    def __init__(self, value: float):
        """
        Initializes the TradeCommissions object with a base value.

        :param value: The base value used for calculating commissions.
        :type value: float
        """
        self.value = value

    @abstractmethod
    def get_commission(self, invested: float, contracts: float) -> float:
        """
        Abstract method to calculate the commission based on the given price.
        This method must be implemented by subclasses.

        :param contracts: The amount of contracts in trade.
        :type contracts: float
        :param invested: The invested amount on which the commission is calculated.
        :type invested: float
        :return: The commission amount for the given price.
        :rtype: float
        """
        pass

    def to_dict(self):
        """
        Converts the TradeCommissions object to a dictionary representation.

        :return: A dictionary containing the commission value.
        :rtype: dict
        """
        return {'value': self.value}
