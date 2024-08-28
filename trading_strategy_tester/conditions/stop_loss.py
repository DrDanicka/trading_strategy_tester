import pandas as pd

from trading_strategy_tester.enums.stoploss_enum import StopLossType


class StopLoss():
    def __init__(self, percentage: float, stop_loss_type: StopLossType = StopLossType.NORMAL, ):
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

        This method iterates over the DataFrame and sets 'SELL' signals based on a calculated
        stop-loss threshold. The stop-loss is determined as a percentage of the buying price.
        When a 'BUY' signal is encountered, the buying price is recorded, and the stop-loss
        threshold is calculated. If the current price drops below the threshold, a 'SELL' signal
        is set, and the trade is considered closed.

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
        buying_price = 0
        # This represents how much can the trade go down until it hits percentage stop-loos
        value_threshold = 0

        for index, row in df.iterrows():
            current_price = row['Close']

            if bought and current_price <= buying_price - value_threshold:
                df.at[index, 'SELL'] = True
                df.at[index, 'SELL_Signals'] = f'StopLossNormal({self.percentage})'
                bought = False

            if row['BUY']:
                buying_price = current_price
                value_threshold = (buying_price * self.percentage) / 100
                bought = True


    def set_trailing_stop_loss(self, df: pd.DataFrame):
        bought = False
        buying_price = 0
        # This represents how much can the trade go down until it hits percentage stop-loos
        value_threshold = 0

        for index, row in df.iterrows():
            current_price = row['Close']

            if bought:
                if current_price > buying_price:
                    buying_price = current_price
                    value_threshold = (buying_price * self.percentage) / 100
                if current_price <= buying_price - value_threshold:
                    df.at[index, 'SELL'] = True
                    df.at[index, 'SELL_Signals'] = f'StopLossTrailing({self.percentage})'
                    bought = False

            if row['BUY']:
                buying_price = current_price
                value_threshold = (buying_price * self.percentage) / 100
                bought = True



    def set_stop_loss(self, df: pd.DataFrame):
        """
        Applies the appropriate stop-loss strategy to the DataFrame based on the selected stop-loss type.

        This method checks the stop-loss type and applies the corresponding stop-loss strategy
        (either 'NORMAL' or 'TRAILING') to adjust the 'SELL' signals in the DataFrame.

        Parameters:
        -----------
        df : pd.DataFrame
            A DataFrame containing columns 'Close', 'BUY', and 'SELL'.
            'Close' represents the closing price of the asset.
            'BUY' indicates where buying actions occurred.
            'SELL' will be modified by the selected stop-loss method to indicate where sell actions should occur.

        Returns:
        --------
        None
            The DataFrame is modified in place.
        """

        if self.stop_loss_type == StopLossType.NORMAL:
            self.set_normal_stop_loss(df)
        elif self.stop_loss_type == StopLossType.TRAILING:
            self.set_trailing_stop_loss(df)