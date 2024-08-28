import pandas as pd

from trading_strategy_tester.utils.validations import get_length
from trading_strategy_tester.indicators.ema import ema


def chaikin_osc(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, fast_length: int = 3, slow_length: int = 10) -> pd.Series:
    """
    Calculates the Chaikin Oscillator, which measures the difference between fast and slow EMAs
    of the Accumulation/Distribution line to gauge the market momentum.

    Parameters:
    -----------
    high : pd.Series
        A pandas Series containing the high prices for each period.

    low : pd.Series
        A pandas Series containing the low prices for each period.

    close : pd.Series
        A pandas Series containing the closing prices for each period.

    volume : pd.Series
        A pandas Series containing the volume data for each period.

    fast_length : int, optional
        The period for the fast EMA. Default is 3.

    slow_length : int, optional
        The period for the slow EMA. Default is 10.

    Returns:
    --------
    pd.Series
        A pandas Series representing the Chaikin Oscillator values.
    """

    # Validate arguments
    fast_length = get_length(length=fast_length, default=3)
    slow_length = get_length(length=slow_length, default=10)

    # Calculate Money Flow Multiplier
    money_flow_multiplier = ((close - low) - (high - close)) / (high - low)

    # Handle division by zero
    money_flow_multiplier.replace([float('inf'), -float('inf')], 0, inplace=True)
    money_flow_multiplier.fillna(0, inplace=True)

    # Calculate Money Flow Volume
    money_flow_volume = money_flow_multiplier * volume

    # Calculate Accumulation/Distribution Line (Cumulative Sum of Money Flow Volume)
    accumulation_distribution = money_flow_volume.cumsum()

    # Calculate the fast and slow EMAs of the A/D line
    fast_ema = ema(series=accumulation_distribution, length=fast_length, offset=0)
    slow_ema = ema(series=accumulation_distribution, length=slow_length, offset=0)

    # Calculate Chaikin Oscillator
    chaikin_osc = fast_ema - slow_ema

    # Return the Chaikin Oscillator as a pandas Series
    return pd.Series(chaikin_osc, name=f'CHAIKINOSC_{fast_length}_{slow_length}')