import pandas as pd

from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.smoothings.smooth import smooth
from trading_strategy_tester.utils.parameter_validations import get_length


def eom(high: pd.Series, low: pd.Series, volume: pd.Series, length: int = 14, divisor: int = 10_000) -> pd.Series:
    """
    Calculate the Ease of Movement (EOM) indicator.

    The Ease of Movement (EOM) is a volume-based oscillator that emphasizes the relationship between
    price changes and volume. It is used to assess the strength of price movements relative to the volume involved.

    :param high: Series of high prices.
    :type high: pd.Series
    :param low: Series of low prices.
    :type low: pd.Series
    :param volume: Series of volume data.
    :type volume: pd.Series
    :param length: The smoothing period for the EOM, default is 14.
    :type length: int, optional
    :param divisor: Divisor to scale the EOM values, default is 10_000.
    :type divisor: int, optional
    :return: Ease of Movement (EOM) indicator as a Pandas Series.
    :rtype: pd.Series
    """
    # Validate the smoothing period length; set to default if invalid
    length = get_length(length=length, default=14)

    # Ensure the divisor is a valid positive number
    if divisor <= 0:
        divisor = 10_000

    # Calculate the midpoint price
    mid_point = (high + low) / 2

    # Calculate the change in midpoint price
    mid_point_move = mid_point.diff()

    # Calculate the box ratio (volume per price change)
    box_ratio = volume / (high - low)

    # Compute the raw Ease of Movement (EOM) values
    eom_series = mid_point_move / box_ratio

    # Apply smoothing to the EOM values and scale by the divisor
    eom_series_smoothened = smooth(eom_series, length=length, smoothing_type=SmoothingType.SMA) * divisor

    # Return the EOM series as a Pandas Series with an appropriate name
    return pd.Series(eom_series_smoothened, name=f'EOM_{length}_{divisor}')
