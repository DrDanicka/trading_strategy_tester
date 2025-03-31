import pandas as pd

from trading_strategy_tester.utils.parameter_validations import get_length


def momentum(series: pd.Series, length: int = 10) -> pd.Series:
    """
    Calculate the Momentum indicator, which measures the rate of change in price over a specified
    period. The Momentum indicator helps identify the strength of a trend by comparing the current
    price to the price from a certain number of periods ago.

    :param series: A pandas Series representing the price data (e.g., close prices) on which to calculate momentum.
    :type series: pd.Series
    :param length: The number of periods to look back for calculating momentum. Default is 10.
    :type length: int, optional
    :return: A pandas Series containing the Momentum values, with the same index as the input series.
    :rtype: pd.Series
    """
    # Validate the specified length or assign a default
    length = get_length(length=length, default=10)

    # Calculate the momentum as the difference between the current price and the price `length` periods ago
    momentum_series = series - series.shift(length)

    # Return the momentum series with an appropriate name for easy identification
    return pd.Series(momentum_series, name=f'MOMENTUM_{length}')
