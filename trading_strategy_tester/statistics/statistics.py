import pandas as pd
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.trade.trade import Trade

def get_strategy_stats(trades: [Trade], df: pd.DataFrame, investing_type) -> dict:
    """
    Calculates and returns various statistics for a given trading strategy based on a list of trades and market data.

    :param trades: A list of Trade objects representing individual trades made during the strategy.
    :type trades: list[Trade]
    :param df: A pandas DataFrame containing market data, including the 'Close' prices used to calculate buy-and-hold returns.
    :type df: pd.DataFrame
    :param investing_type: The type of investing strategy (not used directly in the function but may influence other parameters).
    :type investing_type: Any
    :return: A dictionary containing various strategy statistics, including net profit, gross profit, gross loss, max drawdown,
             buy-and-hold return, commissions paid, total trades, number of winning trades, number of losing trades,
             average trade P&L, largest winning trade, and largest losing trade.
    :rtype: dict
    """
    net_profit = 0
    gross_profit = 0
    gross_loss = 0
    max_drawdown = 0
    buy_and_hold_return = (100 * df[SourceType.CLOSE.value].iloc[-1]) / df[SourceType.CLOSE.value].iloc[0]
    commissions_paid = 0
    total_trades = len(trades)
    number_of_winning_trades = 0
    number_of_losing_trades = 0

    trade_p_and_l = []
    largest_winning_trade = 0
    largest_losing_trade = 0

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

        max_drawdown = max(max_drawdown, trade_summary['Max Drawdown'])

    average_trade = sum(trade_p_and_l) / total_trades

    return {
        'Net Profit': float(net_profit),
        'Gross Profit': float(gross_profit),
        'Gross Loss': float(gross_loss),
        'Max Drawdown': float(max_drawdown),
        'Buy and Hold Return': float(buy_and_hold_return),
        'Commissions Paid': commissions_paid,
        'Total Trades': total_trades,
        'Number of Winning Trades': number_of_winning_trades,
        'Number of Losing Trades': number_of_losing_trades,
        'Average Trade': float(average_trade),
        'Largest Winning Trade': float(largest_winning_trade),
        'Largest Losing Trade': float(largest_losing_trade)
    }
