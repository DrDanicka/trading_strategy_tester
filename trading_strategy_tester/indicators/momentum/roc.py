import pandas as pd
from trading_strategy_tester.utils.parameter_validations import get_length

def roc(series: pd.Series, length: int = 9) -> pd.Series:
    """
    Calculate the Rate of Change (ROC) of a given series.

    The Rate of Change (ROC) is a momentum oscillator that measures the percentage change in price between
    the current price and the price n periods ago. It helps identify overbought or oversold conditions
    and the speed of price changes.

    :param series: A pandas Series representing the series data (e.g., closing prices) for which the ROC is to be calculated.
    :type series: pd.Series
    :param length: The number of periods to use for calculating the ROC. Default is 9.
    :type length: int, optional
    :return: A pandas Series containing the ROC values for the input series, with the same index as the input series.
    :rtype: pd.Series
    """

    # Validate arguments
    length = get_length(length=length, default=14)

    # Calculate the ROC
    roc_ser = (series.diff(length) / series.shift(length)) * 100

    return pd.Series(roc_ser, name=f'ROC_{length}')
