import unittest
import pandas as pd
from trading_strategy_tester.conditions.take_profit import TakeProfit

class TestTakeProfit(unittest.TestCase):

    def setUp(self):
        pass

    def test_take_profit_5_percent(self):
        # Arrange
        take_profit = TakeProfit(5)

        df = pd.DataFrame({
            'Close': [50, 54, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 54, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, True, False, False, False],
        })

        # Act
        take_profit.set_take_profit(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_take_profit_5_percent_with_no_take_profit(self):
        # Arrange
        take_profit = TakeProfit(5)

        df = pd.DataFrame({
            'Close': [50, 52, 49, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 52, 49, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        # Act
        take_profit.set_take_profit(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_take_profit_5_percent_sell_on_take_profit(self):
        # Arrange
        take_profit = TakeProfit(5)

        df = pd.DataFrame({
            'Close': [50, 52, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 52, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
        })

        # Act
        take_profit.set_take_profit(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_take_profit_5_percent_buy_on_take_profit(self):
        # Arrange
        take_profit = TakeProfit(5)

        df = pd.DataFrame({
            'Close': [50, 52, 55, 47, 51],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 52, 55, 47, 51],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, True, False, False],
        })

        # Act
        take_profit.set_take_profit(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_take_profit_5_percent_multiple_trades(self):
        # Arrange
        take_profit = TakeProfit(5)

        df = pd.DataFrame({
            'Close': [50, 52, 55, 60, 51],
            'BUY': [True, False, True, False, False],
            'SELL': [False, True, False, False, True],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 52, 55, 60, 51],
            'BUY': [True, False, True, False, False],
            'SELL': [False, True, False, True, True],
        })

if __name__ == '__main__':
    unittest.main()