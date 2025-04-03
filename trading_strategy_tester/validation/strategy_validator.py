import ast

from trading_strategy_tester.validation.parameter_validations.capital_validator import validate_initial_capital
from trading_strategy_tester.validation.parameter_validations.order_size_validator import validate_order_size
from trading_strategy_tester.validation.parameter_validations.ticker_validator import validate_ticker
from trading_strategy_tester.validation.parameter_validations.position_type_validator import validate_position_type
from trading_strategy_tester.validation.parameter_validations.date_validator import validate_date
from trading_strategy_tester.validation.parameter_validations.stop_loss_validator import validate_stop_loss
from trading_strategy_tester.validation.parameter_validations.take_profit_validator import validate_take_profit
from trading_strategy_tester.validation.parameter_validations.interval_validator import validate_interval
from trading_strategy_tester.validation.parameter_validations.period_validator import validate_period
from trading_strategy_tester.validation.parameter_validations.trade_commissions_validator import \
    validate_trade_commissions
from trading_strategy_tester.validation.parameter_validations.condition_validator import validate_condition

def validate_strategy_string(strategy_str: str, logs: bool = False) -> (bool, str):
    changes = dict()
    message = ''
    invalid_parameters = []
    valid_parameters = []

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
        # Create Abstract Syntax Tree from Strategy object
        parsed_strategy = ast.parse(strategy_str)

        # Check for disallowed functions that may be malicious
        for node in ast.walk(parsed_strategy):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in _DISALLOWED_FUNCTIONS:
                    if logs:
                        print(f"Disallowed function '{node.func.id}' found in strategy string.")

                    message = f"Disallowed function '{node.func.id}' found in strategy string."

                    raise Exception(message)

        strategy_object = parsed_strategy.body[0].value

        # Check if valid Strategy object initialization
        if isinstance(strategy_object, ast.Call) and isinstance(strategy_object.func, ast.Name):
            if strategy_object.func.id != 'Strategy':
                if logs:
                    print("The strategy string must initialize a Strategy object.")

                message = f"The strategy string must initialize a Strategy object."

                raise Exception(message)

        print(ast.dump(strategy_object))

        # Validate the arguments
        for kwarg in strategy_object.keywords:
            if kwarg.arg == 'ticker':
                validation_result, ticker, changes = validate_ticker(kwarg.value, changes, logs)

                # If the ticker is not valid, set it to the default ticker
                if not validation_result:
                    kwarg.value = ast.Constant(value=ticker)
            elif kwarg.arg == 'position_type':
                validation_result, position_type, changes = validate_position_type(kwarg.value, changes, logs)

                # If the position type is not valid, set it to the default position type
                if not validation_result:
                    kwarg.value = ast.Attribute(
                        value= ast.Name(id='PositionTypeEnum', ctx=ast.Load()),
                        attr= position_type.value,
                        ctx=ast.Load()
                    )
            elif kwarg.arg == 'buy_condition':
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=True)

                # If the buy condition is not valid, set it to the default buy condition
                if not validation_result:
                    kwarg.value = ast.Constant(value=condition)

            elif kwarg.arg == 'sell_condition':
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=False)

                # If the sell condition is not valid, set it to the default sell condition
                if not validation_result:
                    kwarg.value = ast.Constant(value=condition)

            elif kwarg.arg in ['start_date', 'end_date']:
                validation_result, date, changes = validate_date(kwarg.value, changes, logs, start=True if kwarg.arg == 'start_date' else False)

                # If the date is not valid, set it to the default date
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
                # If it's not None
                if type(kwarg.value) is not ast.Constant:
                    validation_result, stop_loss, changes = validate_stop_loss(kwarg.value, changes, logs)

                    # If the stop loss is not valid, set it to the default stop loss (None)
                    if not validation_result:
                        kwarg.value = ast.Constant(value=stop_loss)

            elif kwarg.arg == 'take_profit':
                # If it's not None
                if type(kwarg.value) is not ast.Constant:
                    validation_result, take_profit, changes = validate_take_profit(kwarg.value, changes, logs)

                    # If the take profit is not valid, set it to the default take profit (None)
                    if not validation_result:
                        kwarg.value = ast.Constant(value=take_profit)

            elif kwarg.arg == 'interval':
                validation_result, interval, changes = validate_interval(kwarg.value, changes, logs)

                # If the interval is not valid, set it to the default interval
                if not validation_result:
                    kwarg.value = ast.Attribute(
                        value=ast.Name(id='Interval', ctx=ast.Load()),
                        attr='ONE_DAY',
                        ctx=ast.Load()
                    )

            elif kwarg.arg == 'period':
                validation_result, period, changes = validate_period(kwarg.value, changes, logs)

                # If the period is not valid, set it to the default period
                if not validation_result:
                    kwarg.value = ast.Attribute(
                        value=ast.Name(id='Period', ctx=ast.Load()),
                        attr='NOT_PASSED',
                        ctx=ast.Load()
                    )

            elif kwarg.arg == 'initial_capital':
                validation_result, initial_capital, changes = validate_initial_capital(kwarg.value, changes, logs)

                # If the initial capital is not valid, set to default
                if not validation_result:
                    kwarg.value = ast.Constant(value=initial_capital)

            elif kwarg.arg == 'order_size':
                validation_result, order_size, changes = validate_order_size(kwarg.value, changes, logs)

                # If the order size is not valid, set to default
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

            if kwarg.arg not in invalid_parameters:
                if kwarg.arg not in valid_parameters:
                    valid_parameters.append(kwarg.arg)
                else:
                    message = f"Parameter '{kwarg.arg}' used twice."
                    raise Exception(message)

        # Delete invalid parameters
        if len(invalid_parameters) != 0:
            message = f"The following parameters are invalid: {', '.join(invalid_parameters)}. Using strategy without these parameters."
            strategy_object = parsed_strategy.body[0].value.keywords
            valid_keywords = [kwarg for kwarg in strategy_object if kwarg.arg not in invalid_parameters]
            parsed_strategy.body[0].value.keywords = valid_keywords
            changes['strategy'] = message

        mandatory_parameters = ['ticker', 'position_type', 'buy_condition', 'sell_condition']

        for mandatory_parameter in mandatory_parameters:
            if mandatory_parameter not in valid_parameters:
                # Defaulting to AAPL if no ticker
                if mandatory_parameter == 'ticker':
                    parsed_strategy.body[0].value.keywords.append(
                        ast.keyword(
                            arg=mandatory_parameter,
                            value=ast.Constant(value='AAPL')
                        )
                    )
                # Defaulting to LONG if no position_type
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
                else:
                    raise Exception(f"Missing mandatory buy or sell condition parameter.")

    except Exception as e:
        if message == '':
            message = f"Error parsing strategy string: {e}"

        if logs:
            print(f"Error parsing strategy string: {e}")

        changes['strategy'] = message

        return False, '', changes

    return True, ast.unparse(parsed_strategy), changes


x,y,z = validate_strategy_string("Strategy(trade_commissions=MoneyCommissions(1),position_type=PositionTypeEnum.LONG, buy_condition=OR( CrossOverCondition(first_series=RSI('TSLA'), second_series=CONST(30)), LessThanCondition(first_series=EMA('TSLA'), second_series=CLOSE('TSLA'))), sell_condition=OR( CrossOverCondition(first_series=CONST(70), second_series=RSI('TSLA')), IntraIntervalChangeOfXPercentCondition(series=CLOSE('TSLA'), percent=5)), stop_loss=StopLoss(percentage=5, stop_loss_type=StopLossType.NORMAL), take_profit=TakeProfit(percentage=10), start_date=datetime(2020, 1, 1), end_date=datetime(2024, 1, 1), initial_capital=1000, order_size=Contracts(1))")

print(x)
print(y)
print(z)