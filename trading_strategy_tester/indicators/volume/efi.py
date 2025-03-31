import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def efi(close: pd.Series, volume: pd.Series, length: int = 13) -> pd.Series:
    """
    Calculate the Elder Force Index (EFI) indicator.

    The Elder Force Index (EFI) measures the force or power behind a price movement.
    It combines price change and volume to assess the strength of a market trend.

    :param close: Series of close prices.
    :type close: pd.Series
    :param volume: Series of trading volumes.
    :type volume: pd.Series
    :param length: The smoothing period for calculating the exponential moving average (EMA), default is 13.
    :type length: int, optional
    :return: Elder Force Index (EFI) indicator as a Pandas Series.
    :rtype: pd.Series
    """
    # Validate the smoothing period length; set to default if invalid
    length = get_length(length, 13)

    # Calculate the EFI: the difference in close prices multiplied by volume, smoothed by EMA
    efi_series = smooth(close.diff() * volume, length, SmoothingType.EMA)

    # Return the EFI series as a Pandas Series with an appropriate name
    return pd.Series(efi_series, name=f'EFI_{length}')
