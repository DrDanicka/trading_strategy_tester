import unittest
import pandas as pd

from trading_strategy_tester.position_types.long import Long


class TestCleaningData(unittest.TestCase):

    def setUp(self):
        self.long_position = Long()

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
                'SELL': [False, False, False, True, False],
                'Long': [None, 'LongEntry', None, 'LongExit', None],
                'Short': [None, None, None, None, None]
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
                'BUY': [True, True, False, False, False],
                'SELL': [False, False, False, True, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [False, False, False, True, False],
                'Long': ['LongEntry', None, None, 'LongExit', None],
                'Short': [None, None, None, None, None]
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
                'BUY': [True, True, False, False, False],
                'SELL': [True, False, False, True, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, True, False, False, False],
                'SELL': [False, False, False, True, False],
                'Long': [None, 'LongEntry', None, 'LongExit', None],
                'Short': [None, None, None, None, None]
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
                'BUY': [False, True, False, True, False],
                'SELL': [False, False, False, True, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, True, False, False, False],
                'SELL': [False, False, False, True, False],
                'Long': [None, 'LongEntry', None, 'LongExit', None],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

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
                'SELL': [False, False, False, False, False],
                'Long': [None, None, None, None, None],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

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
                'SELL': [False, False, False, False, True],
                'Long': [None, None, None, 'LongEntry', 'LongExit'],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

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
                'SELL': [False, False, False, False, True],
                'Long': [None, None, 'LongEntry', None, 'LongExit'],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

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
                'SELL': [False, False, False, False, True],
                'Long': [None, None, 'LongEntry', None, 'LongExit'],
                'Short': [None, None, None, None, None]
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
                'BUY': [False, False, False, False, True],
                'SELL': [True, False, False, False, True]
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
                'SELL': [False, False, True, False, False],
                'Long': ['LongEntry', None, 'LongExit', None, None],
                'Short': [None, None, None, None, None]
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
                'BUY': [True, False, False, True, False],
                'SELL': [False, True, True, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, True, False],
                'SELL': [False, True, False, False, True],
                'Long': ['LongEntry', 'LongExit', None, 'LongEntry', 'LongExit'],
                'Short': [None, None, None, None, None]
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
                'BUY': [True, False, True, False, False],
                'SELL': [False, False, True, False, True]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [False, False, True, False, False],
                'Long': ['LongEntry', None, 'LongExit', None, None],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_buys_in_row(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, True, True],
                'SELL': [False, False, False, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [False, False, False, False, True],
                'Long': [None, None, 'LongEntry', None, 'LongExit'],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

if __name__ == '__main__':
    unittest.main()