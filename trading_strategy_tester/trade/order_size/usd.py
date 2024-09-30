from trading_strategy_tester.trade.order_size.order_size import OrderSize


class USD(OrderSize):
    """
    A subclass of OrderSize that represents a fixed order size in US dollars.

    This class calculates the invested amount as a specified dollar value and determines how many shares
    or contracts can be purchased with that amount.

    :param value: The fixed dollar amount to invest in the trade.
    :type value: float
    """

    def __init__(self, value: float):
        """
        Initializes the USD object with a specific dollar amount to invest.

        :param value: The fixed dollar amount to be invested in the trade.
        :type value: float
        """
        super().__init__(value)

    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        """
        Returns the fixed dollar amount to invest and the number of shares or contracts that can be purchased.

        :param share_price: The price of a single share or contract.
        :type share_price: float
        :param current_capital: The available capital (equity) for the trade. This parameter is not used in this method
                                as the investment amount is fixed.

        :return: A tuple containing:
                 - The fixed dollar amount to invest.
                 - The number of shares or contracts that can be purchased with the invested amount.
        :rtype: tuple(float, float)
        """
        return self.value, self.value / share_price  # Return the invested amount and the number of shares
