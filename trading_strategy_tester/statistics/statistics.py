import pandas as pd
import numpy as np
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trade.order_size.order_size import OrderSize
from trading_strategy_tester.trade.trade import Trade

def get_strategy_stats(trades: list[Trade], df: pd.DataFrame, initial_capital: float, order_size: OrderSize) -> dict:
    """
    Calculates and returns various statistics for a given trading strategy based on a list of trades and market data.

    :param trades: A list of Trade objects representing individual trades made during the strategy.
    :type trades: list[Trade]
    :param df: A pandas DataFrame containing market data, including the 'Close' prices used to calculate buy-and-hold returns.
    :type df: pd.DataFrame
    :param initial_capital: The initial capital used for the trading strategy.
    :type initial_capital: float
    :param order_size: An instance of OrderSize that defines the size of each order in the strategy.
    :type order_size: OrderSize
    :return: A dictionary containing various strategy statistics, including net profit, gross profit, gross loss, max drawdown,
             buy-and-hold return, commissions paid, total trades, number of winning trades, number of losing trades,
             average trade P&L, largest winning trade, and largest losing trade.
    :rtype: dict
    """
    net_profit = 0
    gross_profit = 0
    gross_loss = 0
    max_drawdown = 0
    commissions_paid = 0
    total_trades = len(trades)
    number_of_winning_trades = 0
    number_of_losing_trades = 0

    trade_p_and_l = []
    largest_winning_trade = 0
    largest_losing_trade = 0

    # Calculate buy and hold return
    num_of_contracts = order_size.get_invested_amount(df[SourceType.OPEN.value].iloc[0], initial_capital)[1] if len(df) > 0 else 0
    buy_and_hold_return = num_of_contracts * df[SourceType.OPEN.value].iloc[-1] - num_of_contracts * df[SourceType.OPEN.value].iloc[0] if len(df) > 1 else 0
    buy_and_hold_return_percentage = (100 * df[SourceType.OPEN.value].iloc[-1]) / df[SourceType.OPEN.value].iloc[0] if len(df) > 1 and df[SourceType.OPEN.value].iloc[0] != 0 else 0

    for trade in trades:
        trade_summary = trade.get_summary()
        net_profit += trade_summary['P&L']
        commissions_paid += trade_summary['Commissions Paid']
        trade_p_and_l.append(trade_summary['P&L'])

        if trade_summary['Percentage P&L'] > 0:
            number_of_winning_trades += 1
            gross_profit += trade_summary['P&L']
            largest_winning_trade = max(largest_winning_trade, trade_summary['Percentage P&L'])
        else:
            number_of_losing_trades += 1
            gross_loss += trade_summary['P&L']
            largest_losing_trade = min(largest_losing_trade, trade_summary['Percentage P&L'])

        max_drawdown = max(max_drawdown, trade_summary['Drawdown'])

    # Sharpe Ratio calculation
    if total_trades > 1 and np.std(trade_p_and_l) != 0:
        average_return = np.mean(trade_p_and_l)
        std_dev = np.std(trade_p_and_l)
        sharpe_ratio = average_return / std_dev if std_dev != 0 else None
    else:
        sharpe_ratio = None

    average_trade = sum(trade_p_and_l) / total_trades if total_trades > 0 else 0
    total_pnl = sum(trade_p_and_l)
    total_percent_pnl = (total_pnl / initial_capital) * 100

    return {
        'Net Profit': f'{round(float(net_profit), 2)}$',
        'Gross Profit': f'{round(float(gross_profit), 2)}$',
        'Gross Loss': f'{round(float(gross_loss), 2)}$',
        'Profit factor': round(float(gross_profit / ((-1) * gross_loss)), 2) if gross_loss != 0 else '-',
        'Sharpe Ratio': round(sharpe_ratio, 2) if sharpe_ratio is not None else '-',
        'Max Drawdown': f'{round(float(max_drawdown), 2)}$',
        'Buy and Hold Return': f'{round(float(buy_and_hold_return), 2)}$',
        'Buy and Hold Return Percentage': f'{round(float(buy_and_hold_return_percentage), 2)}%',
        'Commissions Paid': f'{round(float(commissions_paid), 2)}$',
        'Total Trades': total_trades,
        'Number of Winning Trades': number_of_winning_trades,
        'Number of Losing Trades': number_of_losing_trades,
        'Average Trade': f'{round(float(average_trade), 2)}$',
        'Largest Winning Trade': f'{round(float(largest_winning_trade), 2)}$',
        'Largest Losing Trade': f'{round(float(largest_losing_trade), 2)}$',
        'P&L': f'{round(total_pnl, 2)}$',
        'P&L Percentage': f'{round(total_percent_pnl, 2)}%',
    }
