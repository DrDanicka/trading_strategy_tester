import ast
import pandas as pd

from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum

implemented_conditions = pd.DataFrame(
    data=[
        ['DowntrendFibRetracementLevelCondition', 'fib_level:FibonacciLevels length:int'],
        ['UptrendFibRetracementLevelCondition', 'fib_level:FibonacciLevels length:int'],
        ['AND', '*conditions:Condition'],
        ['OR', '*conditions:Condition'],
        ['AfterXDaysCondition', 'condition:Condition number_of_days:int'],
        ['ChangeOfXPercentPerYDaysCondition', 'series:TradingSeries percent:float number_of_days:int'],
        ['IntraIntervalChangeOfXPercentCondition', 'series:TradingSeries percent:float'],
        ['CrossOverCondition', 'first_series:TradingSeries second_series:TradingSeries'],
        ['CrossUnderCondition', 'first_series:TradingSeries second_series:TradingSeries'],
        ['GreaterThanCondition', 'first_series:TradingSeries second_series:TradingSeries'],
        ['LessThanCondition', 'first_series:TradingSeries second_series:TradingSeries'],
        ['DowntrendForXDaysCondition', 'series:TradingSeries number_of_days:int'],
        ['UptrendForXDaysCondition', 'series:TradingSeries number_of_days:int']
    ],
    columns=['Class_name', 'Parameters']
)

implemented_trading_series = pd.DataFrame(
    data=[['ADX', 'ticker:str adx_smoothing:int length:int'],
          ['AROON_DOWN', 'ticker:str, length:int'],
          ['AROON_UP', 'ticker:str, length:int'],
          ['ATR', 'ticker:str length:int smoothing:SmoothingType'],
          ['BB_LOWER', 'ticker:str source:SourceType length:int ma_type:SmoothingType std_dev:float offset:int'],
          ['BB_MIDDLE', 'ticker:str source:SourceType length:int ma_type:SmoothingType std_dev:float offset:int'],
          ['BB_UPPER', 'ticker:str source:SourceType length:int ma_type:SmoothingType std_dev:float offset:int'],
          ['BBP', 'ticker:str length:int'],
          ['CCI', 'ticker:str source:SourceType length:int'],
          ['CCI_SMOOTHENED', 'ticker:str source:SourceType length:int smoothing_type:SmoothingType smoothing_length:int'],
          ['CHAIKIN_OSC', 'ticker:str fast_length:int slow_length:int'],
          ['CHOP', 'ticker:str length:int offset:int'],
          ['CMF', 'ticker:str length:int'],
          ['CMO', 'ticker:str source:SourceType length:int'],
          ['COPPOCK', 'ticker:str length:int long_roc_length:int short_roc_length:int'],
          ['DC_BASIS', 'ticker:str length:int offset:int'],
          ['DC_UPPER', 'ticker:str length:int offset:int'],
          ['DC_LOWER', 'ticker:str length:int offset:int'],
          ['CLOSE', 'ticker:str'],
          ['CONST', 'const_number:int'],
          ['HIGH', 'ticker:str'],
          ['LOW', 'ticker:str'],
          ['OPEN', 'ticker:str'],
          ['VOLUME', 'ticker:str'],
          ['DI_MINUS', 'ticker:str length:int'],
          ['DI_PLUS', 'ticker:str length:int'],
          ['DPO', 'ticker:str length:int'],
          ['EFI', 'ticker:str length:int'],
          ['EOM', 'ticker:str length:int divisor:int'],
          ['HAMMER', 'ticker:str'],
          ['ICHIMOKU_BASE', 'ticker:str length:int'],
          ['ICHIMOKU_CONVERSION', 'ticker:str length:int'],
          ['ICHIMOKU_LEADING_SPAN_A', 'ticker:str displacement:int'],
          ['ICHIMOKU_LAGGING_SPAN', 'ticker:str displacement:int'],
          ['ICHIMOKU_LEADING_SPAN_B', 'ticker:str length:int displacement:int'],
          ['KC_LOWER', 'ticker:str source:SourceType length:int multiplier:int use_exp_ma:bool atr_length:int'],
          ['KC_UPPER', 'ticker:str source:SourceType length:int multiplier:int use_exp_ma:bool atr_length:int'],
          ['KST', 'ticker:str source:SourceType roc_length_1:int roc_length_2:int roc_length_3:int roc_length_4:int sma_length_1:int sma_length_2:int sma_length_3:int sma_length_4:int'],
          ['KST_SIGNAL', 'ticker:str source:SourceType roc_length_1:int roc_length_2:int roc_length_3:int roc_length_4:int sma_length_1:int sma_length_2:int sma_length_3:int sma_length_4:int signal_length:int'],
          ['EMA', 'ticker:str source:SourceType length:int offset:int'],
          ['SMA', 'ticker:str source:SourceType length:int offset:int'],
          ['MACD', 'ticker:str source:SourceType fast_length:int slow_length:int ma_type:SmoothingType'],
          ['MACD_SIGNAL', 'ticker:str source:SourceType fast_length:int slow_length:int oscillator_ma_type:SmoothingType signal_ma_type:SmoothingType signal_length:int'],
          ['MASS_INDEX', 'ticker:str length:int'],
          ['MFI', 'ticker:str length:int'],
          ['MOMENTUM', 'ticker:str source:SourceType length:int'],
          ['OBV', 'ticker:str'],
          ['PVI', 'ticker:str'],
          ['PVT', 'ticker:str'],
          ['ROC', 'ticker:str source:SourceType length:int'],
          ['RSI', 'ticker:str source:SourceType length:int'],
          ['STOCH_PERCENT_D', 'ticker:str length:int d_smooth_length:int'],
          ['STOCH_PERCENT_K', 'ticker:str length:int'],
          ['TRIX', 'ticker:str length:int'],
          ['UO', 'ticker:str fast_length:int middle_length:int slow_length:int'],
          ['WILLR', 'ticker:str source:SourceType length:int'],
          ],
    columns=['Class_name', 'Parameters']
)


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

        return False, default_ticker, changes

    return True, None, changes


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


def validate_condition(condition, changes: dict, logs: bool, buy: bool) -> (bool, str, dict):
    print(ast.dump(condition))
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

                # If the position type is not valid, set it to the default position type
                if not validation_result:
                    kwarg.value = ast.Attribute(
                        value= ast.Name(id='PositionTypeEnum', ctx=ast.Load()),
                        attr= position_type.value,
                        ctx=ast.Load()
                    )
            if kwarg.arg == 'buy_condition':
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=True)

                # If the buy condition is not valid, set it to the default buy condition
                if not validation_result:
                    kwarg.value = ast.Constant(value=condition)

            if kwarg.arg == 'sell_condition':
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=False)

                # If the sell condition is not valid, set it to the default sell condition
                if not validation_result:
                    kwarg.value = ast.Constant(value=condition)




    except Exception as e:
        print(f"Error parsing strategy string: {e}")
        return False


    return True, 'xd'


validate_strategy_string("Strategy(ticker='TSLA', position_type=PositionTypeEnum.LONG, buy_condition=OR( CrossOverCondition(first_series=RSI('TSLA'), second_series=CONST(30)), LessThanCondition(first_series=EMA('TSLA'), second_series=CLOSE('TSLA'))), sell_condition=OR( CrossOverCondition(first_series=CONST(70), second_series=RSI('TSLA')), IntraIntervalChangeOfXPercentCondition(series=CLOSE('TSLA'), percent=5)), stop_loss=StopLoss(percentage=5, stop_loss_type=StopLossType.NORMAL), take_profit=TakeProfit(percentage=10), start_date=datetime(2020, 1, 1), end_date=datetime(2024, 1, 1), initial_capital=1000)")
