import unittest
import pandas as pd

from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trade.trade import Trade
from trading_strategy_tester.trade.order_size.order_size import OrderSize
from trading_strategy_tester.trade.trade_commissions.percentage_commissions import PercentageCommissions


class MockOrderSize(OrderSize):
    def __init__(self, value=1):
        super().__init__(value)

    def get_invested_amount(self, price: float, capital: float) -> tuple:
        contracts = capital // price
        invested = contracts * price
        return invested, contracts



class TestTrade(unittest.TestCase):
    def setUp(self):
        self.initial_capital = 10000
        self.trade_commissions = PercentageCommissions(2.0)  # 2% commission
        self.order_size = MockOrderSize()

        # Build a dummy dataframe with price and signal data
        self.df = pd.DataFrame({
            SourceType.OPEN.value: [100, 105, 110],
            SourceType.HIGH.value: [102, 108, 115],
            SourceType.LOW.value: [95, 101, 109],
            SourceType.CLOSE.value: [101, 107, 111],
            'BUY_Signals': ['Buy', '', ''],
            'SELL_Signals': ['', '', 'Sell']
        }, index=pd.date_range(start="2024-01-01", periods=3))

    def test_trade_metrics_are_computed_correctly(self):
        # Arrange
        trade = Trade(
            df_slice=self.df,
            trade_id=1,
            order_size=self.order_size,
            current_capital=self.initial_capital,
            initial_capital=self.initial_capital,
            trade_commissions=self.trade_commissions,
            long=True
        )

        # Assert key trade metrics
        self.assertEqual(trade.entry_price, 100)
        self.assertEqual(trade.exit_price, 110)
        self.assertEqual(trade.entry_signal, 'Buy')
        self.assertEqual(trade.exit_signal, 'Sell')
        self.assertGreater(trade.invested, 0)
        self.assertGreater(trade.contracts, 0)
        self.assertGreaterEqual(trade.p_and_l, 0)
        self.assertTrue(isinstance(trade.get_summary(), dict))
        self.assertTrue(isinstance(trade.get_summary_with_units(), dict))

    def test_capital_is_updated_correctly(self):
        # Act
        trade = Trade(
            df_slice=self.df,
            trade_id=1,
            order_size=self.order_size,
            current_capital=self.initial_capital,
            initial_capital=self.initial_capital,
            trade_commissions=self.trade_commissions,
            long=True
        )

        # Assert capital is updated after trade
        self.assertNotEqual(trade.current_capital, self.initial_capital)

    def test_stop_loss_detection(self):
        # Arrange
        self.df.loc[self.df.index[-1], 'SELL_Signals'] = 'StopLoss(5.0)'
        trade = Trade(
            df_slice=self.df,
            trade_id=2,
            order_size=self.order_size,
            current_capital=self.initial_capital,
            initial_capital=self.initial_capital,
            trade_commissions=self.trade_commissions,
            long=True
        )

        # Act
        result = trade.exit_is_stop_loss()

        # Assert
        self.assertTrue(result[0])
        self.assertAlmostEqual(result[1], 5.0)

    def test_take_profit_detection(self):
        # Arrange
        self.df.loc[self.df.index[-1], 'SELL_Signals'] = 'TakeProfit(7.5)'
        trade = Trade(
            df_slice=self.df,
            trade_id=3,
            order_size=self.order_size,
            current_capital=self.initial_capital,
            initial_capital=self.initial_capital,
            trade_commissions=self.trade_commissions,
            long=True
        )

        # Act
        result = trade.exit_is_take_profit()

        # Assert
        self.assertTrue(result[0])
        self.assertAlmostEqual(result[1], 7.5)

    def test_repr_formatting(self):
        # Arrange
        trade = Trade(
            df_slice=self.df,
            trade_id=4,
            order_size=self.order_size,
            current_capital=self.initial_capital,
            initial_capital=self.initial_capital,
            trade_commissions=self.trade_commissions,
            long=False
        )

        # Act
        representation = repr(trade)

        # Assert
        self.assertIn("Trade(", representation)
        self.assertIn("Short", representation)


if __name__ == '__main__':
    unittest.main()
