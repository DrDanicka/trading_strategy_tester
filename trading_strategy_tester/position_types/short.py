import pandas as pd
from trading_strategy_tester.position_types.position_type import PositionType


class Short(PositionType):
    """
    Class representing a short trading position strategy.

    This class provides methods to clean and update the 'BUY' and 'SELL' columns
    in a DataFrame to properly track entries and exits for short positions.
    """

    def clean_buy_sell_columns(self, df: pd.DataFrame):
        """
        Cleans the 'BUY' and 'SELL' columns in the provided DataFrame for short positions.

        This method ensures that the DataFrame reflects correct 'ShortEntry' and 'ShortExit' signals
        based on the 'BUY' and 'SELL' column values. If a 'SELL' signal is detected without a prior
        'BUY', it marks the entry as 'ShortEntry'. Similarly, it marks the exit as 'ShortExit'
        when a 'BUY' signal is detected after a 'SELL'. If there are unmatched 'SELL' signals at
        the end of the DataFrame, they are closed with a 'ShortExit'.

        :param df: The DataFrame containing the 'BUY' and 'SELL' signals to be cleaned.
        :type df: pd.DataFrame
        :return: None. The DataFrame is modified in place.
        :rtype: None
        """
        # Initialize columns for position types
        df['Long'] = None
        df['Short'] = None

        # Track if a position has been sold
        sold = False

        # Iterate through each row to process the 'SELL' and 'BUY' signals
        for index, row in df.iterrows():
            # If no position is currently open and a 'SELL' signal is present without a 'BUY' signal
            if not sold and row['SELL'] and not row['BUY']:
                sold = True
                df.at[index, 'Short'] = 'ShortEntry'  # Mark entry for a short position
            # If a position is currently open and a 'BUY' signal is present
            elif sold and row['BUY']:
                sold = False
                df.at[index, 'SELL'] = False  # Clear the 'SELL' signal
                df.at[index, 'Short'] = 'ShortExit'  # Mark exit for the short position
            else:
                # Clear invalid or redundant 'BUY' and 'SELL' signals
                df.at[index, 'BUY'] = False
                df.at[index, 'SELL'] = False

        # Check for any open 'SELL' positions left at the end of the DataFrame
        if sold:
            if not df.loc[df.index[-1], 'SELL']:
                df.loc[df.index[-1], 'BUY'] = True  # Ensure there's a 'BUY' to close the position
                df.loc[df.index[-1], 'Short'] = 'ShortExit'
            else:
                # If the last entry is 'SELL', clear it as no exit was recorded
                df.loc[df.index[-1], 'SELL'] = False
                df.at[df.index[-1], 'Short'] = None
