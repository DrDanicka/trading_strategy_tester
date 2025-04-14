import pandas as pd
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trade.order_size.order_size import OrderSize
from trading_strategy_tester.trade.trade_commissions.trade_commissions import TradeCommissions

class Trade:
    """
    A class representing a financial trade, handling various aspects such as entry/exit points,
    invested capital, and performance metrics like profit/loss (P&L), drawdown, and run-up.
    """

    def __init__(self, df_slice: pd.DataFrame, trade_id: int, order_size: OrderSize, current_capital: float,
                 initial_capital: float, trade_commissions: TradeCommissions, long: bool = True):
        """
        Initializes a Trade object with the given data and trade details.

        :param df_slice: A slice of the DataFrame containing trade data (open, high, low, close, etc.).
        :type df_slice: pd.DataFrame
        :param trade_id: A unique identifier for the trade.
        :type trade_id: int
        :param order_size: The object handling order size and invested capital calculations.
        :type order_size: OrderSize
        :param current_capital: The capital available at the start of the trade.
        :type current_capital: float
        :param initial_capital: The starting capital of the trading strategy.
        :type initial_capital: float
        :param trade_commissions: An object that calculates trade commissions.
        :type trade_commissions: TradeCommissions
        :param long: Whether the trade is long (True) or short (False). Defaults to True.
        :type long: bool, optional
        """
        self.data = df_slice
        self.trade_id = trade_id
        self.order_size = order_size
        self.current_capital = current_capital
        self.initial_capital = initial_capital
        self.trade_commissions = trade_commissions
        self.long = long

        # Initialize trade metrics
        self.entry_date, self.exit_date = self.get_dates()
        self.entry_price, self.exit_price = self.get_prices()
        self.entry_signal, self.exit_signal = self.get_signals()
        self.invested, self.contracts = order_size.get_invested_amount(self.entry_price, self.current_capital)
        self.drawdown, self.drawdown_percentage = self.get_drawdown()
        self.run_up, self.run_up_percentage = self.get_run_up()
        self.p_and_l, self.percentage_p_and_l, self.commissions = self.get_p_and_l()
        self.current_capital += self.p_and_l  # Update capital after the trade
        self.cumulative_p_and_l = self.current_capital - self.initial_capital
        self.cumulative_p_and_l_percentage = (self.cumulative_p_and_l * 100) / self.initial_capital

    def get_dates(self) -> tuple:
        """
        Retrieves the entry and exit dates from the DataFrame slice.

        :return: A tuple containing the entry and exit dates.
        :rtype: tuple
        """
        entry_date = self.data.index[0]  # Entry date is the first row
        exit_date = self.data.index.max()  # Exit date is the last row in the slice
        return entry_date, exit_date

    def exit_is_stop_loss(self) -> (bool, float):
        """
        Checks if the exit was due to a stop loss. If so, it returns the percentage of the stop loss.

        :return: A tuple containing a boolean indicating if the exit was due to a stop loss and the percentage of the stop loss.
        :rtype: tuple
        """
        is_stop_loss : bool = False
        percentage : float = 0

        for column in ['BUY_Signals', 'SELL_Signals']:
            if str(self.data[column].iloc[-1]).startswith('StopLoss'):
                is_stop_loss = True
                percentage = float(str(self.data[column].iloc[-1]).split('(')[-1].split(')')[0])

        return is_stop_loss, percentage

    def exit_is_take_profit(self) -> (bool, float):
        """
        Checks if the exit was due to a take profit. If so, it returns the percentage of the take profit.

        :return: A tuple containing a boolean indicating if the exit was due to a take profit and the percentage of the take profit.
        :rtype: tuple
        """
        is_take_profit : bool = False
        percentage : float = 0

        for column in ['BUY_Signals', 'SELL_Signals']:
            if str(self.data[column].iloc[-1]).startswith('TakeProfit'):
                is_take_profit = True
                percentage = float(str(self.data[column].iloc[-1]).split('(')[-1].split(')')[0])

        return is_take_profit, percentage

    def get_prices(self) -> tuple:
        """
        Retrieves the entry and exit prices from the DataFrame slice.

        :return: A tuple containing the entry and exit prices based on the 'Open' column.
        :rtype: tuple
        """
        entry_price = self.data[SourceType.OPEN.value].iloc[0]  # First 'Open' price after entry signal
        exit_price = self.data[SourceType.OPEN.value].iloc[-1]  # Last 'Open' price for exit

        # Find you if exit was not Stop loss or Take profit
        has_stop_loss, stop_loss_percentage = self.exit_is_stop_loss()
        has_take_profit, take_profit_percentage = self.exit_is_take_profit()

        if has_stop_loss:
            value_threshold = (entry_price * stop_loss_percentage) / 100
            exit_price = min(self.data[SourceType.OPEN.value].iloc[-1], entry_price - value_threshold)
        elif has_take_profit:
            value_threshold = (entry_price * take_profit_percentage) / 100
            exit_price = max(self.data[SourceType.OPEN.value].iloc[-1], entry_price + value_threshold)

        return entry_price, exit_price

    def get_signals(self) -> tuple:
        """
        Retrieves the entry and exit signals based on the trade direction (long or short).

        :return: A tuple containing the entry and exit signals.
        :rtype: tuple
        """
        entry_signal = self.data['BUY_Signals'].iloc[0] if self.long else self.data['SELL_Signals'].iloc[0]
        exit_signal = self.data['SELL_Signals'].iloc[-1] if self.long else self.data['BUY_Signals'].iloc[-1]
        return entry_signal, exit_signal

    def get_drawdown(self) -> tuple:
        """
        Calculates the maximum drawdown during the trade and its percentage.

        :return: A tuple containing the absolute and percentage drawdown.
        :rtype: tuple
        """
        if self.long:
            trough = self.data[SourceType.LOW.value].iloc[0:-1].min()  # Lowest price between entry and exit
        else:
            trough = self.data[SourceType.HIGH.value].iloc[0:-1].max()  # Highest price between entry and exit

        drawdown = abs(self.entry_price - trough)
        drawdown_percentage = (drawdown / self.entry_price) * 100 if self.entry_price != 0 else 0
        return self.contracts * drawdown, drawdown_percentage

    def get_run_up(self) -> tuple:
        """
        Calculates the maximum run-up during the trade and its percentage.

        :return: A tuple containing the absolute and percentage run-up.
        :rtype: tuple
        """
        if self.long:
            run_up = self.data[SourceType.HIGH.value].iloc[0:-1].max() - self.entry_price  # Max increase in price
        else:
            run_up = self.entry_price - self.data[SourceType.LOW.value].iloc[0:-1].min()  # Max decrease in price

        run_up_percentage = (run_up / self.entry_price) * 100 if self.entry_price != 0 else 0
        return run_up, run_up_percentage

    def get_p_and_l(self) -> tuple:
        """
        Calculates the profit or loss (P&L) for the trade, along with its percentage and commissions paid.

        :return: A tuple containing P&L, percentage P&L, and commissions paid.
        :rtype: tuple
        """
        if self.long:
            p_and_l = self.contracts * self.exit_price - self.invested  # Profit for long trade
        else:
            p_and_l = self.invested - self.contracts * self.exit_price  # Profit for short trade

        commissions = self.trade_commissions.get_commission(self.entry_price, self.contracts)
        p_and_l -= commissions  # Subtract commissions from P&L
        p_and_l_percentage = (p_and_l * 100) / self.invested if self.invested != 0 else 0  # P&L as a percentage of invested capital
        return p_and_l, p_and_l_percentage, commissions

    def get_summary(self) -> dict:
        """
        Returns a summary of the trade, including performance metrics and trade details.

        :return: A dictionary containing the trade summary.
        :rtype: dict
        """
        return {
            'ID': self.trade_id,
            'Type': 'Long' if self.long else 'Short',
            'Entry Date': self.entry_date.strftime('%b %d, %Y'),
            'Exit Date': self.exit_date.strftime('%b %d, %Y'),
            'Entry Price': round(self.entry_price, 2),
            'Exit Price': round(self.exit_price, 2),
            'Invested': round(self.invested, 2),
            'Contracts': round(self.contracts, 2),
            'Entry Signal': self.entry_signal,
            'Exit Signal': self.exit_signal,
            'Commissions Paid': round(self.commissions, 2),
            'P&L': round(self.p_and_l, 2),
            'Percentage P&L': round(self.percentage_p_and_l, 2),
            'Cumulative P&L': round(self.cumulative_p_and_l, 2),
            'Percentage Cumulative P&L': round(self.cumulative_p_and_l_percentage, 2),
            'Run-up': round(self.run_up, 2),
            'Percentage Run-up': round(self.run_up_percentage, 2),
            'Drawdown': round(self.drawdown, 2),
            'Percentage Drawdown': round(self.drawdown_percentage, 2),
            'Current Capital': round(self.current_capital, 2)
        }

    def get_summary_with_units(self) -> dict:
        """
        Returns a summary of the trade with units (USD) for all monetary values.

        :return: A dictionary containing the trade summary with USD units.
        :rtype: dict
        """
        return {
            'ID': self.trade_id,
            'Type': 'Long' if self.long else 'Short',
            'Entry Date': self.entry_date.strftime('%b %d, %Y'),
            'Exit Date': self.exit_date.strftime('%b %d, %Y'),
            'Entry Price': f'{round(self.entry_price, 2)}$',
            'Exit Price': f'{round(self.exit_price, 2)}$',
            'Invested': f'{round(self.invested, 2)}$',
            'Contracts': round(self.contracts, 2),
            'Entry Signal': self.entry_signal,
            'Exit Signal': self.exit_signal,
            'Commissions Paid': f'{round(self.commissions, 2)}$',
            'P&L': f'{round(self.p_and_l, 2)}$',
            'Percentage P&L': f'{round(self.percentage_p_and_l, 2)}%',
            'Cumulative P&L': f'{round(self.cumulative_p_and_l, 2)}$',
            'Percentage Cumulative P&L': f'{round(self.cumulative_p_and_l_percentage, 2)}%',
            'Run-up': f'{round(self.run_up, 2)}$',
            'Percentage Run-up': f'{round(self.run_up_percentage, 2)}%',
            'Drawdown': f'{round(self.drawdown, 2)}$',
            'Percentage Drawdown': f'{round(self.drawdown_percentage, 2)}%',
            'Current Capital': f'{round(self.current_capital, 2)}$'
        }

    def get_capital_after_trade(self):
        """
        Returns the current capital after the trade has been processed.

        :return: The updated capital.
        :rtype: float
        """
        return self.current_capital

    def __repr__(self) -> str:
        """
        Returns a string representation of the trade object, displaying key details.

        :return: A string summary of the trade.
        :rtype: str
        """
        return (
            f"Trade(\n"
            f"  ID={self.trade_id},\n"
            f"  Type={'Long' if self.long else 'Short'},\n"
            f"  Entry Date={self.entry_date},\n"
            f"  Exit Date={self.exit_date},\n"
            f"  Entry Price={self.entry_price:.2f} USD,\n"
            f"  Exit Price={self.exit_price:.2f} USD,\n"
            f"  Invested={self.invested:.2f} USD,\n"
            f"  Contracts={self.contracts:.2f}\n"
            f"  Entry Signal={self.entry_signal},\n"
            f"  Exit Signal={self.exit_signal},\n"
            f"  Commissions Paid={self.commissions:.2f} USD,\n"
            f"  P&L={self.p_and_l:.2f} USD,\n"
            f"  Percentage P&L={self.percentage_p_and_l:.2f}%,\n"
            f"  Cumulative P&L={self.cumulative_p_and_l:.2f} USD,\n"
            f"  Percentage Cumulative P&L={self.cumulative_p_and_l_percentage:.2f}%,\n"
            f"  Run-up={self.run_up:.2f} USD,\n"
            f"  Percentage Run-up={self.run_up_percentage:.2f}%,\n"
            f"  Drawdown={self.drawdown:.2f} USD,\n"
            f"  Drawdown Percentage={self.drawdown_percentage:.2f}%,\n"
            f"  Current Capital={self.current_capital:.2f} USD"
            f"\n)"
            )


def create_all_trades(df: pd.DataFrame, order_size: OrderSize, initial_capital: float,
                      trade_commissions: TradeCommissions) -> list[Trade]:
    """
    Creates a list of Trade objects based on buy/sell signals from the provided DataFrame, handling both long and short trades.

    This function processes each row of the DataFrame to identify entry and exit signals for both long and short trades.
    It slices the DataFrame appropriately to create Trade objects, calculates trade performance, and updates the available
    capital after each trade.

    :param df: The DataFrame containing trading data, including buy/sell signals and prices.
               Expected columns include 'BUY', 'SELL', 'Long', and 'Short', which indicate trade signals.
    :type df: pd.DataFrame
    :param order_size: An instance of the OrderSize class that determines the invested amount and number of contracts.
    :type order_size: OrderSize
    :param initial_capital: The starting capital for the trading strategy.
    :type initial_capital: float
    :param trade_commissions: An object for calculating trade commissions. This instance should provide a method to compute
                              the commission based on entry price and the number of contracts.
    :type trade_commissions: TradeCommissions
    :return: A list of Trade objects representing all trades executed in the DataFrame.
    :rtype: list[Trade]
    """

    # Initialize capital and an empty list to store the Trade objects
    current_capital = initial_capital
    trades = []

    # Indices to track the start (entry) of trades for both long and short positions
    buy_index = 0
    sell_index = 0

    # A counter for assigning unique trade IDs to each trade
    counter = 1

    # Iterate over each row in the DataFrame
    for i, (_, row) in enumerate(df.iterrows()):

        # Detect long entry signal (BUY signal and 'LongEntry')
        if row['BUY'] and row['Long'] == 'LongEntry':
            buy_index = i  # Record the index of the long entry

        # Detect long exit signal (SELL signal and 'LongExit') and execute the trade
        if row['SELL'] and row['Long'] == 'LongExit':
            end_index = i + 1 if i + 1 <= len(df) else len(df)  # Define slice range, ensuring it's within bounds

            entry_price = df.iloc[buy_index][SourceType.OPEN.value]
            invested, contracts = order_size.get_invested_amount(entry_price, current_capital)

            # Split if we have no money to invest
            if contracts == 0:
                continue

            # Create a long Trade object and update the capital
            long_trade = Trade(
                df_slice=df.iloc[buy_index:end_index],
                trade_id=counter,
                order_size=order_size,
                current_capital=current_capital,
                initial_capital=initial_capital,
                trade_commissions=trade_commissions,
                long=True
            )
            counter += 1  # Increment trade counter
            current_capital = long_trade.get_capital_after_trade()  # Update capital after the trade
            trades.append(long_trade)  # Append the long trade to the list

        # Detect short entry signal (SELL signal and 'ShortEntry')
        if row['SELL'] and row['Short'] == 'ShortEntry':
            sell_index = i  # Record the index of the short entry

        # Detect short exit signal (BUY signal and 'ShortExit') and execute the trade
        if row['BUY'] and row['Short'] == 'ShortExit':
            end_index = i + 1 if i + 1 <= len(df) else len(df)  # Define slice range, ensuring it's within bounds

            entry_price = df.iloc[sell_index][SourceType.OPEN.value]
            invested, contracts = order_size.get_invested_amount(entry_price, current_capital)

            # Split if we have no money to invest
            if contracts == 0:
                continue

            # Create a short Trade object and update the capital
            short_trade = Trade(
                df_slice=df.iloc[sell_index:end_index],
                trade_id=counter,
                order_size=order_size,
                current_capital=current_capital,
                initial_capital=initial_capital,
                trade_commissions=trade_commissions,
                long=False  # Indicating a short trade
            )
            counter += 1  # Increment trade counter
            current_capital = short_trade.get_capital_after_trade()  # Update capital after the trade
            trades.append(short_trade)  # Append the short trade to the list

    # Return the list of all Trade objects
    return trades
