def validate_ticker(ticker, changes: dict, logs: bool) -> (bool, str, dict):
    default_ticker = 'AAPL'
    not_valid = False
    message = f"ticker argument should be a string. Using default ticker '{default_ticker}'."

    # Gets the ticker value from the ticker parameter
    try:
        str_ticker = ticker.value

        if not isinstance(str_ticker, str):
            raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['ticker'] = message

        return False, default_ticker, changes

    return True, None, changes