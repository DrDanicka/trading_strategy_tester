from trading_strategy_tester.trade.order_size.order_size import OrderSize


class USD(OrderSize):
    def __init__(self, value: float):
        super().__init__(value)

    def get_invested_amount(self, share_price: float, current_capital: float) -> (float, float):
        return self.value, self.value / share_price