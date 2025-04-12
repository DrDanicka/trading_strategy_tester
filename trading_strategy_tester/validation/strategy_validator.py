from trading_strategy_tester.enums.llm_model_enum import LLMModel
import ollama

# ----- Import conditions -----

# Import fibonacci retracement level conditions
from trading_strategy_tester.conditions.fibonacci_retracement_levels_conditions.downtrend_fib_retracement_level import DowntrendFibRetracementLevelCondition
from trading_strategy_tester.conditions.fibonacci_retracement_levels_conditions.uptrend_fib_retracement_level import UptrendFibRetracementLevelCondition
# Import logical conditions
from trading_strategy_tester.conditions.logical_conditions.or_condition import OR
from trading_strategy_tester.conditions.logical_conditions.and_condition import AND
# Import parameterized conditions
from trading_strategy_tester.conditions.parameterized_conditions.after_x_days_condition import AfterXDaysCondition
from trading_strategy_tester.conditions.parameterized_conditions.change_of_x_percent_per_y_days_condition import ChangeOfXPercentPerYDaysCondition
from trading_strategy_tester.conditions.parameterized_conditions.intra_interval_change_of_x_percent_condition import IntraIntervalChangeOfXPercentCondition
# Import stoploss and takeprofit conditions
from trading_strategy_tester.conditions.stoploss_takeprofit.stop_loss import StopLoss
from trading_strategy_tester.conditions.stoploss_takeprofit.take_profit import TakeProfit
# Import threshold conditions
from trading_strategy_tester.conditions.threshold_conditions.greater_than_condition import GreaterThanCondition
from trading_strategy_tester.conditions.threshold_conditions.less_than_condition import LessThanCondition
from trading_strategy_tester.conditions.threshold_conditions.cross_over_condition import CrossOverCondition
# Import trend conditions
from trading_strategy_tester.conditions.trend_conditions.uptrend_for_x_days_condition import UptrendForXDaysCondition
from trading_strategy_tester.conditions.trend_conditions.downtrend_for_x_days_condition import DowntrendForXDaysCondition

# ----- Import enums -----
from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels
from trading_strategy_tester.enums.interval_enum import Interval
from trading_strategy_tester.enums.period_enum import Period
from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.stoploss_enum import StopLossType
from trading_strategy_tester.enums.source_enum import SourceType

# ----- Import trades -----
from trading_strategy_tester.trade.order_size.contracts import Contracts
from trading_strategy_tester.trade.order_size.percent_of_equity import PercentOfEquity
from trading_strategy_tester.trade.order_size.usd import USD
from trading_strategy_tester.trade.trade_commissions.money_commissions import MoneyCommissions
from trading_strategy_tester.trade.trade_commissions.percentage_commissions import PercentageCommissions

# ----- Import trading series -----
from trading_strategy_tester.trading_series.adx_series.adx_series import ADX
from trading_strategy_tester.trading_series.aroon_series.aroon_up_series import AROON_UP
from trading_strategy_tester.trading_series.aroon_series.aroon_down_series import AROON_DOWN
from trading_strategy_tester.trading_series.atr_series.atr_series import ATR
from trading_strategy_tester.trading_series.bb_series.bb_lower_series import BB_LOWER
from trading_strategy_tester.trading_series.bb_series.bb_upper_series import BB_UPPER
from trading_strategy_tester.trading_series.bb_series.bb_middle_series import BB_MIDDLE
from trading_strategy_tester.trading_series.bbp_series.bbp_series import BBP
from trading_strategy_tester.trading_series.candlestick_series.hammer_series import HAMMER
from trading_strategy_tester.trading_series.cci_series.cci_series import CCI
from trading_strategy_tester.trading_series.cci_series.cci_smoothened_series import CCI_SMOOTHENED
from trading_strategy_tester.trading_series.chaikin_osc_series.chaikin_osc_series import CHAIKIN_OSC
from trading_strategy_tester.trading_series.chop_series.chop_series import CHOP
from trading_strategy_tester.trading_series.cmf_series.cmf_series import CMF
from trading_strategy_tester.trading_series.cmo_series.cmo_series import CMO
from trading_strategy_tester.trading_series.coppock_series.coppock_series import COPPOCK
from trading_strategy_tester.trading_series.dc_series.dc_basis_series import DC_BASIS
from trading_strategy_tester.trading_series.dc_series.dc_lower_series import DC_LOWER
from trading_strategy_tester.trading_series.dc_series.dc_upper_series import DC_UPPER
from trading_strategy_tester.trading_series.default_series.close_series import CLOSE
from trading_strategy_tester.trading_series.default_series.const_series import CONST
from trading_strategy_tester.trading_series.default_series.high_series import HIGH
from trading_strategy_tester.trading_series.default_series.low_series import LOW
from trading_strategy_tester.trading_series.default_series.open_series import OPEN
from trading_strategy_tester.trading_series.default_series.volume_series import VOLUME
from trading_strategy_tester.trading_series.di_series.di_minus_series import DI_MINUS
from trading_strategy_tester.trading_series.di_series.di_plus_series import DI_PLUS
from trading_strategy_tester.trading_series.dpo_series.dpo_series import DPO
from trading_strategy_tester.trading_series.efi_series.efi_series import EFI
from trading_strategy_tester.trading_series.eom_series.eom_series import EOM
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_base_series import ICHIMOKU_BASE
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_conversion_series import ICHIMOKU_CONVERSION
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_lagging_span_series import ICHIMOKU_LAGGING_SPAN
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_leading_span_a_series import ICHIMOKU_LEADING_SPAN_A
from trading_strategy_tester.trading_series.ichimoku_series.ichimoku_leading_span_b_series import ICHIMOKU_LEADING_SPAN_B
from trading_strategy_tester.trading_series.kc_series.kc_lower_series import KC_LOWER
from trading_strategy_tester.trading_series.kc_series.kc_upper_series import KC_UPPER
from trading_strategy_tester.trading_series.kst_series.kst_series import KST
from trading_strategy_tester.trading_series.kst_series.kst_signal_series import KST_SIGNAL
from trading_strategy_tester.trading_series.ma_series.ema_series import EMA
from trading_strategy_tester.trading_series.ma_series.sma_series import SMA
from trading_strategy_tester.trading_series.macd_series.macd_series import MACD
from trading_strategy_tester.trading_series.macd_series.macd_signal_series import MACD_SIGNAL
from trading_strategy_tester.trading_series.mass_series.mass_series import MASS_INDEX
from trading_strategy_tester.trading_series.mfi_series.mfi_series import MFI
from trading_strategy_tester.trading_series.momentum_series.momentum_series import MOMENTUM
from trading_strategy_tester.trading_series.obv_series.obv_series import OBV
from trading_strategy_tester.trading_series.pvi_series.pvi_series import PVI
from trading_strategy_tester.trading_series.pvt_series.pvt_series import PVT
from trading_strategy_tester.trading_series.roc_series.roc_series import ROC
from trading_strategy_tester.trading_series.rsi_series.rsi_series import RSI
from trading_strategy_tester.trading_series.stoch_series.percent_d_series import STOCH_PERCENT_D
from trading_strategy_tester.trading_series.stoch_series.percent_k_series import STOCH_PERCENT_K
from trading_strategy_tester.trading_series.trix_series.trix_series import TRIX
from trading_strategy_tester.trading_series.uo_series.uo_series import UO
from trading_strategy_tester.trading_series.willr_series.willr_series import WILLR

# ----- Import strategy -----
from trading_strategy_tester.strategy.strategy import Strategy

from datetime import datetime

namespace = {
    'DowntrendFibRetracementLevelCondition': DowntrendFibRetracementLevelCondition,
    'UptrendFibRetracementLevelCondition': UptrendFibRetracementLevelCondition,
    'OR': OR,
    'AND': AND,
    'AfterXDaysCondition': AfterXDaysCondition,
    'ChangeOfXPercentPerYDaysCondition': ChangeOfXPercentPerYDaysCondition,
    'IntraIntervalChangeOfXPercentCondition': IntraIntervalChangeOfXPercentCondition,
    'StopLoss': StopLoss,
    'TakeProfit': TakeProfit,
    'GreaterThanCondition': GreaterThanCondition,
    'LessThanCondition': LessThanCondition,
    'CrossOverCondition': CrossOverCondition,
    'UptrendForXDaysCondition': UptrendForXDaysCondition,
    'DowntrendForXDaysCondition': DowntrendForXDaysCondition,
    'FibonacciLevels': FibonacciLevels,
    'Interval': Interval,
    'Period': Period,
    'PositionTypeEnum': PositionTypeEnum,
    'SmoothingType': SmoothingType,
    'StopLossType': StopLossType,
    'SourceType': SourceType,
    'Contracts': Contracts,
    'PercentOfEquity': PercentOfEquity,
    'USD': USD,
    'MoneyCommissions': MoneyCommissions,
    'PercentageCommissions': PercentageCommissions,
    'ADX': ADX,
    'AROON_UP': AROON_UP,
    'AROON_DOWN': AROON_DOWN,
    'ATR': ATR,
    'BB_LOWER': BB_LOWER,
    'BB_UPPER': BB_UPPER,
    'BB_MIDDLE': BB_MIDDLE,
    'BBP': BBP,
    'HAMMER': HAMMER,
    'CCI': CCI,
    'CCI_SMOOTHENED': CCI_SMOOTHENED,
    'CHAIKIN_OSC': CHAIKIN_OSC,
    'CHOP': CHOP,
    'CMF': CMF,
    'CMO': CMO,
    'COPPOCK': COPPOCK,
    'DC_BASIS': DC_BASIS,
    'DC_LOWER': DC_LOWER,
    'DC_UPPER': DC_UPPER,
    'CLOSE': CLOSE,
    'CONST': CONST,
    'HIGH': HIGH,
    'LOW': LOW,
    'OPEN': OPEN,
    'VOLUME': VOLUME,
    'DI_MINUS': DI_MINUS,
    'DI_PLUS': DI_PLUS,
    'DPO': DPO,
    'EFI': EFI,
    'EOM': EOM,
    'ICHIMOKU_BASE': ICHIMOKU_BASE,
    'ICHIMOKU_CONVERSION': ICHIMOKU_CONVERSION,
    'ICHIMOKU_LAGGING_SPAN': ICHIMOKU_LAGGING_SPAN,
    'ICHIMOKU_LEADING_SPAN_A': ICHIMOKU_LEADING_SPAN_A,
    'ICHIMOKU_LEADING_SPAN_B': ICHIMOKU_LEADING_SPAN_B,
    'KC_LOWER': KC_LOWER,
    'KC_UPPER': KC_UPPER,
    'KST': KST,
    'KST_SIGNAL': KST_SIGNAL,
    'EMA': EMA,
    'SMA': SMA,
    'MACD': MACD,
    'MACD_SIGNAL': MACD_SIGNAL,
    'MASS_INDEX': MASS_INDEX,
    'MFI': MFI,
    'MOMENTUM': MOMENTUM,
    'OBV': OBV,
    'PVI': PVI,
    'PVT': PVT,
    'ROC': ROC,
    'RSI': RSI,
    'STOCH_PERCENT_D': STOCH_PERCENT_D,
    'STOCH_PERCENT_K': STOCH_PERCENT_K,
    'TRIX': TRIX,
    'UO': UO,
    'WILLR': WILLR,
    'Strategy': Strategy,
    'datetime': datetime
}

#--------------------------

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
    global_ticker = 'AAPL'

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
                else:
                    global_ticker = ticker
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
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=True, global_ticker=global_ticker)

                # Always rewrite because there can be condition omit and we get True and the condition changed
                if validation_result:
                    kwarg.value = condition
                else:
                    message = f'Error in buy condition'
                    raise Exception(message)

            elif kwarg.arg == 'sell_condition':
                validation_result, condition, changes = validate_condition(kwarg.value, changes, logs, buy=False, global_ticker=global_ticker)

                # Always rewrite because there can be condition omit and we get True and the condition changed
                if validation_result:
                    kwarg.value = condition
                else:
                    message = f'Error in sell condition'
                    raise Exception(message)

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
                    changes['strategy'] = f'No ticker specified. Defaulting to AAPL ticker.'
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
                    changes['strategy'] = f'No position type specified. Defauling to long positions.'
                else:
                    raise Exception(f"Missing mandatory buy or sell condition parameter.")
    except Exception as e:
        if message == '':
            message = f"Error parsing strategy string: {e}"

        if logs:
            print(f"Error parsing strategy string: {e}")

        changes['strategy'] = message

        return False, '', changes

    print(ast.dump(parsed_strategy.body[0].value))

    return True, ast.unparse(parsed_strategy), changes

"""
TRUE
- no ticker                                             PASS
- no position_type                                      PASS
- trading_series missing parameter                      PASS
- trading_series missing ticker -> use global ticker    PASS
- wrong stop_loss -> default 0                          PASS
- wrong take_profit -> default 0                        PASS
- wrong start_date
- wrong end_date
- wrong interval -> default ONE_DAY                     PASS
- wrong period -> default NOT_PASSED
- wrong initial_capital -> default 1_000_000
- wrong order_size -> Contracts(1)                      PASS
- wrong trade_commissions -> MoneyCommissions(0)        PASS
- wrong trading_series in logical conditions            PASS

FALSE
- no buy_condition
- no sell_condition
- condition missing parameter
- syntactic mistakes
"""

strat_str = """
Strategy(
    ticker = 'AAPL',
    position_type=PositionTypeEnum.LONG,
    buy_condition=CrossOverCondition(
        first_series=BB_LOWER(
            'AAPL',
            source=SourceType.CLOSE
        ),
        second_series=CONST(30)
    ),
    sell_condition=AND(
        CrossOverCondition(
            first_series=CONST(70),
            second_series=RSI(
                'AAPL'
            )
        ),
        IntraIntervalChangeOfXPercentCondition(
            series=CLOSE('AAPL'),
            percent=5
        )
    ),
    stop_loss=StopLoss(
        percentage=5,
        stop_loss_type=StopLossType.NORMAL
    ),
    take_profit=TakeProfit(
        percentage=10
    ),
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2024, 1, 1),
    commission=MoneyCommissions(value=0)
)"""



x,y,z = validate_strategy_string(strat_str)

print(x)
print(y)
print(z)

if x:
    try:
        strat : Strategy = eval(y, namespace)
        strat.execute()
    except Exception as e:
        print(e)