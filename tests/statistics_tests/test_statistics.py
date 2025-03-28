import unittest
from unittest.mock import Mock
import pandas as pd

from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.statistics.statistics import get_strategy_stats

class TestGetStrategyStats(unittest.TestCase):
    def setUp(self):
        # Sample market data (open prices)
        self.df = pd.DataFrame({
            SourceType.OPEN.value: [100, 105, 110]
        })

        # Mock OrderSize to return fixed investment values
        self.order_size = Mock()
        self.order_size.get_invested_amount.return_value = (1000, 10)  # (amount, contracts)

        self.initial_capital = 1000

        # Sample trade summaries
        self.trade1 = Mock()
        self.trade1.get_summary.return_value = {
            'P&L': 100,
            'Percentage P&L': 10.0,
            'Commissions Paid': 5,
            'Drawdown': 20,
        }

        self.trade2 = Mock()
        self.trade2.get_summary.return_value = {
            'P&L': -50,
            'Percentage P&L': -5.0,
            'Commissions Paid': 3,
            'Drawdown': 10,
        }

    def test_stats_with_two_trades(self):
        trades = [self.trade1, self.trade2]

        stats = get_strategy_stats(trades, self.df, self.initial_capital, self.order_size)

        self.assertEqual(stats['Net Profit'], '50.0$')
        self.assertEqual(stats['Gross Profit'], '100.0$')
        self.assertEqual(stats['Gross Loss'], '-50.0$')
        self.assertEqual(stats['Profit factor'], 2.0)
        self.assertEqual(stats['Commissions Paid'], '8.0$')
        self.assertEqual(stats['Total Trades'], 2)
        self.assertEqual(stats['Number of Winning Trades'], 1)
        self.assertEqual(stats['Number of Losing Trades'], 1)
        self.assertEqual(stats['Average Trade'], '25.0$')
        self.assertEqual(stats['Largest Winning Trade'], '10.0$')
        self.assertEqual(stats['Largest Losing Trade'], '-5.0$')
        self.assertEqual(stats['P&L'], '50$')
        self.assertEqual(stats['P&L Percentage'], '5.0%')
        self.assertEqual(stats['Max Drawdown'], '20.0$')
        self.assertEqual(stats['Buy and Hold Return'], '100.0$')  # 10 contracts * (110 - 100)
        self.assertEqual(stats['Buy and Hold Return Percentage'], '110.0%')  # (110 / 100) * 100

    def test_no_trades(self):
        stats = get_strategy_stats([], self.df, self.initial_capital, self.order_size)

        self.assertEqual(stats['Net Profit'], '0.0$')
        self.assertEqual(stats['Gross Profit'], '0.0$')
        self.assertEqual(stats['Gross Loss'], '0.0$')
        self.assertEqual(stats['Profit factor'], '-')
        self.assertEqual(stats['Commissions Paid'], '0.0$')
        self.assertEqual(stats['Total Trades'], 0)
        self.assertEqual(stats['Number of Winning Trades'], 0)
        self.assertEqual(stats['Number of Losing Trades'], 0)
        self.assertEqual(stats['Average Trade'], '0.0$')
        self.assertEqual(stats['Largest Winning Trade'], '0.0$')
        self.assertEqual(stats['Largest Losing Trade'], '0.0$')
        self.assertEqual(stats['P&L'], '0$')
        self.assertEqual(stats['P&L Percentage'], '0.0%')
        self.assertEqual(stats['Max Drawdown'], '0.0$')

    def test_empty_dataframe(self):
        stats = get_strategy_stats([], pd.DataFrame(columns=[SourceType.OPEN.value]), self.initial_capital, self.order_size)
        self.assertEqual(stats['Buy and Hold Return'], '0.0$')
        self.assertEqual(stats['Buy and Hold Return Percentage'], '0.0%')

    def test_only_losing_trades(self):
        losing_trade = Mock()
        losing_trade.get_summary.return_value = {
            'P&L': -100,
            'Percentage P&L': -10.0,
            'Commissions Paid': 4,
            'Drawdown': 30,
        }

        trades = [losing_trade, losing_trade]

        stats = get_strategy_stats(trades, self.df, self.initial_capital, self.order_size)

        self.assertEqual(stats['Gross Profit'], '0.0$')
        self.assertEqual(stats['Gross Loss'], '-200.0$')
        self.assertEqual(stats['Profit factor'], 0.0)
        self.assertEqual(stats['Number of Winning Trades'], 0)
        self.assertEqual(stats['Number of Losing Trades'], 2)
        self.assertEqual(stats['Largest Losing Trade'], '-10.0$')

    def test_only_winning_trades(self):
        winning_trade = Mock()
        winning_trade.get_summary.return_value = {
            'P&L': 150,
            'Percentage P&L': 15.0,
            'Commissions Paid': 2,
            'Drawdown': 5,
        }

        trades = [winning_trade, winning_trade]

        stats = get_strategy_stats(trades, self.df, self.initial_capital, self.order_size)

        self.assertEqual(stats['Gross Loss'], '0.0$')
        self.assertEqual(stats['Gross Profit'], '300.0$')
        self.assertEqual(stats['Profit factor'], '-')  # still "-"
        self.assertEqual(stats['Number of Winning Trades'], 2)
        self.assertEqual(stats['Number of Losing Trades'], 0)
        self.assertEqual(stats['Largest Winning Trade'], '15.0$')

    def test_single_trade(self):
        trade = Mock()
        trade.get_summary.return_value = {
            'P&L': 25,
            'Percentage P&L': 2.5,
            'Commissions Paid': 1,
            'Drawdown': 3,
        }

        stats = get_strategy_stats([trade], self.df, self.initial_capital, self.order_size)

        self.assertEqual(stats['Net Profit'], '25.0$')
        self.assertEqual(stats['Average Trade'], '25.0$')
        self.assertEqual(stats['Largest Winning Trade'], '2.5$')
        self.assertEqual(stats['Max Drawdown'], '3.0$')


if __name__ == '__main__':
    unittest.main()
