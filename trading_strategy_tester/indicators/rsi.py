import pandas as pd
from trading_strategy_tester.utils.validations import get_length


def rsi(series: pd.Series, length: int = 14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI) of a given series using Wilder's Moving Average.

    The RSI is a momentum oscillator that measures the speed and change of price movements.
    It oscillates between 0 and 100 and is typically used to identify overbought or oversold conditions in a market.

    :param series: A pandas Series representing the series data (e.g., closing prices) for which the RSI is to be calculated.
    :type series: pd.Series
    :param length: The number of periods to use for calculating the RSI. Default is 14, which is a common standard.
    :type length: int, optional
    :return: A pandas Series containing the RSI values for the input series, with the same index as the input series.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=14)

    # Calculate the difference between consecutive prices
    delta = series.diff()

    # Calculate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Compute the average gain and loss using Wilder's Moving Average (RMA)
    avg_gain = gain.ewm(alpha=1 / length, min_periods=length, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / length, min_periods=length, adjust=False).mean()

    # Calculate the Relative Strength (RS)
    rs = avg_gain / avg_loss

    # Calculate RSI
    rsi_ser = 100 - (100 / (1 + rs))

    return pd.Series(rsi_ser, name=f'RSI_{length}')
