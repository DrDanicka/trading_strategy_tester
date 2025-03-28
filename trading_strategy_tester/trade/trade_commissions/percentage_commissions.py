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
        # Ensure value is non-negative
        if value < 0:
            value = 0.0

        # Ensure the value does not exceed 100%
        if value > 100:
            value = 100.0
        super().__init__(value)

    def get_commission(self, invested: float, contracts: float) -> float:
        """
        Calculates the commission as a percentage of the provided trade price.

        :param contracts: The amount of contracts in trade.
        :type contracts: float
        :param invested: The invested amount on which the commission is calculated.
        :type invested: float
        :return: The calculated commission amount.
        :rtype: float
        """
        return (self.value / 100) * invested
