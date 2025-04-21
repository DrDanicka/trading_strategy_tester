import pandas as pd

from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.source_enum import SourceType


class TakeProfit:
    """
    Implements a take-profit strategy for trading data.

    This class monitors the price increase from the buying price or decrease from the selling price
    and applies a 'SELL' or 'BUY' signal when the price exceeds the specified take-profit percentage threshold.
    """

    def __init__(self, percentage: float):
        """
        Initializes the TakeProfit class with the take-profit percentage.

        :param percentage: The percentage threshold for the take-profit. For instance,
                           if set to 10, a 'SELL' signal is triggered when the price increases
                           by 10% from the buying price, or a 'BUY' signal is triggered
                           when the price decreases by 10% from the selling price.
        :type percentage: float
        """
        self.percentage = percentage

    def set_take_profit(self, df: pd.DataFrame, position_type: PositionTypeEnum):
        """
        Applies the take-profit strategy by adjusting 'SELL' and 'BUY' signals based on the current price.

        The function iterates over the DataFrame, and when the current price rises (or falls) to or beyond
        the calculated take-profit threshold, it sets 'SELL' or 'BUY' signals accordingly.

        :param df: A DataFrame containing columns 'BUY' and 'SELL' signals to be modified.
        :type df: pd.DataFrame
        :param position_type: Indicates whether the strategy supports LONG, SHORT, or LONG_SHORT_COMBINED positions.
        :type position_type: PositionTypeEnum
        """

        # Initialize tracking variables for buy/sell state
        bought = False
        sold = False
        buying_price = 0
        selling_price = 0
        value_threshold = 0  # How much the trade can rise or fall before reaching the take-profit

        # Determine whether the strategy supports long, short, or both
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

            # Handle LONG positions: Trigger 'SELL' when take-profit is reached
            if has_long and not bought and not sold and row['BUY'] and not row['SELL']:
                buying_price = current_open
                value_threshold = (buying_price * self.percentage) / 100
                bought = True
                continue

            # Handle SHORT positions: Trigger 'BUY' when take-profit is reached
            elif has_short and not bought and not sold and row['SELL'] and not row['BUY']:
                selling_price = current_open
                value_threshold = (selling_price * self.percentage) / 100
                sold = True
                continue

            # Check if the take-profit threshold is reached for LONG positions
            if has_long and bought and current_high >= buying_price + value_threshold:
                df.at[index, 'SELL'] = True
                df.at[index, 'BUY'] = False  # Prioritize Selling
                df.at[index, 'SELL_Signals'] = f'TakeProfit({self.percentage})'
                bought = False

            # Check if the take-profit threshold is reached for SHORT positions
            if has_short and sold and current_low <= selling_price - value_threshold:
                df.at[index, 'BUY'] = True
                df.at[index, 'SELL'] = False  # Prioritize Buying
                df.at[index, 'BUY_Signals'] = f'TakeProfit({self.percentage})'
                sold = False

    def to_dict(self):
        """
        Converts the TakeProfit instance to a dictionary representation.

        :return: A dictionary containing the take-profit percentage.
        :rtype: dict
        """
        return {
            'percentage': self.percentage
        }