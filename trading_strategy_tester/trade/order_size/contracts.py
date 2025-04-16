from trading_strategy_tester.trade.order_size.order_size import OrderSize


class Contracts(OrderSize):
    """
    A subclass of OrderSize that represents an order size based on a fixed number of contracts.

    This class implements the method for calculating the invested amount by multiplying
    the number of contracts by the share price.
    """

    def __init__(self, value: float):
        """
        Initializes the Contracts object with a specific number of contracts.

        :param value: The fixed number of contracts to be purchased.
        :type value: float
        """
        # Ensure that the value is a non-negative float
        if value < 0:
            value = 0

        super().__init__(value)

    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        """
        Calculates the total invested amount based on the number of contracts and the share price.

        :param share_price: The price of a single share or contract.
        :type share_price: float
        :param current_capital: The available capital for the trade. This parameter is not used in this implementation
                                since the number of contracts is fixed, regardless of capital.
        :type current_capital: float

        :return: A tuple containing:
                 - The total invested amount, calculated as the number of contracts multiplied by the share price.
                 - The number of contracts, which is the value of the object.
        :rtype: tuple(float, float)
        """
        if current_capital < 0:
            current_capital = 0

        want_to_invest = self.value * share_price
        if want_to_invest > current_capital:
            return current_capital, current_capital / share_price

        return want_to_invest, self.value
