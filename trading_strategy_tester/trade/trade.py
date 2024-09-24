import pandas as pd

from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trade.trade_commissions.trade_commissions import TradeCommissions

class Trade:
    """
    A class to represent a financial trade, encapsulating details such as entry/exit prices, dates,
    and calculations for performance metrics like profit and loss, and drawdown.
    """

    def __init__(self, df_slice: pd.DataFrame, trade_id: int, trade_commissions: TradeCommissions, long: bool = True):
        """
        Initializes the Trade object with the provided DataFrame slice and trade details.

        :param df_slice: A slice of the DataFrame containing trade data.
        :type df_slice: pd.DataFrame
        :param trade_commissions: An object for calculating trade commissions.
        :type trade_commissions: TradeCommissions
        :param long: Indicates if the trade is long (True) or short (False), defaults to True.
        :type long: bool, optional
        """
        self.data = df_slice
        self.trade_id = trade_id
        self.trade_commissions = trade_commissions
        self.long = long
        self.open_date, self.close_date = self.get_dates()
        self.entry_price, self.exit_price = self.get_prices()
        self.entry_signal, self.exit_signal = self.get_signals()
        self.max_drawdown, self.max_drawdown_percentage = self.get_max_drawdown()
        self.p_and_l, self.percentage_p_and_l, self.commissions = self.get_p_and_l()

    def get_dates(self) -> tuple:
        """
        Returns the first and last dates from the DataFrame slice.

        :return: A tuple containing the first and last dates.
        :rtype: tuple
        """
        first_date = self.data.index.min()  # First date of the trade period
        last_date = self.data.index.max()  # Last date of the trade period
        return first_date, last_date

    def get_prices(self) -> tuple:
        """
        Returns the first and last 'Close' prices from the DataFrame slice.

        :return: A tuple containing the entry price (first 'Close' price) and exit price (last 'Close' price).
        :rtype: tuple
        """
        entry_price = self.data[SourceType.CLOSE.value].iloc[0]  # First 'Close' price
        exit_price = self.data[SourceType.CLOSE.value].iloc[-1]  # Last 'Close' price
        return entry_price, exit_price

    def get_signals(self) -> tuple:
        """
        Returns the entry and exit signals based on the trade direction (long or short).

        :return: A tuple containing the entry signal and exit signal.
        :rtype: tuple
        """
        entry_signal = self.data['BUY_Signals'].iloc[0] if self.long else self.data['SELL_Signals'].iloc[0]
        exit_signal = self.data['SELL_Signals'].iloc[-1] if self.long else self.data['BUY_Signals'].iloc[-1]
        return entry_signal, exit_signal

    def get_max_drawdown(self) -> tuple:
        """
        Calculates the maximum drawdown and its percentage during the trade period.

        :return: A tuple containing the maximum drawdown and the maximum drawdown percentage.
        :rtype: tuple
        """
        if self.long:
            peak = self.data[SourceType.CLOSE.value].max()
            trough = self.data[SourceType.CLOSE.value].min()
        else:
            peak = self.data[SourceType.CLOSE.value].min()
            trough = self.data[SourceType.CLOSE.value].max()

        max_drawdown = peak - trough
        max_drawdown_percentage = (max_drawdown / peak) * 100 if peak != 0 else 0
        return max_drawdown, max_drawdown_percentage

    def get_p_and_l(self) -> tuple:
        """
        Calculates the profit or loss (P&L) of the trade and the P&L percentage.

        :return: A tuple containing the profit/loss and the percentage profit/loss.
        :rtype: tuple
        """
        p_and_l = self.exit_price - self.entry_price if self.long else self.entry_price - self.exit_price
        commissions = self.trade_commissions.get_commission(self.entry_price)
        p_and_l -= commissions
        p_and_l_percentage = (p_and_l * 100) / self.entry_price
        return p_and_l, p_and_l_percentage, commissions

    def get_summary(self) -> dict:
        """
        Provides a summary of the trade including type, dates, prices, signals, and performance metrics.

        :return: A dictionary containing the trade summary.
        :rtype: dict
        """
        return {
            'ID': self.trade_id,
            'Type': 'Long' if self.long else 'Short',
            'Open Date': self.open_date,
            'Close Date': self.close_date,
            'Entry Price': self.entry_price,
            'Exit Price': self.exit_price,
            'Entry Signal': self.entry_signal,
            'Exit Signal': self.exit_signal,
            'Commissions Paid': self.commissions,
            'Max Drawdown': self.max_drawdown,
            'Max Drawdown Percentage': self.max_drawdown_percentage,
            'P&L': self.p_and_l,
            'Percentage P&L': self.percentage_p_and_l,
        }

    def __repr__(self) -> str:
        """
        Provides a string representation of the Trade object.

        :return: A string representation of the Trade object.
        :rtype: str
        """
        return (f"Trade(ID={self.trade_id}, Type={'Long' if self.long else 'Short'}, "
                f"Open Date={self.open_date}, Close Date={self.close_date}, "
                f"Entry Price={self.entry_price}, Exit Price={self.exit_price}, "
                f"P&L={self.p_and_l:.2f}, Percentage P&L={self.percentage_p_and_l:.2f}%)")


def create_all_trades(df: pd.DataFrame, trade_commissions: TradeCommissions) -> list[Trade]:
    """
    Creates a list of Trade objects based on buy/sell signals in the provided DataFrame.

    :param df: The DataFrame containing the trading data.
    :type df: pd.DataFrame
    :param trade_commissions: An object for calculating trade commissions.
    :type trade_commissions: TradeCommissions
    :return: A list of Trade objects representing all trades in the DataFrame.
    :rtype: list[Trade]
    """
    trades = []
    buy_index = 0
    sell_index = 0
    counter = 1

    for i, (_, row) in enumerate(df.iterrows()):
        if row['BUY'] and row['Long'] == 'LongEntry':
            buy_index = i

        if row['SELL'] and row['Long'] == 'LongExit':
            long_trade = Trade(df.iloc[buy_index:i + 1], counter, trade_commissions, True)
            counter += 1
            trades.append(long_trade)

        if row['SELL'] and row['Short'] == 'ShortEntry':
            sell_index = i

        if row['BUY'] and row['Short'] == 'ShortExit':
            short_trade = Trade(df.iloc[sell_index:i + 1], counter, trade_commissions, False)
            counter += 1
            trades.append(short_trade)

    return trades
