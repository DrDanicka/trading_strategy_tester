import unittest
import pandas as pd

from trading_strategy_tester.position_types.long_short_combination import LongShortCombination


class TestCleaningDataLongShortCombination(unittest.TestCase):

    def setUp(self):
        self.long_short_position = LongShortCombination()

    def test_multiple_buy_sell(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [False, False, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': ['LongEntry', None, 'LongExit', None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_buy_sell_at_the_same_day_in_the_beginning(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [True, False, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': [None, None, None, None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_buy_sell_at_the_same_day_when_bought(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, True, False, False, False],
                'SELL': [False, True, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': ['LongEntry', None, 'LongExit', None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_buy_sell_at_the_same_day_when_sold(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, True, False],
                'SELL': [False, False, True, True, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': ['LongEntry', None, 'LongExit', None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_buy_sell_at_the_same_day_when_sold_in_the_end(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, True],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': ['LongEntry', None, 'LongExit', None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_buy_sell_at_the_same_day_when_bought_in_the_end(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, False, False, True],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, False],
                'SELL': [False, False, False, False, True],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': ['LongEntry', None, None, None, 'LongExit'],
                'Short': [None, None, None, None, None]
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_multiple_sell_buy(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [True, False, False, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [True, False, False, False, True],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': [None, None, 'LongEntry', None, 'LongExit'],
                'Short': ['ShortEntry', None, 'ShortExit', None, None]
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_duplicate_buys(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, True, False],
                'SELL': [True, False, False, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [True, False, False, False, True],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': [None, None, 'LongEntry', None, 'LongExit'],
                'Short': ['ShortEntry', None, 'ShortExit', None, None]
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_duplicate_sells(self):
        # Arrange
        df = pd.DataFrame(
            {
                'BUY': [False, False, True, True, False],
                'SELL': [True, True, False, False, False],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [False, False, True, False, False],
                'SELL': [True, False, False, False, True],
                'BUY_Signals': [None, None, None, None, None],
                'SELL_Signals': [None, None, None, None, None],
                'Long': [None, None, 'LongEntry', None, 'LongExit'],
                'Short': ['ShortEntry', None, 'ShortExit', None, None]
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

if __name__ == '__main__':
    unittest.main()