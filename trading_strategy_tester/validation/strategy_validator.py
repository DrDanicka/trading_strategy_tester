import ast
from datetime import datetime

from trading_strategy_tester.validation.parameter_validations.capital_validator import validate_initial_capital
from trading_strategy_tester.validation.parameter_validations.order_size_validator import validate_order_size
from trading_strategy_tester.validation.parameter_validations.ticker_validator import validate_ticker
from trading_strategy_tester.validation.parameter_validations.position_type_validator import validate_position_type
from trading_strategy_tester.validation.parameter_validations.date_validator import validate_date
from trading_strategy_tester.validation.parameter_validations.stop_loss_validator import validate_stop_loss
from trading_strategy_tester.validation.parameter_validations.take_profit_validator import validate_take_profit
from trading_strategy_tester.validation.parameter_validations.interval_validator import validate_interval
from trading_strategy_tester.validation.parameter_validations.period_validator import validate_period
from trading_strategy_tester.validation.parameter_validations.trade_commissions_validator import validate_trade_commissions
from trading_strategy_tester.validation.parameter_validations.condition_validator import validate_condition

def validate_strategy_string(strategy_str: str, logs: bool = False) -> (bool, str):
    """
    Validate a strategy string that initializes a `Strategy` object.

    The function:
    - Parses the input string into an Abstract Syntax Tree (AST),
    - Checks for disallowed functions for security,
    - Validates each parameter individually,
    - Corrects invalid values with defaults when needed,
    - Deletes invalid parameters,
    - Ensures required parameters exist,
    - Returns a corrected string version of the strategy.

    :param strategy_str: The strategy definition as a string.
    :param logs: If True, print validation logs.
    :return: Tuple (success_flag, validated_strategy_str_or_error_message, changes_dict).
    """
    changes = dict()
    message = ''
    invalid_parameters = []
    valid_parameters = []
    global_ticker = 'AAPL'

    _DISALLOWED_FUNCTIONS = {
        'exec', 'eval', 'os', 'sys', 'import', 'open', '__import__', 'compile'
    }

    try:
        # Parse the input strategy into AST
        parsed_strategy = ast.parse(strategy_str)

        # Walk through the AST to check for disallowed functions
        for node in ast.walk(parsed_strategy):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in _DISALLOWED_FUNCTIONS:
                    if logs:
                        print(f"Disallowed function '{node.func.id}' found in strategy string.")
                    message = f"Disallowed function '{node.func.id}' found in strategy string."
                    raise Exception(message)

        strategy_object = parsed_strategy.body[0].value

        # Check if the AST represents a Strategy object
        if isinstance(strategy_object, ast.Call) and isinstance(strategy_object.func, ast.Name):
            if strategy_object.func.id != 'Strategy':
                if logs:
                    print("The strategy string must initialize a Strategy object.")
                message = "The strategy string must initialize a Strategy object."
                raise Exception(message)

        # Validate each keyword argument in the Strategy
        for kwarg in strategy_object.keywords:
            if kwarg.arg == 'ticker':
                validation_result, ticker, changes = validate_ticker(kwarg.value, changes, logs)
                if not validation_result:
                    kwarg.value = ast.Constant(value=ticker)
                else:
                    global_ticker = ticker

            elif kwarg.arg == 'position_type':
                validation_result, position_type, changes = validate_position_type(kwarg.value, changes, logs)
                if not validation_result:
                    kwarg.value = ast.Attribute(
                        value=ast.Name(id='PositionTypeEnum', ctx=ast.Load()),
                        attr=position_type.value,
                        ctx=ast.Load()
                    )

            elif kwarg.arg == 'buy_condition':
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=True, global_ticker=global_ticker)
                if validation_result:
                    kwarg.value = condition
                else:
                    message = 'Error in buy condition'
                    raise Exception(message)

            elif kwarg.arg == 'sell_condition':
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=False, global_ticker=global_ticker)
                if validation_result:
                    kwarg.value = condition
                else:
                    message = 'Error in sell condition'
                    raise Exception(message)

            elif kwarg.arg in ['start_date', 'end_date']:
                validation_result, date, changes = validate_date(kwarg.value, changes, logs, start=(kwarg.arg == 'start_date'))
                if not validation_result:
                    kwarg.value = ast.Call(
                        func=ast.Name(id='datetime', ctx=ast.Load()),
                        args=[
                            ast.Constant(value=date.year),
                            ast.Constant(value=date.month),
                            ast.Constant(value=date.day),
                        ],
                        keywords=[]
                    )

            elif kwarg.arg == 'stop_loss':
                if type(kwarg.value) is not ast.Constant:
                    validation_result, stop_loss, changes = validate_stop_loss(kwarg.value, changes, logs)
                    if not validation_result:
                        kwarg.value = ast.Constant(value=stop_loss)

            elif kwarg.arg == 'take_profit':
                if type(kwarg.value) is not ast.Constant:
                    validation_result, take_profit, changes = validate_take_profit(kwarg.value, changes, logs)
                    if not validation_result:
                        kwarg.value = ast.Constant(value=take_profit)

            elif kwarg.arg == 'interval':
                validation_result, interval, changes = validate_interval(kwarg.value, changes, logs)
                if not validation_result:
                    kwarg.value = ast.Attribute(
                        value=ast.Name(id='Interval', ctx=ast.Load()),
                        attr='ONE_DAY',
                        ctx=ast.Load()
                    )

            elif kwarg.arg == 'period':
                validation_result, period, changes = validate_period(kwarg.value, changes, logs)
                if not validation_result:
                    kwarg.value = ast.Attribute(
                        value=ast.Name(id='Period', ctx=ast.Load()),
                        attr='NOT_PASSED',
                        ctx=ast.Load()
                    )

            elif kwarg.arg == 'initial_capital':
                validation_result, initial_capital, changes = validate_initial_capital(kwarg.value, changes, logs)
                if not validation_result:
                    kwarg.value = ast.Constant(value=initial_capital)

            elif kwarg.arg == 'order_size':
                validation_result, order_size, changes = validate_order_size(kwarg.value, changes, logs)
                if not validation_result:
                    kwarg.value = ast.Call(
                        func=ast.Name(id='Contracts', ctx=ast.Load()),
                        args=[ast.Constant(value=1)],
                        keywords=[]
                    )

            elif kwarg.arg == 'trade_commissions':
                validation_result, trade_commission, changes = validate_trade_commissions(kwarg.value, changes, logs)
                if not validation_result:
                    kwarg.value = ast.Call(
                        func=ast.Name(id='MoneyCommissions', ctx=ast.Load()),
                        args=[ast.Constant(value=0)],
                        keywords=[]
                    )

            else:
                invalid_parameters.append(kwarg.arg)

            # Track used parameters
            if kwarg.arg not in invalid_parameters:
                if kwarg.arg not in valid_parameters:
                    valid_parameters.append(kwarg.arg)
                else:
                    message = f"Parameter '{kwarg.arg}' used twice."
                    raise Exception(message)

        # Remove invalid parameters
        if len(invalid_parameters) != 0:
            message = f"The following parameters are invalid: {', '.join(invalid_parameters)}. Using strategy without these parameters."
            strategy_object = parsed_strategy.body[0].value.keywords
            valid_keywords = [kwarg for kwarg in strategy_object if kwarg.arg not in invalid_parameters]
            parsed_strategy.body[0].value.keywords = valid_keywords
            changes['strategy'] = message

        # Ensure mandatory fields are present
        mandatory_parameters = ['ticker', 'position_type', 'buy_condition', 'sell_condition']

        for mandatory_parameter in mandatory_parameters:
            if mandatory_parameter not in valid_parameters:
                if mandatory_parameter == 'ticker':
                    parsed_strategy.body[0].value.keywords.append(
                        ast.keyword(
                            arg=mandatory_parameter,
                            value=ast.Constant(value='AAPL')
                        )
                    )
                    changes['strategy'] = 'No ticker specified. Defaulting to AAPL ticker.'
                elif mandatory_parameter == 'position_type':
                    parsed_strategy.body[0].value.keywords.append(
                        ast.keyword(
                            arg=mandatory_parameter,
                            value=ast.Attribute(
                                value=ast.Name(id='PositionTypeEnum', ctx=ast.Load()),
                                attr='LONG',
                                ctx=ast.Load()
                            )
                        )
                    )
                    changes['strategy'] = 'No position type specified. Defaulting to long positions.'
                else:
                    raise Exception('Missing mandatory buy or sell condition parameter.')

        wrong_date = False

        # Check if start_date and end_date are present
        if 'start_date' in valid_parameters and 'end_date' in valid_parameters:
            start_date_args = next((kwarg for kwarg in strategy_object.keywords if kwarg.arg == 'start_date'), None).value.args
            end_date_args = next((kwarg for kwarg in strategy_object.keywords if kwarg.arg == 'end_date'), None).value.args

            start_date = datetime(year=start_date_args[0].value, month=start_date_args[1].value, day=start_date_args[2].value)
            end_date = datetime(year=end_date_args[0].value, month=end_date_args[1].value, day=end_date_args[2].value)

            if start_date and end_date:
                if start_date > end_date:
                    wrong_date = True

        # Check in only end_date is present
        if 'end_date' in valid_parameters and 'start_date' not in valid_parameters:
            end_date_args = next((kwarg for kwarg in strategy_object.keywords if kwarg.arg == 'end_date'), None).value.args
            end_date = datetime(year=end_date_args[0].value, month=end_date_args[1].value, day=end_date_args[2].value)

            # Compare end_date with January 1, 2024 (default for strategy)
            default_date = datetime(2024, 1, 1)

            if end_date < default_date:
                wrong_date = True

        if wrong_date:
            changes['date'] = "Start date cannot be after end date. Setting end date to today and keeping start date as is."

            for kwarg in strategy_object.keywords:
                if kwarg.arg == 'start_date':
                    start_date = datetime(2024, 1, 1)
                    kwarg.value = ast.Call(
                        func=ast.Name(id='datetime', ctx=ast.Load()),
                        args=[
                            ast.Constant(value=start_date.year),
                            ast.Constant(value=start_date.month),
                            ast.Constant(value=start_date.day),
                        ],
                        keywords=[]
                    )
                elif kwarg.arg == 'end_date':
                    current_date = datetime.today()
                    kwarg.value = ast.Call(
                        func=ast.Name(id='datetime', ctx=ast.Load()),
                        args=[
                            ast.Constant(value=current_date.year),
                            ast.Constant(value=current_date.month),
                            ast.Constant(value=current_date.day),
                        ],
                        keywords=[]
                    )


    except Exception as e:
        if message == '':
            message = f"Error parsing strategy string: {e}"

        if logs:
            print(f"Error parsing strategy string: {e}")

        changes['strategy'] = message

        return False, '', changes

    return True, ast.unparse(parsed_strategy), changes
