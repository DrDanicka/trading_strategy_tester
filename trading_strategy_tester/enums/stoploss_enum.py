from enum import Enum

class StopLossType(Enum):
    """
    StopLossType is an enumeration that represents different types of stop-loss strategies
    used in trading and risk management.

    Attributes:
    ----------
    NORMAL : str
        Represents a standard stop-loss strategy, where a predefined price level triggers the stop-loss.
    TRAILING : str
        Represents a trailing stop-loss strategy, where the stop-loss price level adjusts as the
        market price moves in favor of the position, locking in profits while limiting losses.
    """

    NORMAL = 'normal'      # Standard stop-loss strategy
    TRAILING = 'trailing'  # Trailing stop-loss strategy
