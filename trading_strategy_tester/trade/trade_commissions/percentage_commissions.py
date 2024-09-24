from trading_strategy_tester.trade.trade_commissions.trade_commissions import TradeCommissions


class PercentageCommissions(TradeCommissions):
    """
    A concrete class representing a commission calculated as a percentage of the trade price.
    The commission is a fixed percentage of the trade price.
    """

    def __init__(self, value: float):
        """
        Initializes the PercentageCommissions object with a percentage value.

        :param value: The percentage used to calculate the commission (e.g., 0.01 for 1%).
        :type value: float
        """
        super().__init__(value)

    def get_commission(self, price: float) -> float:
        """
        Calculates the commission as a percentage of the provided trade price.

        :param price: The price of the trade on which the commission is calculated.
        :type price: float
        :return: The calculated commission amount.
        :rtype: float
        """
        return self.value * price
