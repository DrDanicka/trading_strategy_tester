import pandas as pd

from trading_strategy_tester.enums.stoploss_enum import StopLossType


class StopLoss():
    def __init__(self, percentage: float, stop_loss_type: StopLossType = StopLossType.NORMAL):
        """
        Initializes the stop-loss with the specified parameters.

        Parameters:
        -----------
        percentage : float
            The percentage used to determine the stop-loss threshold.
            For example, if set to 5, the stop-loss will trigger if the price drops 5% below the buying price.

        stop_loss_type : StopLossType, optional
            Specifies the type of stop-loss strategy to be applied.
            By default, it is set to StopLossType.NORMAL. This could be an enumeration or class
            defining different stop-loss strategies (e.g., NORMAL, TRAILING).

        Attributes:
        -----------
        self.percentage : float
            Stores the stop-loss percentage to be used in the strategy.

        self.stop_loss_type : StopLossType
            Stores the type of stop-loss strategy to be applied.
        """
        self.percentage = percentage
        self.stop_loss_type = stop_loss_type

    def set_normal_stop_loss(self, df: pd.DataFrame):
        """
        Adjusts the 'SELL' signals in the DataFrame based on a stop-loss strategy.

        This method iterates over the provided DataFrame and sets the 'SELL' signals
        based on a calculated stop-loss threshold. The stop-loss is determined as a percentage
        of the buying price. If the current price falls below the threshold, a 'SELL' signal is set.
        Additionally, it handles cases where multiple 'SELL' signals occur in a row by deleting
        the next 'SELL' signal after the stop-loss is triggered.

        Parameters:
        -----------
        df : pd.DataFrame
            A DataFrame containing columns 'Close', 'BUY', and 'SELL'.
            'Close' represents the closing price of the asset.
            'BUY' indicates where buying actions occurred.
            'SELL' will be modified by this function to indicate where sell actions should occur.

        Returns:
        --------
        None
            The DataFrame is modified in place.
        """

        bought = False
        delete_next_sell = False
        buying_price = 0
        # This represents how much many can the trade go down until it hits percentage stop-loos
        value_threshold = 0

        for index, row in df.iterrows():
            current_price = row['Close']

            if bought:
                if row['SELL']:
                    if delete_next_sell:
                        df.at[index, 'SELL'] = False
                        delete_next_sell = False
                    bought = False
                else:
                    if current_price <= buying_price - value_threshold:
                        df.at[index, 'SELL'] = True
                        delete_next_sell = True
            else:
                if row['BUY']:
                    bought = True
                    buying_price = row['Close']
                    value_threshold = (buying_price * self.percentage) / 100


    #def set_trailing_stop_loss(self, df: pd.DataFrame):
