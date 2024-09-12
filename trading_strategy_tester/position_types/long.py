import pandas as pd

from trading_strategy_tester.position_types.position_type import PositionType


class Long(PositionType):
    """
    Class representing a long trading position strategy.

    This class provides methods to clean and update the 'BUY' and 'SELL' columns
    in a DataFrame to properly track entries and exits for long positions.
    """

    def clean_buy_sell_columns(self, df: pd.DataFrame):
        """
        Cleans the 'BUY' and 'SELL' columns in the provided DataFrame for long positions.

        This method ensures that the DataFrame reflects correct 'LongEntry' and 'LongExit' signals
        based on the 'BUY' and 'SELL' column values. If a 'BUY' signal is detected without a prior
        'SELL', it marks the entry as 'LongEntry'. Similarly, it marks the exit as 'LongExit'
        when a 'SELL' signal is detected after a 'BUY'. If there are unmatched 'BUY' signals at
        the end of the DataFrame, they are closed with a 'LongExit'.

        :param df: The DataFrame containing the 'BUY' and 'SELL' signals to be cleaned.
        :type df: pd.DataFrame
        :return: None. The DataFrame is modified in place.
        :rtype: None
        """
        # Initialize columns for position types
        df['Long'] = None
        df['Short'] = None

        # Track if a position has been bought
        bought = False

        # Iterate through each row to process the 'BUY' and 'SELL' signals
        for index, row in df.iterrows():
            # If no position is currently open and a 'BUY' signal is present without a 'SELL' signal
            if not bought and row['BUY'] and not row['SELL']:
                bought = True
                df.at[index, 'Long'] = 'LongEntry'  # Mark entry for a long position
            # If a position is currently open and a 'SELL' signal is present
            elif bought and row['SELL']:
                bought = False
                df.at[index, 'BUY'] = False  # Clear the 'BUY' signal
                df.at[index, 'Long'] = 'LongExit'  # Mark exit for the long position
            else:
                # Clear invalid or redundant 'BUY' and 'SELL' signals
                df.at[index, 'BUY'] = False
                df.at[index, 'SELL'] = False

        # Check for any open 'BUY' positions left at the end of the DataFrame
        if bought:
            if not df.loc[df.index[-1], 'BUY']:
                df.loc[df.index[-1], 'SELL'] = True  # Ensure there's a 'SELL' to close the position
                df.at[df.index[-1], 'Long'] = 'LongExit'
            else:
                # If the last entry is 'BUY', clear it as no exit was recorded
                df.loc[df.index[-1], 'BUY'] = False
                df.at[df.index[-1], 'Long'] = None
