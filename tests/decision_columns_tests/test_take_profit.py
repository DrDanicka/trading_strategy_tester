import unittest
import pandas as pd

from trading_strategy_tester.conditions.stoploss_takeprofit.take_profit import TakeProfit
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.source_enum import SourceType


class TestTakeProfit(unittest.TestCase):

    def setUp(self):
        pass

    def test_long_take_profit_5_percent(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.HIGH.value: [50, 54, 55, 47, 51],
            SourceType.OPEN.value: [50, 52, 55, 47, 51],
            SourceType.LOW.value: [50, 52, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.HIGH.value: [50, 54, 55, 47, 51],
            SourceType.OPEN.value: [50, 52, 55, 47, 51],
            SourceType.LOW.value: [50, 52, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, True, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, expected_signal, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_take_profit_5_percent_with_no_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 49, 47, 51],
            SourceType.HIGH.value: [50, 52, 49, 47, 51],
            SourceType.LOW.value: [50, 52, 49, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 49, 47, 51],
            SourceType.HIGH.value: [50, 52, 49, 47, 51],
            SourceType.LOW.value: [50, 52, 49, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_take_profit_5_percent_sell_on_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 55, 47, 51],
            SourceType.HIGH.value: [50, 52, 55, 47, 51],
            SourceType.LOW.value: [50, 52, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 55, 47, 51],
            SourceType.HIGH.value: [50, 52, 55, 47, 51],
            SourceType.LOW.value: [50, 52, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_take_profit_5_percent_buy_on_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 55, 47, 51],
            SourceType.HIGH.value: [50, 52, 55, 47, 51],
            SourceType.LOW.value: [50, 52, 55, 47, 51],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 55, 47, 51],
            SourceType.HIGH.value: [50, 52, 55, 47, 51],
            SourceType.LOW.value: [50, 52, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_take_profit_5_percent_multiple_trades(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 55, 60, 51],
            SourceType.HIGH.value: [50, 52, 55, 60, 51],
            SourceType.LOW.value: [50, 52, 55, 60, 51],
            'BUY': [True, False, True, False, False],
            'SELL': [False, True, False, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 55, 60, 51],
            SourceType.HIGH.value: [50, 52, 55, 60, 51],
            SourceType.LOW.value: [50, 52, 55, 60, 51],
            'BUY': [True, False, True, False, False],
            'SELL': [False, True, False, True, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, expected_signal, None],
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_take_profit_5_percent(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 48, 45, 51],
            SourceType.HIGH.value: [50, 48, 48, 45, 51],
            SourceType.LOW.value: [50, 48, 48, 45, 51],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 48, 45, 51],
            SourceType.HIGH.value: [50, 48, 48, 45, 51],
            SourceType.LOW.value: [50, 48, 48, 45, 51],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, expected_signal, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_take_profit_5_percent_with_no_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 48, 49, 51],
            SourceType.HIGH.value: [50, 48, 48, 49, 51],
            SourceType.LOW.value: [50, 48, 48, 49, 51],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 48, 49, 51],
            SourceType.HIGH.value: [50, 48, 48, 49, 51],
            SourceType.LOW.value: [50, 48, 48, 49, 51],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_take_profit_5_percent_sell_on_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 47, 49, 51],
            SourceType.HIGH.value: [50, 48, 47, 49, 51],
            SourceType.LOW.value: [50, 48, 47, 49, 51],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 47, 49, 51],
            SourceType.HIGH.value: [50, 48, 47, 49, 51],
            SourceType.LOW.value: [50, 48, 47, 49, 51],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, expected_signal, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_take_profit_5_percent_buy_on_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 47, 49, 51],
            SourceType.HIGH.value: [50, 48, 47, 49, 51],
            SourceType.LOW.value: [50, 48, 47, 49, 51],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 47, 49, 51],
            SourceType.HIGH.value: [50, 48, 47, 49, 51],
            SourceType.LOW.value: [50, 48, 47, 49, 51],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_take_profit_5_percent_multiple_trades(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 47, 49, 44],
            SourceType.HIGH.value: [50, 48, 47, 49, 44],
            SourceType.LOW.value: [50, 48, 47, 49, 44],
            'BUY': [False, False, False, False, True],
            'SELL': [True, True, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 48, 47, 49, 44],
            SourceType.HIGH.value: [50, 48, 47, 49, 44],
            SourceType.LOW.value: [50, 48, 47, 49, 44],
            'BUY': [False, False, True, False, True],
            'SELL': [True, True, False, True, False],
            'BUY_Signals': [None, None, expected_signal, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_take_profit_5_percent_one_buy(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_take_profit_5_percent_one_sell(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 47, 49, 44],
            SourceType.HIGH.value: [50, 52, 47, 49, 44],
            SourceType.LOW.value: [50, 52, 47, 49, 44],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 47, 49, 44],
            SourceType.HIGH.value: [50, 52, 47, 49, 44],
            SourceType.LOW.value: [50, 52, 47, 49, 44],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, expected_signal, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_take_profit_5_percent_buy_sell_combination(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, False, True],
            'SELL': [False, False, True, True, False],
            'BUY_Signals': [None, None, None, None, expected_signal],
            'SELL_Signals': [None, None, expected_signal, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_take_profit_5_percent_sell_at_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, expected_signal, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_take_profit_5_percent_buy_sell_at_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, True, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, False, True],
            'SELL': [False, False, True, True, False],
            'BUY_Signals': [None, None, None, None, expected_signal],
            'SELL_Signals': [None, None, expected_signal, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_take_profit_5_percent_false_buy_sell_at_take_profit(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'TakeProfit({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None]
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 52, 53, 49, 44],
            SourceType.HIGH.value: [50, 52, 53, 49, 44],
            SourceType.LOW.value: [50, 52, 53, 49, 44],
            'BUY': [True, False, False, False, True],
            'SELL': [False, False, True, True, False],
            'BUY_Signals': [None, None, None, None, expected_signal],
            'SELL_Signals': [None, None, expected_signal, None, None]
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_and_then_but(self):
        # Arrange
        percent = 5
        take_profit = TakeProfit(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED

        df = pd.DataFrame({
            SourceType.OPEN.value: [100, 100, 100, 100, 100],
            SourceType.HIGH.value: [100, 100, 100, 100, 100],
            SourceType.LOW.value: [100, 100, 100, 100, 100],
            'BUY': [False, False, True, False, False],
            'SELL': [False, True, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [100, 100, 100, 100, 100],
            SourceType.HIGH.value: [100, 100, 100, 100, 100],
            SourceType.LOW.value: [100, 100, 100, 100, 100],
            'BUY': [False, False, True, False, False],
            'SELL': [False, True, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        take_profit.set_take_profit(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

if __name__ == '__main__':
    unittest.main()