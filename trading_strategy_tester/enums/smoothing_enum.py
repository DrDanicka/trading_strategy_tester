from enum import Enum

class SmoothingType(Enum):
    """
    SmoothingType is an enumeration that represents different types of smoothing techniques used
    in data analysis, particularly in the context of time series and financial data.

    Attributes:
    ----------
    RMA : str
        Represents the Running Moving Average (RMA) smoothing technique.
    SMA : str
        Represents the Simple Moving Average (SMA) smoothing technique.
    EMA : str
        Represents the Exponential Moving Average (EMA) smoothing technique.
    WMA : str
        Represents the Weighted Moving Average (WMA) smoothing technique.
    """

    RMA = 'RMA'  # Running Moving Average
    SMA = 'SMA'  # Simple Moving Average
    EMA = 'EMA'  # Exponential Moving Average
    WMA = 'WMA'  # Weighted Moving Average
