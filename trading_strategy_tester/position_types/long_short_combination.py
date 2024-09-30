import pandas as pd
from trading_strategy_tester.position_types.position_type import PositionType


class LongShortCombination(PositionType):
    """
    Class representing a combined long and short trading position strategy.

    This class provides methods to clean and update the 'BUY' and 'SELL' columns
    in a DataFrame to properly track entries and exits for both long and short positions.
    """

    def clean_buy_sell_columns(self, df: pd.DataFrame):
        """
        Cleans the 'BUY' and 'SELL' columns in the provided DataFrame for combined long and short positions.

        This method ensures that the DataFrame correctly reflects both 'LongEntry' and 'LongExit' signals
        for long positions, and 'ShortEntry' and 'ShortExit' signals for short positions. If a 'BUY' signal
        is detected without a prior 'SELL', it marks the entry as 'LongEntry'. Similarly, if a 'SELL' signal
        is detected without a prior 'BUY', it marks the entry as 'ShortEntry'. The method handles transitions
        between long and short positions appropriately and closes any unmatched positions at the end of the
        DataFrame.

        :param df: The DataFrame containing the 'BUY' and 'SELL' signals to be cleaned.
        :type df: pd.DataFrame
        :return: None. The DataFrame is modified in place.
        :rtype: None
        """
        # Initialize columns for position types
        df['Long'] = None
        df['Short'] = None

        # Track if a position is bought or sold
        bought = False
        sold = False

        # Iterate through each row to process the 'BUY' and 'SELL' signals
        for index, row in df.iterrows():
            # If either a 'BUY' or 'SELL' signal is present
            if row['BUY'] or row['SELL']:
                # If no position is currently open (neither bought nor sold)
                if not bought and not sold:
                    # If it is a 'BUY' signal
                    if row['BUY'] and not row['SELL'] and not self._is_takeprofit_or_stoploss(row, False):
                        bought = True
                        df.at[index, 'Long'] = 'LongEntry'  # Mark entry for a long position
                    # If it is a 'SELL' signal
                    elif row['SELL'] and not row['BUY'] and not self._is_takeprofit_or_stoploss(row, True):
                        sold = True
                        df.at[index, 'Short'] = 'ShortEntry'  # Mark entry for a short position
                    else:
                        # Clear invalid or redundant 'BUY' and 'SELL' signals
                        df.at[index, 'BUY'] = False
                        df.at[index, 'SELL'] = False

                # If a long position is currently open
                elif bought:
                    # If there is a 'SELL' signal to exit the long position and enter a short position
                    if row['SELL'] and not row['BUY']:
                        bought = False
                        df.at[index, 'Long'] = 'LongExit'  # Mark exit for the long position

                        if not self._is_takeprofit_or_stoploss(row, True):
                            sold = True
                            df.at[index, 'Short'] = 'ShortEntry'  # Mark entry for a short position
                    else:
                        # Clear invalid or redundant 'BUY' and 'SELL' signals
                        df.at[index, 'BUY'] = False
                        df.at[index, 'SELL'] = False

                # If a short position is currently open
                elif sold:
                    # If there is a 'BUY' signal to exit the short position and enter a long position
                    if row['BUY'] and not row['SELL']:
                        sold = False
                        df.at[index, 'Short'] = 'ShortExit'  # Mark exit for the short position

                        if not self._is_takeprofit_or_stoploss(row, False):
                            bought = True
                            df.at[index, 'Long'] = 'LongEntry'  # Mark entry for a long position
                    else:
                        # Clear invalid or redundant 'BUY' and 'SELL' signals
                        df.at[index, 'BUY'] = False
                        df.at[index, 'SELL'] = False

        # Handle any remaining open positions at the end of the DataFrame
        if bought:
            # Ensure the position is closed with a 'SELL' if not already
            if not df.loc[df.index[-1], 'BUY']:
                df.loc[df.index[-1], 'SELL'] = True
                df.at[df.index[-1], 'Long'] = 'LongExit'
            else:
                # If the last entry is 'BUY', clear it as no exit was recorded
                df.at[df.index[-1], 'Long'] = None

        if sold:
            # Ensure the position is closed with a 'BUY' if not already
            if not df.loc[df.index[-1], 'SELL']:
                df.loc[df.index[-1], 'BUY'] = True
                df.loc[df.index[-1], 'Short'] = 'ShortExit'
            else:
                # If the last entry is 'SELL', clear it as no exit was recorded
                df.at[df.index[-1], 'Short'] = None

    def _is_takeprofit_or_stoploss(self, row, sell: bool = True) -> bool:
        """
        Checks if the given row contains a 'TakeProfit' or 'StopLoss' signal, based on whether it is a buy or sell signal.

        :param row: A row from a DataFrame, typically representing a single trading day or period.
                    The row is expected to contain columns 'SELL_Signals' and 'BUY_Signals' which indicate trading signals.
        :type row: pd.Series

        :param sell: A boolean flag to determine whether to check for a sell or buy signal.
                     - If True (default), it checks the 'SELL_Signals' column for 'TakeProfit' or 'StopLoss'.
                     - If False, it checks the 'BUY_Signals' column instead.
        :type sell: bool

        :return: True if the respective 'SELL_Signals' or 'BUY_Signals' column contains a signal that starts with
                 'TakeProfit' or 'StopLoss'. False otherwise.
        :rtype: bool
        """
        if sell:
            return row['SELL_Signals'] is not None and (
                        row['SELL_Signals'].startswith('TakeProfit') or row['SELL_Signals'].startswith('StopLoss'))
        else:
            return row['BUY_Signals'] is not None and (
                        row['BUY_Signals'].startswith('TakeProfit') or row['BUY_Signals'].startswith('StopLoss'))
