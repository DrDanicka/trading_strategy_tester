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
        super().__init__(value)

    def get_commission(self, price: float) -> float:
        """
        Returns the fixed commission amount.

        :param price: The price of the trade (not used in calculation for fixed commission).
        :type price: float
        :return: The fixed commission amount.
        :rtype: float
        """
        return self.value
