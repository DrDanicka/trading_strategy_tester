from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum

def validate_position_type(position_type, changes: dict, logs: bool) -> (bool, str, dict):
    """
    Validate the position type parameter.

    This function checks whether the `position_type` argument is correctly defined as a member
    of the `PositionTypeEnum`. If not valid, it logs an appropriate message (if logs=True),
    updates the `changes` dictionary with the error, and falls back to a default value (`LONG`).

    :param position_type: The AST node representing the position type.
    :param changes: A dictionary to store any changes or error messages.
    :param logs: A boolean flag to control logging output.
    :return: A tuple (validation_success, new_value_or_None, updated_changes).
             If valid, new_value_or_None is None.
             If invalid, new_value_or_None is the default `PositionTypeEnum.LONG`.
    """
    default_position_type = PositionTypeEnum.LONG
    not_valid = False
    message = f"position_type argument should be of type PositionTypeEnum. Using default position type '{default_position_type}'."

    try:
        # Extract the enum type name from AST
        pos_type_enum = position_type.value.id

        # Check if the type is exactly PositionTypeEnum
        if pos_type_enum != 'PositionTypeEnum':
            raise Exception(message)

        # Check if the attribute is a valid member of PositionTypeEnum
        pos_type_attr = position_type.attr

        if pos_type_attr not in PositionTypeEnum.__dict__.keys():
            message = f"Valid PositionTypeEnums are: 'LONG', 'SHORT', 'LONG_SHORT_COMBINATION'. Using default position type '{default_position_type}'."
            raise Exception(message)

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        # Log the change/error
        changes['position_type'] = message

        return False, default_position_type, changes

    return True, None, changes
