from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum

def validate_position_type(position_type, changes: dict, logs: bool) -> (bool, str, dict):
    default_position_type = PositionTypeEnum.LONG
    not_valid = False
    message = f"position_type argument should be of type PositionTypeEnum. Using default position type '{default_position_type}'."

    try:
        pos_type_enum = position_type.value.id
        pos_type_attr = position_type.attr
    except Exception:
        not_valid = True

    if not not_valid:
        if pos_type_enum != 'PositionTypeEnum':
            not_valid = True
        elif pos_type_attr not in PositionTypeEnum.__dict__.keys():
            message = f"Valid PositionTypeEnums are: 'LONG', 'SHORT', 'LONG_SHORT_COMBINATION'. Using default position type '{default_position_type}'."
            not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['position_type'] = message

        return False, default_position_type, changes

    return True, None, changes