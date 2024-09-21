from enum import Enum

class FibonacciLevels(Enum):
    """
    Enum representing the commonly used Fibonacci retracement levels.

    These levels are used in technical analysis to predict potential support and resistance
    areas based on the Fibonacci sequence. Each level is represented as a percentage.

    Attributes:
    -----------
    LEVEL_0 : str
        The 0% Fibonacci retracement level (no retracement).
    LEVEL_23_6 : str
        The 23.6% Fibonacci retracement level.
    LEVEL_38_2 : str
        The 38.2% Fibonacci retracement level.
    LEVEL_50 : str
        The 50% Fibonacci retracement level (often used, though not directly derived from Fibonacci sequence).
    LEVEL_61_8 : str
        The 61.8% Fibonacci retracement level (Golden Ratio).
    LEVEL_100 : str
        The 100% Fibonacci retracement level (full retracement).
    """

    LEVEL_0 = '0'
    LEVEL_23_6 = '23.6'
    LEVEL_38_2 = '38.2'
    LEVEL_50 = '50'
    LEVEL_61_8 = '61.8'
    LEVEL_100 = '100'
