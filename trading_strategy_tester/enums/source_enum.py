from enum import Enum

class SourceType(Enum):
    """
    Enum for defining different types of price sources for financial instruments.

    Attributes:
    -----------
    CLOSE : str
        Represents the closing price of the instrument.
    OPEN : str
        Represents the opening price of the instrument.
    HIGH : str
        Represents the highest price of the instrument.
    LOW : str
        Represents the lowest price of the instrument.
    HLC3 : str
        Represents the average of the High, Low, and Close prices (HLC/3).
    HL2 : str
        Represents the average of the High and Low prices (HL/2).
    OHLC4 : str
        Represents the average of the Open, High, Low, and Close prices (OHLC/4).
    HLCC4 : str
        Represents the weighted average of the High, Low, and two times the Close price ((High + Low + 2 * Close) / 4).
    VOLUME : str
        Represents the volume of the instrument
    """

    CLOSE = 'Close'
    OPEN = 'Open'
    HIGH = 'High'
    LOW = 'Low'
    HLC3 = 'HLC3'
    HL2 = 'HL2'
    OHLC4 = 'OHLC4'
    HLCC4 = 'HLCC4'
    VOLUME = 'Volume'
