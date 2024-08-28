import pandas as pd
from trading_strategy_tester.indicators.atr import atr
from trading_strategy_tester.smoothings.rma_smoothing import rma_smoothing
from trading_strategy_tester.utils.validations import get_length


def adx(high: pd.Series, low: pd.Series, close: pd.Series, adx_smoothing: int = 14, DI_length: int = 14) -> pd.Series:
    """
    Calculate the Average Directional Index (ADX) and the Directional Indicators (+DI and -DI).

    The ADX is a trend strength indicator. It is based on the moving averages of the expansion of
    price range over a given period of time.

    Parameters:
    -----------
    high : pd.Series
        A pandas Series representing the high prices.
    low : pd.Series
        A pandas Series representing the low prices.
    close : pd.Series
        A pandas Series representing the closing prices.
    adx_smoothing : int
        The smoothing period for calculating the ADX.
    DI_length : int
        The period length to calculate the Directional Indicators (+DI and -DI).

    Returns:
    --------
    pd.Series
        The ADX indicator of the given series.
    """

    # Validate arguments
    adx_smoothing = get_length(length=adx_smoothing, default=14)
    DI_length = get_length(length=DI_length, default=14)

    atr_series = atr(high, low, close, DI_length)

    # Calculate Directional Movement (+DM and -DM)
    plus_dm = high.diff()
    minus_dm = -low.diff()

    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0.0)
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0.0)

    plus_dm_smoothed = rma_smoothing(plus_dm, DI_length)
    minus_dm_smoothed = rma_smoothing(minus_dm, DI_length)

    # Calculate Directional Indicators (+DI and -DI)
    plus_di = 100 * (plus_dm_smoothed / atr_series)
    minus_di = 100 * (minus_dm_smoothed / atr_series)

    # Calculate the Directional Index (DX)
    dx = 100 * (abs(plus_di - minus_di) / (plus_di + minus_di))

    # Calculate the ADX (Average Directional Index) using Wilder's Moving Average
    adx_series = rma_smoothing(dx, adx_smoothing)

    return pd.Series(adx_series, name=f'ADX_{adx_smoothing}_{DI_length}')
