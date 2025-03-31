import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.indicators.momentum.roc import roc
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def cop(series: pd.Series, length: int = 10, long_roc_length: int = 14, short_roc_length: int = 11) -> pd.Series:
    """
    Calculate the Coppock Curve indicator for a given price series.

    The Coppock Curve is a momentum-based indicator used to identify potential long-term buying opportunities
    in the market. It is calculated by summing the Rate of Change (ROC) over two different periods, and then
    applying a weighted moving average (WMA) to smooth the result.

    :param series: A pandas Series representing the series data (e.g., closing prices) for which the Coppock Curve is to be calculated.
    :type series: pd.Series
    :param length: The window length to calculate the weighted moving average for smoothing the Coppock Curve. Default is 10.
    :type length: int, optional
    :param long_roc_length: The number of periods for the long rate of change (ROC). Default is 14.
    :type long_roc_length: int, optional
    :param short_roc_length: The number of periods for the short rate of change (ROC). Default is 11.
    :type short_roc_length: int, optional
    :return: A pandas Series containing the Coppock Curve values for the input series, with the same index as the input series.
    :rtype: pd.Series
    """
    # Validate arguments
    length = get_length(length=length, default=10)  # Ensure length is a valid integer
    long_roc_length = get_length(length=long_roc_length, default=14)  # Ensure long ROC length is valid
    short_roc_length = get_length(length=short_roc_length, default=11)  # Ensure short ROC length is valid

    # Calculate the long and short Rate of Change (ROC) for the given series
    long_roc_series = roc(series, long_roc_length)  # Long ROC for the specified period
    short_roc_series = roc(series, short_roc_length)  # Short ROC for the specified period

    # Sum the long and short ROC series to compute the base result for the Coppock Curve
    result = long_roc_series + short_roc_series

    # Smooth the result using a Weighted Moving Average (WMA) with the specified length
    coppock_series = smooth(result, length, SmoothingType.WMA)

    # Return the Coppock Curve as a pandas Series with a descriptive name
    return pd.Series(coppock_series, name=f'COPPOCK_{length}_{long_roc_length}_{short_roc_length}')
