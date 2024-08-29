from trading_strategy_tester.enums.source_enum import SourceType

def get_length(length: int, default: int) -> int:
    """
    Validates and returns a positive integer length.

    Checks if the provided `length` is a positive integer. If not, it returns the specified default value.

    :param length: Number representing the desired length.
    :type length: int
    :param default: Default value to use if `length` is not a positive integer.
    :type default: int
    :return: Validated length as a positive integer or the default value.
    :rtype: int
    """
    return int(length) if isinstance(length, int) and length > 0 else default

def get_offset(offset: int) -> int:
    """
    Validates and returns a non-negative integer offset.

    Checks if the provided `offset` is a non-negative integer. If not, it returns 0.

    :param offset: Number representing the offset.
    :type offset: int
    :return: Validated offset as a non-negative integer or 0.
    :rtype: int
    """
    return int(offset) if isinstance(offset, int) and offset >= 0 else 0

def get_std_dev(std_dev: float, default: float) -> float:
    """
    Validates and returns a positive standard deviation value.

    Checks if the provided `std_dev` is a positive float. If not, it returns the specified default value.

    :param std_dev: Number representing the standard deviation.
    :type std_dev: float
    :param default: Default value to use if `std_dev` is not positive.
    :type default: float
    :return: Validated standard deviation as a positive float or the default value.
    :rtype: float
    """
    return float(std_dev) if std_dev > 0 else default

def get_base_sources(source: SourceType, default: SourceType) -> SourceType:
    """
    Validates and returns a base source type for financial data.

    Ensures that the provided `source` is a valid base source (e.g., 'CLOSE', 'OPEN', 'HIGH', 'LOW').
    If the source is not valid, it returns the specified default source.

    :param source: The source type to validate.
    :type source: SourceType
    :param default: The default source type to return if the provided `source` is invalid.
    :type default: SourceType
    :return: Validated source type or the default value.
    :rtype: SourceType
    """
    return source if source in [
        SourceType.CLOSE,
        SourceType.OPEN,
        SourceType.HIGH,
        SourceType.LOW,
    ] else default
