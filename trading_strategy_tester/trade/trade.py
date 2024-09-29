import pandas as pd

from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trade.order_size.order_size import OrderSize
from trading_strategy_tester.trade.trade_commissions.trade_commissions import TradeCommissions

class Trade:
    """
    A class to represent a financial trade, encapsulating details such as entry/exit prices, dates,
    and calculations for performance metrics like profit and loss, and drawdown.
    """

    def __init__(self, df_slice: pd.DataFrame, trade_id: int, order_size: OrderSize, current_capital: float, trade_commissions: TradeCommissions, long: bool = True):
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
        self.order_size = order_size
        self.current_capital = current_capital
        self.trade_commissions = trade_commissions
        self.long = long
        self.open_date, self.close_date = self.get_dates()
        self.entry_price, self.exit_price = self.get_prices()
        self.entry_signal, self.exit_signal = self.get_signals()
        self.invested, self.contracts = order_size.get_invested_amount(self.entry_price, self.current_capital)
        self.max_drawdown, self.max_drawdown_percentage = self.get_max_drawdown()
        self.p_and_l, self.percentage_p_and_l, self.commissions = self.get_p_and_l()
        self.current_capital = current_capital + self.p_and_l

    def get_dates(self) -> tuple:
        """
        Returns the first and last dates from the DataFrame slice.

        :return: A tuple containing the first and last dates.
        :rtype: tuple
        """
        first_date = self.data.index[1]  # First date of the trade period
        last_date = self.data.index.max()  # Last date of the trade period
        return first_date, last_date

    def get_prices(self) -> tuple:
        """
        Returns the first and last 'Close' prices from the DataFrame slice.

        :return: A tuple containing the entry price (first 'Close' price) and exit price (last 'Close' price).
        :rtype: tuple
        """
        entry_price = self.data[SourceType.OPEN.value].iloc[1]  # First 'Open' price after the signal
        exit_price = self.data[SourceType.OPEN.value].iloc[-1]  # Last 'Open' price after the signal
        return entry_price, exit_price

    def get_signals(self) -> tuple:
        """
        Returns the entry and exit signals based on the trade direction (long or short).

        :return: A tuple containing the entry signal and exit signal.
        :rtype: tuple
        """
        entry_signal = self.data['BUY_Signals'].iloc[0] if self.long else self.data['SELL_Signals'].iloc[0]
        exit_signal = self.data['SELL_Signals'].iloc[-2] if self.long else self.data['BUY_Signals'].iloc[-2]
        return entry_signal, exit_signal

    def get_max_drawdown(self) -> tuple:
        """
        Calculates the maximum drawdown and its percentage during the trade period.

        :return: A tuple containing the maximum drawdown and the maximum drawdown percentage.
        :rtype: tuple
        """
        if self.long:
            peak = self.data[SourceType.HIGH.value].max()
            trough = self.data[SourceType.LOW.value].min()
        else:
            peak = self.data[SourceType.LOW.value].min()
            trough = self.data[SourceType.HIGH.value].max()

        max_drawdown = peak - trough
        max_drawdown_percentage = (max_drawdown / peak) * 100 if peak != 0 else 0
        return self.contracts * max_drawdown, max_drawdown_percentage

    def get_p_and_l(self) -> tuple:
        """
        Calculates the profit or loss (P&L) of the trade and the P&L percentage.

        :return: A tuple containing the profit/loss and the percentage profit/loss.
        :rtype: tuple
        """
        p_and_l = self.contracts * self.exit_price - self.invested if self.long else self.invested - self.contracts * self.exit_price
        commissions = self.trade_commissions.get_commission(self.entry_price, self.contracts)
        p_and_l -= commissions
        p_and_l_percentage = (p_and_l * 100) / self.invested
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
            'Invested': self.invested,
            'Contracts': self.contracts,
            'Entry Signal': self.entry_signal,
            'Exit Signal': self.exit_signal,
            'Commissions Paid': self.commissions,
            'Max Drawdown': self.max_drawdown,
            'Max Drawdown Percentage': self.max_drawdown_percentage,
            'P&L': self.p_and_l,
            'Percentage P&L': self.percentage_p_and_l,
            'Current Capital': self.current_capital,
        }


    def get_capital_after_trade(self):
        return self.current_capital


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


def create_all_trades(df: pd.DataFrame, order_size: OrderSize, initial_capital: float, trade_commissions: TradeCommissions) -> list[Trade]:
    """
    Creates a list of Trade objects based on buy/sell signals in the provided DataFrame.

    :param df: The DataFrame containing the trading data.
    :type df: pd.DataFrame
    :param trade_commissions: An object for calculating trade commissions.
    :type trade_commissions: TradeCommissions
    :return: A list of Trade objects representing all trades in the DataFrame.
    :rtype: list[Trade]
    """
    current_capital = initial_capital
    trades = []
    buy_index = 0
    sell_index = 0
    counter = 1

    for i, (_, row) in enumerate(df.iterrows()):
        if row['BUY'] and row['Long'] == 'LongEntry':
            buy_index = i

        if row['SELL'] and row['Long'] == 'LongExit':
            end_index = i + 2 if i + 2 <= len(df) else len(df)
            long_trade = Trade(
                df_slice=df.iloc[buy_index:end_index],
                trade_id=counter,
                order_size=order_size,
                current_capital=current_capital,
                trade_commissions=trade_commissions,
                long=True
            )
            counter += 1
            current_capital = long_trade.get_capital_after_trade() # Update current capital
            trades.append(long_trade)

        if row['SELL'] and row['Short'] == 'ShortEntry':
            sell_index = i

        if row['BUY'] and row['Short'] == 'ShortExit':
            end_index = i + 2 if i + 2 <= len(df) else len(df)
            short_trade = Trade(
                df_slice=df.iloc[sell_index:end_index],
                trade_id=counter,
                order_size=order_size,
                current_capital=current_capital,
                trade_commissions=trade_commissions,
                long=False
            )
            counter += 1
            current_capital = short_trade.get_capital_after_trade() # Update current capital
            trades.append(short_trade)

    return trades
