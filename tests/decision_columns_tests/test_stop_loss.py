import unittest
import pandas as pd
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.source_enum import SourceType


class TestStopLoss(unittest.TestCase):

    def setUp(self):
        pass

    def test_long_normal_stop_loss_5_percent_false_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 55, 47, 51],
            SourceType.HIGH.value: [50, 54, 55, 47, 51],
            SourceType.LOW.value: [50, 54, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 55, 47, 51],
            SourceType.HIGH.value: [50, 54, 55, 47, 51],
            SourceType.LOW.value: [50, 54, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, expected_signal, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_long_normal_stop_loss_5_percent_trailing_sells(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 47, 53, 51],
            SourceType.HIGH.value: [50, 54, 47, 53, 51],
            SourceType.LOW.value: [50, 54, 47, 53, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 47, 53, 51],
            SourceType.HIGH.value: [50, 54, 47, 53, 51],
            SourceType.LOW.value: [50, 54, 47, 53, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Asset
        pd.testing.assert_frame_equal(df, df_expected)

    def test_long_normal_stop_loss_5_percent_false_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 47, 53, 51],
            SourceType.HIGH.value: [50, 54, 47, 53, 51],
            SourceType.LOW.value: [50, 54, 47, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 47, 53, 51],
            SourceType.HIGH.value: [50, 54, 47, 53, 51],
            SourceType.LOW.value: [50, 54, 47, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_long_normal_stop_loss_5_percent_without_stop_loss_activation(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 50, 53, 51],
            SourceType.HIGH.value: [50, 54, 50, 53, 51],
            SourceType.LOW.value: [50, 54, 50, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, True, False, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 54, 50, 53, 51],
            SourceType.HIGH.value: [50, 54, 50, 53, 51],
            SourceType.LOW.value: [50, 54, 50, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, True, False, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_long_normal_stop_loss_5_percent_with_more_buys(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 30, 50, 48, 45],
            SourceType.HIGH.value: [50, 30, 50, 48, 45],
            SourceType.LOW.value: [50, 30, 50, 48, 45],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 30, 50, 48, 45],
            SourceType.HIGH.value: [50, 30, 50, 48, 45],
            SourceType.LOW.value: [50, 30, 50, 48, 45],
            'BUY': [True, False, True, False, False],
            'SELL': [False, True, False, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, expected_signal, None, None, expected_signal],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_normal_stop_loss_5_percent_true_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 43, 48, 26],
            SourceType.HIGH.value: [50, 49, 43, 48, 26],
            SourceType.LOW.value: [50, 49, 43, 48, 26],
            'BUY': [True, False, True, True, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 43, 48, 26],
            SourceType.HIGH.value: [50, 49, 43, 48, 26],
            SourceType.LOW.value: [50, 49, 43, 48, 26],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, expected_signal],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_normal_stop_loss_5_percent_true_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 43, 48, 26],
            SourceType.HIGH.value: [50, 49, 43, 48, 26],
            SourceType.LOW.value: [50, 49, 43, 48, 26],
            'BUY': [True, False, True, True, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 43, 48, 26],
            SourceType.HIGH.value: [50, 49, 43, 48, 26],
            SourceType.LOW.value: [50, 49, 43, 48, 26],
            'BUY': [True, False, True, True, False],
            'SELL': [False, False, True, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, expected_signal],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_normal_stop_loss_5_percent_false_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, expected_signal, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_normal_stop_loss_5_percent_true_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_short_normal_stop_loss_5_percent_false_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, expected_signal, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_normal_stop_loss_5_percent_true_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 54, 48, 26],
            SourceType.HIGH.value: [50, 49, 54, 48, 26],
            SourceType.LOW.value: [50, 49, 54, 48, 26],
            'BUY': [False, False, True, False, False],
            'SELL': [True, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_normal_stop_loss_5_percent_false_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_normal_stop_loss_5_percent_true_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_normal_stop_loss_5_percent_false_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, expected_signal, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_normal_stop_loss_5_percent_true_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossNormal({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 49, 45, 48, 60],
            SourceType.HIGH.value: [50, 49, 45, 48, 60],
            SourceType.LOW.value: [50, 49, 45, 48, 60],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, None],
        })

        # Act
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_trailing_stop_loss_5_percent_false_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 60, 58, 58.5, 26],
            SourceType.HIGH.value: [50, 60, 58, 58.5, 26],
            SourceType.LOW.value: [50, 60, 58, 58.5, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 60, 58, 58.5, 26],
            SourceType.HIGH.value: [50, 60, 58, 58.5, 26],
            SourceType.LOW.value: [50, 60, 58, 58.5, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, True],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, expected_signal],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_long_trailing_stop_loss_5_percent_true_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 96, 90, 26],
            SourceType.HIGH.value: [50, 100, 96, 90, 26],
            SourceType.LOW.value: [50, 100, 96, 90, 26],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 96, 90, 26],
            SourceType.HIGH.value: [50, 100, 96, 90, 26],
            SourceType.LOW.value: [50, 100, 96, 90, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, expected_signal, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_trailing_stop_loss_5_percent_false_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 96, 90, 26],
            SourceType.HIGH.value: [50, 100, 96, 90, 26],
            SourceType.LOW.value: [50, 100, 96, 90, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 96, 90, 26],
            SourceType.HIGH.value: [50, 100, 96, 90, 26],
            SourceType.LOW.value: [50, 100, 96, 90, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_trailing_stop_loss_5_percent_true_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 96, 90, 26],
            SourceType.HIGH.value: [50, 100, 96, 90, 26],
            SourceType.LOW.value: [50, 100, 96, 90, 26],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 96, 90, 26],
            SourceType.HIGH.value: [50, 100, 96, 90, 26],
            SourceType.LOW.value: [50, 100, 96, 90, 26],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_trailing_stop_loss_5_percent_false_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, expected_signal, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_trailing_stop_loss_5_percent_true_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_trailing_stop_loss_5_percent_false_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, expected_signal, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_trailing_stop_loss_5_percent_true_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.SHORT
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_trailing_stop_loss_5_percent_false_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, False, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [100, 50, 51, 53, 26],
            SourceType.HIGH.value: [100, 50, 51, 53, 26],
            SourceType.LOW.value: [100, 50, 51, 53, 26],
            'BUY': [False, False, False, True, False],
            'SELL': [True, False, False, False, False],
            'BUY_Signals': [None, None, None, expected_signal, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_long_short_combination_trailing_stop_loss_5_percent_true_false(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 97, 93, 26],
            SourceType.HIGH.value: [50, 100, 97, 93, 26],
            SourceType.LOW.value: [50, 100, 97, 93, 26],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, False, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 97, 93, 26],
            SourceType.HIGH.value: [50, 100, 97, 93, 26],
            SourceType.LOW.value: [50, 100, 97, 93, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, expected_signal, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_trailing_stop_loss_5_percent_false_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 93, 100, 26],
            SourceType.HIGH.value: [50, 100, 93, 100, 26],
            SourceType.LOW.value: [50, 100, 93, 100, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 93, 100, 26],
            SourceType.HIGH.value: [50, 100, 93, 100, 26],
            SourceType.LOW.value: [50, 100, 93, 100, 26],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, expected_signal, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_long_short_combination_trailing_stop_loss_5_percent_true_true(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
        position_type = PositionTypeEnum.LONG_SHORT_COMBINED
        expected_signal = f'StopLossTrailing({percent})'

        df = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 93, 100, 26],
            SourceType.HIGH.value: [50, 100, 93, 100, 26],
            SourceType.LOW.value: [50, 100, 93, 100, 26],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, None, None, None],
        })

        df_expected = pd.DataFrame({
            SourceType.OPEN.value: [50, 100, 93, 100, 26],
            SourceType.HIGH.value: [50, 100, 93, 100, 26],
            SourceType.LOW.value: [50, 100, 93, 100, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
            'BUY_Signals': [None, None, None, None, None],
            'SELL_Signals': [None, None, expected_signal, None, None],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_and_then_buy_normal(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
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
        stop_loss.set_normal_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_short_and_then_buy_trailing(self):
        # Arrange
        percent = 5
        stop_loss = StopLoss(percent)
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
        stop_loss.set_trailing_stop_loss(df, position_type)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

if __name__ == '__main__':
    unittest.main()