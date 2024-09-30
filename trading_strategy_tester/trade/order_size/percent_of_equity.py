from trading_strategy_tester.trade.order_size.order_size import OrderSize


class PercentOfEquity(OrderSize):
    """
    A subclass of OrderSize that represents an order size based on a percentage of the available equity (capital).

    This class calculates the invested amount as a percentage of the current capital and determines how many shares
    or contracts can be purchased with that amount of equity.

    :param value: The percentage of the total available equity to invest.
    :type value: float
    """

    def __init__(self, value: float):
        """
        Initializes the PercentOfEquity object with a specific percentage of equity to invest.

        :param value: The percentage of the total available equity to be invested.
        :type value: float
        """
        super().__init__(value)

    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        """
        Calculates the invested amount as a percentage of the current capital and the number of shares or contracts
        that can be purchased with that amount.

        :param share_price: The price of a single share or contract.
        :type share_price: float
        :param current_capital: The available capital (equity) for the trade.
        :type current_capital: float

        :return: A tuple containing:
                 - The amount of capital to invest, calculated as a percentage of the current capital.
                 - The number of shares or contracts that can be purchased with the invested amount.
        :rtype: tuple(float, float)
        """
        amount_of_equity = self.value / 100 * current_capital  # Calculate the percentage of current capital to invest
        return amount_of_equity, amount_of_equity / share_price  # Return the invested amount and the number of shares
