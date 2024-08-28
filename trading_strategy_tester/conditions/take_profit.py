import pandas as pd

class TakeProfit:
    """
    A class to apply a take-profit strategy to trading data.

    The TakeProfit class allows for the implementation of a take-profit strategy based on a specified percentage.
    It monitors the price increase from the buying price and sets a 'SELL' signal when the price exceeds the take-profit threshold.
    """

    def __init__(self, percentage: float):
        """
        Initializes the take-profit strategy with the specified percentage.

        Parameters:
        -----------
        percentage : float
            The percentage used to determine the take-profit threshold.
            For example, if set to 10, a 'SELL' signal will be triggered when the price increases by 10% from the buying price.
        """
        self.percentage = percentage

    def set_take_profit(self, df: pd.DataFrame):
        """
        Adjusts the 'SELL' signals in the DataFrame based on the take-profit strategy.

        This method iterates over the DataFrame and sets 'SELL' signals when the current price
        rises to or above a calculated take-profit threshold. The threshold is determined as a 
        percentage increase from the buying price.

        Parameters:
        -----------
        df : pd.DataFrame
            A DataFrame containing columns 'Close', 'BUY', and 'SELL'.
            'Close' represents the closing price of the asset.
            'BUY' indicates where buying actions occurred.
            'SELL' will be modified by this function to indicate where take-profit sell actions should occur.

        Returns:
        --------
        None
            The DataFrame is modified in place.
        """

        bought = False
        buying_price = 0
        # This represents how much can the trade go down until it hits percentage stop-loos
        value_threshold = 0

        for index, row in df.iterrows():
            current_price = row['Close']

            if bought and current_price >= buying_price + value_threshold:
                df.at[index, 'SELL'] = True
                df.at[index, 'SELL_Signals'] = f'TakeProfit({self.percentage})'
                bought = False

            if row['BUY']:
                buying_price = current_price
                value_threshold = (buying_price * self.percentage) / 100
                bought = True
