from enum import Enum


class Interval(Enum):
    """
    Interval is an enumeration that represents various time intervals commonly used in data analysis,
    particularly in the context of financial data or time series data.

    Attributes:
    ----------
    ONE_MINUTE : str
        Represents a 1-minute interval ('1m').
    TWO_MINUTES : str
        Represents a 2-minute interval ('2m').
    FIVE_MINUTES : str
        Represents a 5-minute interval ('5m').
    FIFTEEN_MINUTES : str
        Represents a 15-minute interval ('15m').
    THIRTY_MINUTES : str
        Represents a 30-minute interval ('30m').
    SIXTY_MINUTES : str
        Represents a 60-minute interval ('60m').
    NINETY_MINUTES : str
        Represents a 90-minute interval ('90m').
    ONE_HOUR : str
        Represents a 1-hour interval ('1h').
    ONE_DAY : str
        Represents a 1-day interval ('1d').
    FIVE_DAYS : str
        Represents a 5-day interval ('5d').
    ONE_WEEK : str
        Represents a 1-week interval ('1wk').
    ONE_MONTH : str
        Represents a 1-month interval ('1mo').
    THREE_MONTHS : str
        Represents a 3-month interval ('3mo').
    """

    ONE_MINUTE = '1m'  # 1-minute interval
    TWO_MINUTES = '2m'  # 2-minute interval
    FIVE_MINUTES = '5m'  # 5-minute interval
    FIFTEEN_MINUTES = '15m'  # 15-minute interval
    THIRTY_MINUTES = '30m'  # 30-minute interval
    SIXTY_MINUTES = '60m'  # 60-minute interval
    NINETY_MINUTES = '90m'  # 90-minute interval
    ONE_HOUR = '1h'  # 1-hour interval
    ONE_DAY = '1d'  # 1-day interval
    FIVE_DAYS = '5d'  # 5-day interval
    ONE_WEEK = '1wk'  # 1-week interval
    ONE_MONTH = '1mo'  # 1-month interval
    THREE_MONTHS = '3mo'  # 3-month interval
