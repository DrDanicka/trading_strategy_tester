from enum import Enum


class Interval(Enum):
    """
    Interval is an enumeration that represents various time intervals commonly used in data analysis,
    particularly in the context of financial data or time series data.

    Attributes:
    ----------
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

    ONE_DAY = '1d'  # 1-day interval
    FIVE_DAYS = '5d'  # 5-day interval
    ONE_WEEK = '1wk'  # 1-week interval
    ONE_MONTH = '1mo'  # 1-month interval
    THREE_MONTHS = '3mo'  # 3-month interval
