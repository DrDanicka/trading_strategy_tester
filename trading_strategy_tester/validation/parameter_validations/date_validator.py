from datetime import datetime

def validate_date(date, changes: dict, logs: bool, start: bool) -> (bool, str, dict):
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