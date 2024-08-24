import unittest
import pandas as pd
from trading_strategy_tester.conditions.stop_loss import StopLoss
from trading_strategy_tester.enums.stoploss_enum import StopLossType


class TestStopLoss(unittest.TestCase):

    def setUp(self):
        pass

    def test_normal_stop_loss_5_percent(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 54, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 54, 55, 47, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
        })

        # Act
        stop_loss.set_normal_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_normal_stop_loss_5_percent_trailing_sells(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 54, 47, 53, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, True],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 54, 47, 53, 51],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, True],
        })

        # Act
        stop_loss.set_normal_stop_loss(df)

        # Asset
        pd.testing.assert_frame_equal(df, df_expected)

    def test_normal_stop_loss_5_percent_sell_on_same_day_as_stop_loss(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 54, 47, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, True],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 54, 47, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, False, True, False, True],
        })

        # Act
        stop_loss.set_normal_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_normal_stop_loss_5_percent_without_stop_loss_activation(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 54, 50, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, True, False, False, True],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 54, 50, 53, 51],
            'BUY': [True, False, False, True, False],
            'SELL': [False, True, False, False, True],
        })

        # Act
        stop_loss.set_normal_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_normal_stop_loss_5_percent_with_more_buys(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 30, 50, 48, 45],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 30, 50, 48, 45],
            'BUY': [True, False, True, False, False],
            'SELL': [False, True, False, False, True],
        })

        # Act
        stop_loss.set_normal_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)


    def test_normal_stop_loss_5_percent_stop_loss_hit_on_buy_day(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 49, 43, 48, 26],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 49, 43, 48, 26],
            'BUY': [True, False, True, False, False],
            'SELL': [False, False, True, False, True],
        })

        # Act
        stop_loss.set_normal_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_trailing_stop_loss_5_percent_without_recalculating_threshold(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 49, 47, 48, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 49, 47, 48, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, True, False, False],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_trailing_stop_loss_5_percent_with_recalculating_threshold(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 60, 58, 57, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 60, 58, 57, 26],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, True, False],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

    def test_trailing_stop_loss_5_percent_with_recalculating_threshold_no_trade(self):
        # Arrange
        stop_loss = StopLoss(5)

        df = pd.DataFrame({
            'Close': [50, 60, 58, 57.5, 60],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        df_expected = pd.DataFrame({
            'Close': [50, 60, 58, 57.5, 60],
            'BUY': [True, False, False, False, False],
            'SELL': [False, False, False, False, False],
        })

        # Act
        stop_loss.set_trailing_stop_loss(df)

        # Assert
        pd.testing.assert_frame_equal(df, df_expected)

if __name__ == '__main__':
    unittest.main()