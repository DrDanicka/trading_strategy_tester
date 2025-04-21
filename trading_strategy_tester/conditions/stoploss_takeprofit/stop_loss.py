import pandas as pd

from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.enums.stoploss_enum import StopLossType


class StopLoss:
    """
    A class to apply stop-loss strategies (normal or trailing) to trading data.

    The StopLoss class implements different stop-loss strategies to manage risk in trading by setting
    thresholds at which the system automatically triggers sell or buy signals.
    """

    def __init__(self, percentage: float, stop_loss_type: StopLossType = StopLossType.NORMAL):
        """
        Initializes the StopLoss strategy with a percentage and stop-loss type.

        :param percentage: The percentage threshold to trigger the stop-loss. For example, a 10% stop-loss means
                           the system will trigger a sell if the price falls by 10% from the buying price (or rises for short positions).
        :type percentage: float
        :param stop_loss_type: The type of stop-loss to apply (NORMAL or TRAILING). Defaults to StopLossType.NORMAL.
        :type stop_loss_type: StopLossType
        """
        self.percentage = percentage
        self.stop_loss_type = stop_loss_type

    def set_normal_stop_loss(self, df: pd.DataFrame, position_type: PositionTypeEnum):
        """
        Applies a normal stop-loss strategy to the DataFrame.

        This method iterates through the DataFrame and checks if the price reaches a stop-loss threshold
        for both long and short positions, triggering the appropriate sell or buy signals.

        :param df: The DataFrame containing the trading data, with 'BUY' and 'SELL' signals to be modified
                   based on the stop-loss strategy.
        :type df: pd.DataFrame
        :param position_type: Indicates whether the strategy supports LONG, SHORT, or LONG_SHORT_COMBINED positions.
        :type position_type: PositionTypeEnum
        """

        bought = False
        sold = False
        buying_price = 0
        selling_price = 0
        value_threshold = 0  # How much the trade can rise or fall before reaching the stop-loss

        has_long = position_type == PositionTypeEnum.LONG or position_type == PositionTypeEnum.LONG_SHORT_COMBINED
        has_short = position_type == PositionTypeEnum.SHORT or position_type == PositionTypeEnum.LONG_SHORT_COMBINED

        for index, row in df.iterrows():
            current_open = row[SourceType.OPEN.value]
            current_low = row[SourceType.LOW.value]
            current_high = row[SourceType.HIGH.value]

            # Reset bought/sold flags if opposing signals occur (e.g., SELL after BUY)
            if bought and row['SELL']:
                if position_type == PositionTypeEnum.LONG_SHORT_COMBINED:
                    if not row['BUY']:
                        bought = False
                        sold = False
                else:
                    bought = False
                    continue

            elif sold and row['BUY']:
                if position_type == PositionTypeEnum.LONG_SHORT_COMBINED:
                    if not row['SELL']:
                        sold = False
                        bought = False
                else:
                    sold = False
                    continue

            # Handle LONG positions: Trigger 'SELL' when stop-loss is reached
            if has_long and not bought and not sold and row['BUY'] and not row['SELL']:
                buying_price = current_open
                value_threshold = (buying_price * self.percentage) / 100
                bought = True
                continue

            # Handle SHORT positions: Trigger 'BUY' when stop-loss is reached
            elif has_short and not bought and not sold and row['SELL'] and not row['BUY']:
                selling_price = current_open
                value_threshold = (selling_price * self.percentage) / 100
                sold = True
                continue

            # Check if the stop-loss threshold is reached for LONG positions
            if has_long and bought and current_low <= buying_price - value_threshold:
                df.at[index, 'SELL'] = True
                df.at[index, 'BUY'] = False  # Prioritize Selling
                df.at[index, 'SELL_Signals'] = f'StopLossNormal({self.percentage})'
                bought = False

            # Check if the stop-loss threshold is reached for SHORT positions
            if has_short and sold and current_high >= selling_price + value_threshold:
                df.at[index, 'BUY'] = True
                df.at[index, 'SELL'] = False  # Prioritize Buying
                df.at[index, 'BUY_Signals'] = f'StopLossNormal({self.percentage})'
                sold = False

    def set_trailing_stop_loss(self, df: pd.DataFrame, position_type: PositionTypeEnum):
        """
        Applies a trailing stop-loss strategy to the DataFrame.

        This method updates the stop-loss threshold as the price moves favorably, allowing the stop-loss level
        to "trail" the price upwards (for long positions) or downwards (for short positions), locking in gains.

        :param df: The DataFrame containing the trading data, with 'BUY' and 'SELL' signals to be modified
                   based on the stop-loss strategy.
        :type df: pd.DataFrame
        :param position_type: Indicates whether the strategy supports LONG, SHORT, or LONG_SHORT_COMBINED positions.
        :type position_type: PositionTypeEnum
        """
        bought = False
        sold = False
        buying_price = 0
        selling_price = 0
        value_threshold = 0  # How much the trade can rise or fall before reaching the stop-loss

        has_long = position_type == PositionTypeEnum.LONG or position_type == PositionTypeEnum.LONG_SHORT_COMBINED
        has_short = position_type == PositionTypeEnum.SHORT or position_type == PositionTypeEnum.LONG_SHORT_COMBINED

        for index, row in df.iterrows():
            current_open = row[SourceType.OPEN.value]
            current_low = row[SourceType.LOW.value]
            current_high = row[SourceType.HIGH.value]

            # Update buying and selling prices for trailing stop-loss
            if bought and current_open > buying_price:
                buying_price = current_open
                value_threshold = (buying_price * self.percentage) / 100

            if sold and current_open < selling_price:
                selling_price = current_open
                value_threshold = (selling_price * self.percentage) / 100

            # Reset bought/sold flags if opposing signals occur (e.g., SELL after BUY)
            if bought and row['SELL']:
                if position_type == PositionTypeEnum.LONG_SHORT_COMBINED:
                    if not row['BUY']:
                        bought = False
                        sold = False
                else:
                    bought = False
                    continue

            elif sold and row['BUY']:
                if position_type == PositionTypeEnum.LONG_SHORT_COMBINED:
                    if not row['SELL']:
                        sold = False
                        bought = False
                else:
                    sold = False
                    continue

            # Handle LONG positions: Trigger 'SELL' when stop-loss is reached
            if has_long and not bought and not sold and row['BUY'] and not row['SELL']:
                buying_price = current_open
                value_threshold = (buying_price * self.percentage) / 100
                bought = True
                continue

            # Handle SHORT positions: Trigger 'BUY' when stop-loss is reached
            elif has_short and not bought and not sold and row['SELL'] and not row['BUY']:
                selling_price = current_open
                value_threshold = (selling_price * self.percentage) / 100
                sold = True
                continue

            # Check if the stop-loss threshold is reached for LONG positions
            if has_long and bought and current_low <= buying_price - value_threshold:
                df.at[index, 'SELL'] = True
                df.at[index, 'BUY'] = False  # Prioritize Selling
                df.at[index, 'SELL_Signals'] = f'StopLossTrailing({self.percentage})'
                bought = False

            # Check if the stop-loss threshold is reached for SHORT positions
            if has_short and sold and current_high >= selling_price + value_threshold:
                df.at[index, 'BUY'] = True
                df.at[index, 'SELL'] = False  # Prioritize Buying
                df.at[index, 'BUY_Signals'] = f'StopLossTrailing({self.percentage})'
                sold = False

    def set_stop_loss(self, df: pd.DataFrame, position_type: PositionTypeEnum):
        """
        Applies the appropriate stop-loss strategy to the DataFrame based on the selected stop-loss type.

        This method checks the stop-loss type and applies the corresponding stop-loss strategy
        (either 'NORMAL' or 'TRAILING') to adjust the 'SELL' signals in the DataFrame.

        :param df: A DataFrame containing columns 'Close', 'BUY', and 'SELL'.
                   'Close' represents the closing price of the asset.
                   'BUY' indicates where buying actions occurred.
                   'SELL' will be modified by the selected stop-loss method to indicate where sell actions should occur.
        :type df: pd.DataFrame
        :param position_type: Specifies whether to use a LONG, SHORT, or LONG_SHORT_COMBINED strategy.
        :type position_type: PositionTypeEnum

        :return: None. The DataFrame is modified in place.
        """
        if self.stop_loss_type == StopLossType.NORMAL:
            self.set_normal_stop_loss(df, position_type)
        elif self.stop_loss_type == StopLossType.TRAILING:
            self.set_trailing_stop_loss(df, position_type)

    def to_dict(self):
        """
        Converts the StopLoss object to a dictionary representation.

        :return: A dictionary containing the stop-loss percentage and type.
        :rtype: dict
        """
        return {
            'percentage': self.percentage,
            'stop_loss_type': self.stop_loss_type
        }
