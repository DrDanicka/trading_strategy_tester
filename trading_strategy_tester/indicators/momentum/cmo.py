import pandas as pd

from trading_strategy_tester.utils.parameter_validations import get_length

def cmo(series: pd.Series, length: int = 9) -> pd.Series:
    """
    Calculate the Chande Momentum Oscillator (CMO) for a given price series.

    The Chande Momentum Oscillator (CMO) is a technical indicator that measures the difference
    between the sum of all recent gains and the sum of all recent losses over a specified period,
    divided by the total sum of all price movements during the same period.

    :param series: The price series (e.g., 'Close') for which the CMO is calculated.
    :type series: pd.Series
    :param length: The number of periods over which to calculate the CMO. Default is 9.
    :type length: int, optional
    :return: A pandas Series containing the CMO values for the specified price series and length.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=9)

    # Calculate the price changes (differences between consecutive prices)
    delta = series.diff()

    # Separate the gains (positive changes) and losses (negative changes)
    gains = delta.where(delta > 0, 0.0)  # Keep positive changes only, set others to 0
    losses = -delta.where(delta < 0, 0.0)  # Keep negative changes only, convert to positive, set others to 0

    # Sum the gains and losses over the specified period (length)
    sum_gains = gains.rolling(window=length).sum()
    sum_losses = losses.rolling(window=length).sum()

    # Calculate the Chande Momentum Oscillator (CMO)
    cmo = 100 * (sum_gains - sum_losses) / (sum_gains + sum_losses)

    return pd.Series(cmo, name=f'CMO_{length}')
