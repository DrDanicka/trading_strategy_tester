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
                'SELL': [False, False, True, False, False]
            }
        )

        df_expected = pd.DataFrame(
            {
                'BUY': [True, False, False, False, True],
                'SELL': [False, False, True, False, False],
                'Long': ['LongEntry', None, 'LongExit', None, None],
                'Short': [None, None, 'ShortEntry', None, 'ShortExit']
            }
        )

        # Act
        self.long_short_position.clean_buy_sell_columns(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


if __name__ == '__main__':
    unittest.main()