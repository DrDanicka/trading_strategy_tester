from enum import Enum

class PositionTypeEnum(Enum):
    """
    Enum for defining the types of trading positions a strategy can take.

    Attributes:
    -----------
    LONG : str
        Represents a long position that profits when the price of an asset increases.
    SHORT : str
        Represents a short position that profits when the price of an asset decreases.
    LONG_SHORT_COMBINED : str
        Represents a combined strategy that can take both long and short positions, either simultaneously or alternately.
    """

    LONG = 'LONG'
    SHORT = 'SHORT'
    LONG_SHORT_COMBINED = 'LONG_SHORT_COMBINED'
