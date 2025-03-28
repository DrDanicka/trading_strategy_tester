import pandas as pd
from trading_strategy_tester.enums.source_enum import SourceType

def get_source_series(df: pd.DataFrame, source: SourceType) -> pd.Series:
    """
    Extracts or computes the desired price data series from a DataFrame.

    Depending on the selected `source` type, this function either returns a specific price column
    (such as 'Close', 'Open', 'High', or 'Low') or computes a derived series (such as HLC3, HL2, or HLCC4).

    :param df: The DataFrame containing the price data (with columns like 'Open', 'High', 'Low', 'Close').
    :type df: pd.DataFrame
    :param source: The type of price source to extract or compute, defined in the `SourceType` enum.
    :type source: SourceType
    :return: A pandas Series representing the desired price source.
    :rtype: pd.Series
    """
    if source in [SourceType.CLOSE, SourceType.OPEN, SourceType.HIGH, SourceType.LOW]:
        # Return the direct price column if it matches one of the basic price types
        return df[source.value]
    else:
        # Compute the derived price series based on the selected source type
        if source == SourceType.HLC3:
            # Typical Price: (High + Low + Close) / 3
            return (df[SourceType.HIGH.value] + df[SourceType.LOW.value] + df[SourceType.CLOSE.value]) / 3.0
        elif source == SourceType.HL2:
            # Median Price: (High + Low) / 2
            return (df[SourceType.HIGH.value] + df[SourceType.LOW.value]) / 2.0
        elif source == SourceType.HLCC4:
            # Weighted Close Price: (High + Low + Close + Close) / 4
            return (df[SourceType.HIGH.value] + df[SourceType.LOW.value] + df[SourceType.CLOSE.value] + df[SourceType.CLOSE.value]) / 4.0
        elif source == SourceType.OHLC4:
            # OHLC4 (Open + High + Low + Close) / 4
            return (df[SourceType.OPEN.value] + df[SourceType.HIGH.value] + df[SourceType.LOW.value] + df[SourceType.CLOSE.value]) / 4.0
        else:
            # Default to Close
            return df[SourceType.CLOSE.value]