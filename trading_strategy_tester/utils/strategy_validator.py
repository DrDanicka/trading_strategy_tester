import ast

from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum


def validate_ticker(ticker, changes: dict, logs: bool) -> (bool, str, dict):
    default_ticker = 'AAPL'
    not_valid = False
    message = f"ticker argument should be a string. Using default ticker '{default_ticker}'."

    # Gets the ticker value from the ticker parameter
    try:
        str_ticker = ticker.value
    except Exception:
        not_valid = True

    if not not_valid and not isinstance(str_ticker, str):
        not_valid = True

    # TODO check if string is actual ticker in some database of valid tickers

    if not_valid:
        if logs:
            print(message)

        changes['ticker'] = message

        # Defaults to the default ticker
        return False, default_ticker, changes

    return True, None, changes


def validate_position_type(position_type, changes: dict, logs: bool) -> (bool, str, dict):
    default_position_type = PositionTypeEnum.LONG

    print(position_type.attr)
    print(position_type.value.id)

    return True, None, changes

def validate_strategy_string(strategy_str: str, logs: bool = False) -> (bool, str):
    changes = dict()

    _DISALLOWED_FUNCTIONS = {
        'exec',
        'eval',
        'os',
        'sys',
        'import',
        'open',
        '__import__',
        'compile'
    }

    try:
        parsed_strategy = ast.parse(strategy_str)

        # Check for disallowed functions
        for node in ast.walk(parsed_strategy):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in _DISALLOWED_FUNCTIONS:
                    print(f"Disallowed function '{node.func.id}' found in strategy string.")
                    return False

        call = parsed_strategy.body[0].value

        # Check if valid Strategy object initialization
        if isinstance(parsed_strategy.body[0], ast.Expr):
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name):
                if call.func.id != 'Strategy':
                    print("The strategy string must initialize a Strategy object.")
                    return False

        # Validate the arguments
        for kwarg in call.keywords:
            if kwarg.arg == 'ticker':
                validation_result, ticker, changes = validate_ticker(kwarg.value, changes, logs)

                # If the ticker is not valid, set it to the default ticker
                if not validation_result:
                    kwarg.value = ast.Constant(value=ticker)
            if kwarg.arg == 'position_type':
                validation_result, position_type, changes = validate_position_type(kwarg.value, changes, logs)




    except Exception as e:
        print(f"Error parsing strategy string: {e}")
        return False


    return True, 'xd'


validate_strategy_string("Strategy(ticker='TSLA', position_type=PositionTypeEnum.LONG, buy_condition=OR( CrossOverCondition(first_series=RSI('TSLA'), second_series=CONST(30)), LessThanCondition(first_series=EMA('TSLA'), second_series=CLOSE('TSLA'))), sell_condition=OR( CrossOverCondition(first_series=CONST(70), second_series=RSI('TSLA')), IntraIntervalChangeOfXPercentCondition(series=CLOSE('TSLA'), percent=5)), stop_loss=StopLoss(percentage=5, stop_loss_type=StopLossType.NORMAL), take_profit=TakeProfit(percentage=10), start_date=datetime(2020, 1, 1), end_date=datetime(2024, 1, 1), initial_capital=1000)")
