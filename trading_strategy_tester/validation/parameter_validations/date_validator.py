from datetime import datetime

def validate_date(date, changes: dict, logs: bool, start: bool=False) -> (bool, str, dict):
    """
    Validates the date parameter. Ensures that the date is of type datetime and that it is not a future date.

    :param date: The date to be validated. This is expected to be an AST node representing a function call to `datetime`.
    :type date: ast.Call
    :param changes: A dictionary to store any changes or messages made during validation.
    :type changes: dict
    :param logs: A boolean indicating whether to log messages.
    :type logs: bool
    :param start: A boolean indicating whether the date is the start date (`True`) or the end date (`False`).
    :type start: bool
    :return: A tuple containing a boolean indicating validity, a message, and the updated `changes` dictionary.
    :rtype: (bool, str, dict)

    The function ensures:
    1. The `date` parameter is a valid `datetime` object.
    2. The date is not in the future.
    3. If validation fails, it uses a default date and logs an error message.
    """

    if start:
        default_date = datetime(2024, 1, 1)
    else:
        default_date = datetime.today()
    message = f"Date argument should be of type datetime. Using default date '{default_date.strftime('%Y-%m-%d')}'."
    not_valid = False

    try:
        str_datetime = date.func.id

        if str_datetime != 'datetime':
            raise Exception(message)

        year, month, day = [i.value for i in date.args]

        passed_date = datetime(year, month, day)
        if passed_date > datetime.today():
            message = f"Date argument should be a date in the past. Using default date '{default_date.strftime('%Y-%m-%d')}'."
            raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['start_date' if start else 'end_date'] = message

        return False, default_date, changes

    return True, None, changes