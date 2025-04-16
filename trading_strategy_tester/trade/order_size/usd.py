from trading_strategy_tester.trade.order_size.order_size import OrderSize


class USD(OrderSize):
    """
    A subclass of OrderSize that represents a fixed order size in US dollars.

    This class calculates the invested amount as a specified dollar value and determines how many shares
    or contracts can be purchased with that amount.
    """

    def __init__(self, value: float):
        """
        Initializes the USD object with a specific dollar amount to invest.

        :param value: The fixed dollar amount to be invested in the trade.
        :type value: float
        """
        # Ensure that the value is a non-negative float
        if value < 0:
            value = 0

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
        # Ensure that the current capital is non-negative
        if current_capital < 0:
            current_capital = 0

        if self.value > current_capital:
            return current_capital, current_capital / share_price

        return self.value, self.value / share_price  # Return the invested amount and the number of shares
