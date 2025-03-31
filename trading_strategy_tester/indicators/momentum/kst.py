import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length
from trading_strategy_tester.indicators.momentum.roc import roc


def kst(series: pd.Series,
        roc_length_1: int = 10,
        roc_length_2: int = 15,
        roc_length_3: int = 20,
        roc_length_4: int = 30,
        sma_length_1: int = 10,
        sma_length_2: int = 10,
        sma_length_3: int = 10,
        sma_length_4: int = 15) -> pd.Series:
    """
    Calculate the Know Sure Thing (KST) line for a given time series.

    The KST is a momentum oscillator that combines smoothed Rate of Change (ROC) values over different timeframes.
    It is used to determine the momentum direction and strength of a trend. The calculation includes smoothing
    the ROC values with simple moving averages (SMAs) and weighting them with fixed multipliers.

    :param series: A pandas Series representing the series data (e.g., closing prices) for which the KST line is to be calculated.
    :type series: pd.Series
    :param roc_length_1: The period length for the first ROC calculation. Default is 10.
    :type roc_length_1: int, optional
    :param roc_length_2: The period length for the second ROC calculation. Default is 15.
    :type roc_length_2: int, optional
    :param roc_length_3: The period length for the third ROC calculation. Default is 20.
    :type roc_length_3: int, optional
    :param roc_length_4: The period length for the fourth ROC calculation. Default is 30.
    :type roc_length_4: int, optional
    :param sma_length_1: The period length for the SMA of the first ROC. Default is 10.
    :type sma_length_1: int, optional
    :param sma_length_2: The period length for the SMA of the second ROC. Default is 10.
    :type sma_length_2: int, optional
    :param sma_length_3: The period length for the SMA of the third ROC. Default is 10.
    :type sma_length_3: int, optional
    :param sma_length_4: The period length for the SMA of the fourth ROC. Default is 15.
    :type sma_length_4: int, optional
    :return: A pandas Series containing the KST values for the input series.
    :rtype: pd.Series
    """

    # Validate arguments
    roc_length_1 = get_length(length=roc_length_1, default=10)
    roc_length_2 = get_length(length=roc_length_2, default=15)
    roc_length_3 = get_length(length=roc_length_3, default=20)
    roc_length_4 = get_length(length=roc_length_4, default=30)
    sma_length_1 = get_length(length=sma_length_1, default=10)
    sma_length_2 = get_length(length=sma_length_2, default=10)
    sma_length_3 = get_length(length=sma_length_3, default=10)
    sma_length_4 = get_length(length=sma_length_4, default=15)

    # Calculate Rate Of Change for each period
    roc_1 = roc(series=series, length=roc_length_1)
    roc_2 = roc(series=series, length=roc_length_2)
    roc_3 = roc(series=series, length=roc_length_3)
    roc_4 = roc(series=series, length=roc_length_4)

    # Smooth each ROC using SMA
    roc_1_smoothen = smooth(series=roc_1, length=sma_length_1, smoothing_type=SmoothingType.SMA)
    roc_2_smoothen = smooth(series=roc_2, length=sma_length_2, smoothing_type=SmoothingType.SMA)
    roc_3_smoothen = smooth(series=roc_3, length=sma_length_3, smoothing_type=SmoothingType.SMA)
    roc_4_smoothen = smooth(series=roc_4, length=sma_length_4, smoothing_type=SmoothingType.SMA)

    # Sum the weighted ROCs to get the KST line
    kst_series = roc_1_smoothen + 2 * roc_2_smoothen + 3 * roc_3_smoothen + 4 * roc_4_smoothen

    return pd.Series(kst_series,
                     name=f'KST_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}')


def kst_signal(series: pd.Series,
               roc_length_1: int = 10,
               roc_length_2: int = 15,
               roc_length_3: int = 20,
               roc_length_4: int = 30,
               sma_length_1: int = 10,
               sma_length_2: int = 10,
               sma_length_3: int = 10,
               sma_length_4: int = 15,
               signal_length: int = 9) -> pd.Series:
    """
    Calculate the Know Sure Thing (KST) signal line for a given time series.

    The KST signal line is a simple moving average of the KST line, which provides a smoothed reference
    for identifying trend changes. The signal line helps in identifying KST crossovers, often used as buy or sell signals.

    :param series: A pandas Series representing the series data (e.g., closing prices) for which the KST signal line is to be calculated.
    :type series: pd.Series
    :param roc_length_1: The period length for the first ROC calculation. Default is 10.
    :type roc_length_1: int, optional
    :param roc_length_2: The period length for the second ROC calculation. Default is 15.
    :type roc_length_2: int, optional
    :param roc_length_3: The period length for the third ROC calculation. Default is 20.
    :type roc_length_3: int, optional
    :param roc_length_4: The period length for the fourth ROC calculation. Default is 30.
    :type roc_length_4: int, optional
    :param sma_length_1: The period length for the SMA of the first ROC. Default is 10.
    :type sma_length_1: int, optional
    :param sma_length_2: The period length for the SMA of the second ROC. Default is 10.
    :type sma_length_2: int, optional
    :param sma_length_3: The period length for the SMA of the third ROC. Default is 10.
    :type sma_length_3: int, optional
    :param sma_length_4: The period length for the SMA of the fourth ROC. Default is 15.
    :type sma_length_4: int, optional
    :param signal_length: The period length for the SMA of the KST line, which generates the signal line. Default is 9.
    :type signal_length: int, optional
    :return: A pandas Series containing the KST signal values for the input series.
    :rtype: pd.Series
    """

    # Calculate KST line
    kst_series = kst(series, roc_length_1, roc_length_2, roc_length_3, roc_length_4, sma_length_1, sma_length_2,
                     sma_length_3, sma_length_4)

    # Calculate KST signal line by smoothing KST line
    kst_signal_series = smooth(series=kst_series, length=signal_length, smoothing_type=SmoothingType.SMA)

    return pd.Series(kst_signal_series,
                     name=f'KST-SIGNAL_{roc_length_1}_{roc_length_2}_{roc_length_3}_{roc_length_4}_{sma_length_1}_{sma_length_2}_{sma_length_3}_{sma_length_4}_{signal_length}')
