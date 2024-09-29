from trading_strategy_tester.trade.order_size.order_size import OrderSize


class PercentOfEquity(OrderSize):
    def __init__(self, value: float):
        super().__init__(value)

    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        amount_of_equity = self.value / 100 * current_capital

        return amount_of_equity, amount_of_equity / share_price