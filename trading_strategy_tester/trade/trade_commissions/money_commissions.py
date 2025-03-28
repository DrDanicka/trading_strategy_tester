from trading_strategy_tester.trade.trade_commissions.trade_commissions import TradeCommissions

class MoneyCommissions(TradeCommissions):
    """
    A concrete class representing a fixed monetary commission.
    The commission is a fixed amount regardless of the trade price.
    """

    def __init__(self, value: float):
        """
        Initializes the MoneyCommissions object with a fixed commission value.

        :param value: The fixed amount used as the commission.
        :type value: float
        """
        # Ensure the commission value is non-negative
        if value < 0:
            value = 0.0

        super().__init__(value)

    def get_commission(self, invested: float, contracts: float) -> float:
        """
        Returns the fixed commission amount.

        :param contracts: The amount of contracts in trade.
        :type contracts: float
        :param invested: The invested amount on which the commission is calculated.
        :type invested: float
        :return: The fixed commission amount.
        :rtype: float
        """
        return self.value * contracts
