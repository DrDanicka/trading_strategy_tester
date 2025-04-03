def validate_stop_loss(stop_loss, changes: dict, logs: bool) -> (bool, str, dict):
    """
        Validates the stop loss parameter to ensure it is of the correct type and has the necessary attributes.
        If the validation fails, it defaults to no stop loss and logs an error message.

        :param stop_loss: The stop loss object to be validated. This is expected to be an AST `Call` node representing a `StopLoss`.
        :type stop_loss: ast.Call
        :param changes: A dictionary to store any changes or messages made during validation.
        :type changes: dict
        :param logs: A boolean indicating whether to log messages when validation fails.
        :type logs: bool
        :return: A tuple containing a boolean indicating validity, a message, and the updated `changes` dictionary.
        :rtype: (bool, str, dict)

        The function ensures:
        1. The `stop_loss` argument is of type `StopLoss`.
        2. The `stop_loss` object has a valid `percentage` and `stop_loss_type` attributes.
        3. The `stop_loss_type` must be of type `StopLossType`, and its value must be either `'NORMAL'` or `'TRAILING'`.
        4. The `percentage` value should be a numeric type (int or float).
        5. If validation fails, it defaults to no stop loss (`None`) and logs an error message.
        """

    default_stop_loss = None
    message = f"stop_loss argument should be of type StopLoss with percentage and stop_loss_type arguments. Defaulting to no stop loss."
    not_valid = False

    try:
        stop_loss_type = stop_loss.func.id

        if stop_loss_type == 'StopLoss':
            param1 = stop_loss.keywords[0]
            param2 = stop_loss.keywords[1]

            if param1.arg == 'percentage':
                stop_loss_percentage = param1.value
            elif param2.arg == 'percentage':
                stop_loss_percentage = param2.value
            else:
                message = f"stop_loss argument percentage is missing. Defaulting to no stop loss."
                raise Exception("percentage not found")

            if param1.arg == 'stop_loss_type':
                stop_loss_type = param1.value
            elif param2.arg == 'stop_loss_type':
                stop_loss_type = param2.value
            else:
                message = f"stop_loss argument stop_loss_type is missing. Defaulting to no stop loss."
                raise Exception("stop_loss_type not found")

            if stop_loss_type.value.id != 'StopLossType':
                message = f"stop_loss argument stop_loss_type should be of type StopLossType. Defaulting to no stop loss."
                raise Exception("stop_loss_type not found")

            if stop_loss_type.attr not in ['NORMAL', 'TRAILING']:
                message = f"Valid stop_loss_types are: 'NORMAL', 'TRAILING'. Defaulting to no stop loss."
                raise Exception("stop_loss_type not found")

            # Check stop_loss_percentage.value is float
            if not isinstance(stop_loss_percentage.value, (int, float)):
                message = f"stop_loss argument percentage should be a number. Defaulting to no stop loss."
                raise Exception("percentage not found")
        else:
            not_valid = True

    except Exception:
        not_valid = True

    if not_valid:
        if logs:
            print(message)

        changes['stop_loss'] = message

        return False, default_stop_loss, changes

    return True, None, changes