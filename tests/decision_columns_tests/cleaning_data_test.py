import unittest
import pandas as pd

from trading_strategy_tester.conditions.trade_conditions import TradeConditions


class TestCleaningData(unittest.TestCase):

    def setUp(self):
        self.trade_condition = TradeConditions(None, None, None)

    def test_multiple_sells(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, True, False, False, False],
                'SELL': [False, False, False, True, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, True, False, False, False],
                'SELL': [False, False, False, True, False]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_multiple_buys(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, True, False, False, False],
                'SELL': [False, False, False, True, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [False, False, False, True, False],
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buy_and_sell_on_same_day_as_start(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, True, False, False, False],
                'SELL': [True, False, False, True, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, True, False, False, False],
                'SELL': [False, False, False, True, False]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buy_and_sell_on_same_day_as_exit(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, True, False, True, False],
                'SELL': [False, False, False, True, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, True, False, False, False],
                'SELL': [False, False, False, True, False]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_last_day_buy(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, False, False, True],
                'SELL': [False, False, False, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, False],
                'SELL': [False, False, False, False, False]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buy_without_sell(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, False, True, False],
                'SELL': [False, False, False, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, True, False],
                'SELL': [False, False, False, False, True]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_sell_first(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [True, False, False, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [False, False, False, False, True]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_last_day_buy_and_sell_with_buy(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, False, True],
                'SELL': [True, False, False, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [False, False, False, False, True]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_last_day_buy_and_sell_without_buy(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, False, False, True],
                'SELL': [True, False, False, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, False],
                'SELL': [False, False, False, False, False]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_delete_tailing_sells(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [False, False, True, True, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [False, False, True, False, False]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_multiple_trades(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, True, False],
                'SELL': [False, True, True, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, True, False],
                'SELL': [False, True, False, False, True]
            }
        )

        # Act
        self.trade_condition.clean_BUY_SELL_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

if __name__ == '__main__':
    unittest.main()