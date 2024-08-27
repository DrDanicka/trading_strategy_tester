from enum import Enum

class Period(Enum):
    """
    Period is an enumeration that represents various time periods for which data can be aggregated
    or analyzed. This is often used in financial data analysis to specify the period of interest.

    Attributes:
    ----------
    ONE_DAY : str
        Represents a 1-day period ('1d').
    FIVE_DAYS : str
        Represents a 5-day period ('5d').
    ONE_MONTH : str
        Represents a 1-month period ('1mo').
    THREE_MONTHS : str
        Represents a 3-month period ('3mo').
    SIX_MONTHS : str
        Represents a 6-month period ('6mo').
    ONE_YEAR : str
        Represents a 1-year period ('1y').
    TWO_YEARS : str
        Represents a 2-year period ('2y').
    FIVE_YEARS : str
        Represents a 5-year period ('5y').
    TEN_YEARS : str
        Represents a 10-year period ('10y').
    YEAR_TO_DATE : str
        Represents the year-to-date period ('ytd').
    MAX : str
        Represents the maximum available period ('max').
    NOT_PASSED : str
        Represents a special case indicating that a period has not been passed ('not_passed').
    """

    ONE_DAY = '1d'          # 1-day period
    FIVE_DAYS = '5d'        # 5-day period
    ONE_MONTH = '1mo'       # 1-month period
    THREE_MONTHS = '3mo'    # 3-month period
    SIX_MONTHS = '6mo'      # 6-month period
    ONE_YEAR = '1y'         # 1-year period
    TWO_YEARS = '2y'        # 2-year period
    FIVE_YEARS = '5y'       # 5-year period
    TEN_YEARS = '10y'       # 10-year period
    YEAR_TO_DATE = 'ytd'    # Year-to-date period
    MAX = 'max'             # Maximum available period
    NOT_PASSED = 'not_passed'  # Indicates that a period has not been passed
