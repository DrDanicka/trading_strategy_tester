
def get_length(length: int, default: int) -> int:
    """
    Parameters:
    -----------
    length: int
        Number representing the length.
    default: int
        Default value for the length.

    Returns:
    --------
    int
        Returns given number or zero as default.
    """
    return int(length) if isinstance(length, int) and length > 0 else default

def get_offset(offset: int) -> int:
    """
    Parameters:
    -----------
    offset: int
        Number representing offset.

    Returns:
    --------
    int
        Returns given number or zero as default.
    """
    return int(offset) if isinstance(offset, int) and offset >= 0 else 0

def get_std_dev(std_dev: float, default: float) -> float:
    """
    Parameters:
    -----------
    std_dev: float
        Number representing the std_dev.
    default: float
        Default value for the std_dev.

    Returns:
    --------
    float
        Returns given number or zero as default.
    """
    return float(std_dev) if std_dev > 0 else default