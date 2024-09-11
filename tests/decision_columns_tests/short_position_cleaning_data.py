import unittest
import pandas as pd

from trading_strategy_tester.position_types.short import Short


class TestCleaningData(unittest.TestCase):

    def setUp(self):
        self.long_position = Short()

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
                'BUY': [False, False, False, False, True],
                'SELL': [False, False, False, True, False],
                'Long': [None, None, None, None, None],
                'Short': [None, None, None, 'ShortEntry', 'ShortExit']
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_multiple_buys(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, False, True, True],
                'SELL': [True, False, False, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, True, False],
                'SELL': [True, False, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': ['ShortEntry', None, None, 'ShortExit', None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buy_and_sell_on_same_day_as_start(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, True, False],
                'SELL': [True, True, False, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, True, False],
                'SELL': [False, True, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, 'ShortEntry', None, 'ShortExit', None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buy_and_sell_on_same_day_as_exit(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, False, True, False],
                'SELL': [False, True, False, True, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, True, False],
                'SELL': [False, True, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, 'ShortEntry', None, 'ShortExit', None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_last_day_sell(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, False, False, False],
                'SELL': [False, False, False, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, False],
                'SELL': [False, False, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_sell_without_buy(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, False, False, False],
                'SELL': [False, False, True, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buy_first(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_last_day_buy_and_sell_with_sell(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_last_day_buy_and_sell_without_buy(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, False, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, False],
                'SELL': [False, False, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_delete_tailing_buys(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, True, True],
                'SELL': [True, False, False, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [True, False, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': ['ShortEntry', None, 'ShortExit', None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_multiple_trades(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, True, False, False, True],
                'SELL': [True, False, True, True, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, True, False, False, True],
                'SELL': [True, False, True, False, False],
                'Long': [None, None, None, None, None],
                'Short': ['ShortEntry', 'ShortExit', 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buy_sell_on_the_same_day_in_the_middle(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, False, True],
                'SELL': [True, False, True, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [True, False, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': ['ShortEntry', None, 'ShortExit', None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

if __name__ == '__main__':
    unittest.main()