import pandas as pd

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

    # Calculate True Range (TR)
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # Calculate Directional Movement (+DM and -DM)
    plus_dm = high.diff()
    minus_dm = low.diff()

    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0.0)
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0.0)

    # Use Wilder's Moving Average (RMA) for smoothing True Range and Directional Movements
    tr_smoothed = true_range.ewm(alpha=1/DI_length, min_periods=DI_length, adjust=False).mean()
    plus_dm_smoothed = plus_dm.ewm(alpha=1/DI_length, min_periods=DI_length, adjust=False).mean()
    minus_dm_smoothed = minus_dm.ewm(alpha=1/DI_length, min_periods=DI_length, adjust=False).mean()

    # Calculate Directional Indicators (+DI and -DI)
    plus_di = 100 * (plus_dm_smoothed / tr_smoothed)
    minus_di = 100 * (minus_dm_smoothed / tr_smoothed)

    # Calculate the Directional Index (DX)
    dx = 100 * (abs(plus_di - minus_di) / (plus_di + minus_di))

    # Calculate the ADX (Average Directional Index) using Wilder's Moving Average
    adx_series = dx.ewm(alpha=1/adx_smoothing, min_periods=adx_smoothing, adjust=False).mean()

    return pd.Series(adx_series, name=f'ADX_{adx_smoothing}_{DI_length}')
