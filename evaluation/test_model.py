import ollama
import pandas as pd
import json
from deepdiff import DeepDiff

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
from trading_strategy_tester.conditions.threshold_conditions.cross_under_condition import CrossUnderCondition
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
from trading_strategy_tester.validation.strategy_validator import *

import ast

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
    'CrossUnderCondition': CrossUnderCondition,
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

ollama_models = [
    'llama3-2-1B_tst_ft-ticker',
    'llama3-2-1B_tst_ft-position_type',
    'llama3-2-3B_tst_ft-conditions',
    'llama3-2-1B_tst_ft-stop_loss',
    'llama3-2-1B_tst_ft-take_profit',
    'llama3-2-1B_tst_ft-start_date',
    'llama3-2-1B_tst_ft-end_date',
    'llama3-2-1B_tst_ft-period',
    'llama3-2-1B_tst_ft-interval',
    'llama3-2-1B_tst_ft-initial_capital',
    'llama3-2-1B_tst_ft-order_size',
    'llama3-2-1B_tst_ft-trade_commissions'
    'llama3-2-3B_tst_ft-all',
]


class xTester:
    def __init__(self, model:str, log: bool = False):
        self.number_of_tested_cases = 0

        # Variable for validity of the output
        self.number_of_not_valid_outputs = 0

        # Variable for wrong outputs
        self.number_of_wrong_outputs = 0

        # Variables for parameters of the outputs
        self.number_of_wrong_parameters = 0
        self.number_of_all_parameters = 0

        self.model = model
        self.model_for = self.model.split('-')[-1]
        if self.model_for == 'rag':
            self.model_for = self.model.split('-')[-2]

        self.test_data = self.load_data()

        self.log = log

    def load_data(self):
        # Load data from JSONL file where model has been trained
        return pd.read_json(path_or_buf=f'testing_outputs/{self.model}.jsonl', lines=True)


    def validate_response(self, response: str):
        model_to_validation_mapping = {
            'ticker': validate_ticker,
            'position_type': validate_position_type,
            'conditions': validate_condition,
            'stop_loss': validate_stop_loss,
            'take_profit': validate_take_profit,
            'start_date': validate_date,
            'end_date': validate_date,
            'period': validate_period,
            'interval': validate_interval,
            'initial_capital': validate_initial_capital,
            'order_size': validate_order_size,
            'trade_commissions': validate_trade_commissions,
            'all': validate_strategy_string
        }

        if self.model_for == 'conditions':
            final_obj = None
            if 'buy_condition=' in response and 'sell_condition=' in response:
                try:
                    buy_condition_str, sell_condition_str = response.split('sell_condition=')
                    buy_condition_str = buy_condition_str.split('buy_condition=')[-1].strip()[:-1] # to remove last comma

                    buy_condition = ast.parse(buy_condition_str, mode='eval')
                    sell_condition = ast.parse(sell_condition_str, mode='eval')

                    validation_result_buy, validated_obj_buy, _ = validate_condition(
                        condition=buy_condition.body,
                        changes={},
                        logs=False,
                        buy=True,
                        global_ticker=''
                    )

                    validation_result_sell, validated_obj_sell, _ = validate_condition(
                        condition=sell_condition.body,
                        changes={},
                        logs=False,
                        buy=False,
                        global_ticker=''
                    )

                    if validation_result_buy and validation_result_sell:
                        final_obj = f'buy_condition={ast.unparse(validated_obj_buy)}, sell_condition={ast.unparse(validated_obj_sell)}'

                    return validation_result_buy and validation_result_sell, final_obj
                except Exception as e:
                    return False, final_obj
            else:
                return False, final_obj
        elif self.model_for == 'all':
            validation_result, validated_obj, _ = validate_strategy_string(response, logs=False)

            return validation_result, validated_obj
        else:
            if response == '':
                return True, None
            split_response = response.split('=')
            param_name = split_response[0].strip()
            param_value = '='.join(split_response[1:])

            if param_name == self.model_for:
                try:
                    param_value = ast.parse(param_value, mode='eval')
                except Exception as e:
                    return False, None

                validation_result, validated_obj, _ = model_to_validation_mapping[self.model_for](
                    param_value.body, {}, False
                )
            else:
                return False, None

            return validation_result, validated_obj

    def _count_total_params(self, d):
        if isinstance(d, dict):
            return sum(self._count_total_params(v) for v in d.values()) + len(d.values()) - 1
        elif isinstance(d, list):
            return sum(self._count_total_params(i) for i in d)
        else:
            return 1

    def _compare_dicts(self, dict1, dict2):
        diff = DeepDiff(dict1, dict2, ignore_order=True, report_repetition=True)
        total_params = self._count_total_params(dict1)
        total_differences = sum(len(v) for v in diff.values())

        if self.log:
            if total_differences > 0:
                print(f"Difference found: {diff}")

        return total_params, total_differences

    def _compare_strategy_objects(self, obj1_str, obj2_str):
        """
        Compare two strategy objects represented as strings.

        :param obj1_str: The first strategy object string.
        :param obj2_str: The second strategy object string.
        :return: True if the objects are equivalent, False otherwise.
        """
        number_of_parameters = 0
        number_of_faults = 0

        # Convert the strings to strategy objects
        strat1: Strategy = eval(obj1_str, namespace)
        strat2: Strategy = eval(obj2_str, namespace)

        # Convert strategy objects to dictionaries
        strat1_dict = strat1.to_dict()
        strat2_dict = strat2.to_dict()

        for key in strat1_dict.keys():
            # Compare conditions recursively
            arg1 = strat1_dict[key]
            arg2 = strat2_dict[key]

            number_of_params, number_of_differences = self._compare_dicts(arg1, arg2)

            number_of_parameters += number_of_params
            number_of_faults += number_of_differences

            number_of_parameters += 1 # For argument name

        return number_of_parameters, number_of_faults, number_of_faults == 0

    def _compare_parameter_object(self, obj1_str: str, obj2_str: str):
        obj1_str = '='.join(obj1_str.split('=')[1:])
        obj2_str = '='.join(obj2_str.split('=')[1:])

        # Convert the strings to objects of arguments in Strategy
        obj1 = eval(obj1_str, namespace)
        obj2 = eval(obj2_str, namespace)

        # Convert argument objects to dictionaries
        obj1_dict = obj1.to_dict()
        obj2_dict = obj2.to_dict()

        number_of_params, number_of_differences = self._compare_dicts(obj1_dict, obj2_dict)

        return number_of_params, number_of_differences, number_of_differences == 0


    def _compare_dates(self, date1: str, date2: str):
        number_of_faults = 0
        number_of_parameters = 4

        try:
            _, date_value1 = date1.split('=')
            date_name2, date_value2 = date2.split('=')

            # Strip all values
            date_name2 = date_name2.strip()
            date_values1 = date_value1.split('(')[-1].split(',')
            date_values2 = date_value2.split('(')[-1].split(',')

            year1 = date_values1[0].strip()
            month1 = date_values1[1].strip()
            day1 = date_values1[2].strip()

            year2 = date_values2[0].strip()
            month2 = date_values2[1].strip()
            day2 = date_values2[2].strip()

            if date_name2 not in ['start_date', 'end_date']:
                number_of_faults += 1
                if self.log:
                    print(f"Date name is not valid: {date_name2}")

            if year1 != year2:
                number_of_faults += 1
                if self.log:
                    print(f"Year is not valid: {year1} != {year2}")

            if month1 != month2:
                number_of_faults += 1
                if self.log:
                    print(f"Month is not valid: {month1} != {month2}")

            if day1 != day2:
                number_of_faults += 1
                if self.log:
                    print(f"Day is not valid: {day1} != {day2}")

        except Exception:
            return number_of_parameters, number_of_parameters, False

        return number_of_parameters, number_of_faults, number_of_faults == 0

    def _compare_enum(self, enum1: str, enum2: str, enum_name: str):
        number_of_faults = 0
        number_of_parameters = 2

        try:
            _, value1 = enum1.split('=')
            name2, value2 = enum2.split('=')

            # Strip all values
            name2 = name2.strip()
            value1 = value1.strip()
            value2 = value2.strip()

            if name2 != enum_name:
                number_of_faults += 1
                if self.log:
                    print(f"Name is not valid: {name2}")

            if value1 != value2:
                number_of_faults += 1
                if self.log:
                    print(f"Value is not valid: {value1} != {value2}")

        except Exception:
            return number_of_parameters, number_of_parameters, False

        return number_of_parameters, number_of_faults, number_of_faults == 0

    def compare_outputs(self, expected_completion: str, response: str) -> (int, int, bool):
        matched_outputs = 2

        if expected_completion == '':
            if response == '':
                return matched_outputs, 0, True
            else:
                return matched_outputs, matched_outputs, False

        if response == '':
            return matched_outputs, matched_outputs, False

        if self.model_for == 'all':
            return self._compare_strategy_objects(expected_completion, response)
        elif self.model_for == 'conditions':
            buy_condition_expected = expected_completion.split('sell_condition=')[0].strip()[:-1]
            buy_condition_response = response.split('sell_condition=')[0].strip()[:-1]
            sell_condition_expected = f"sell_condition={expected_completion.split('sell_condition=')[1].strip()}"
            sell_condition_response = f"sell_condition={response.split('sell_condition=')[1].strip()}"

            number_of_params_buy, number_of_faults_buy, identical_buy = self._compare_parameter_object(buy_condition_expected, buy_condition_response)
            number_of_params_sell, number_of_faults_sell, identical_sell = self._compare_parameter_object(sell_condition_expected, sell_condition_response)

            return number_of_params_buy + number_of_params_sell, number_of_faults_buy + number_of_faults_sell, identical_buy and identical_sell
        elif self.model_for in ['stop_loss', 'take_profit', 'order_size', 'trade_commissions']:
            return self._compare_parameter_object(expected_completion, response)
        elif self.model_for in ['start_date', 'end_date']:
            return self._compare_dates(expected_completion, response)
        elif self.model_for in ['ticker', 'position_type', 'interval', 'period', 'initial_capital']:
            return self._compare_enum(expected_completion, response, self.model_for)
        else:
            raise ValueError(f"Unknown model for: {self.model_for}")


    def test(self, prompt: str, expected_completion: str, response: str):
        validation_result, validated_obj = self.validate_response(response)

        if validation_result:
            string_to_test = validated_obj if self.model_for in ['all', 'conditions'] else response

            number_of_params, number_of_wrong_params, identical = self.compare_outputs(expected_completion, string_to_test)

            self.number_of_wrong_parameters += number_of_wrong_params
            self.number_of_all_parameters += number_of_params

            if not identical:
                self.number_of_wrong_outputs += 1
        else:
            self.number_of_not_valid_outputs += 1
            if self.log:
                print(f"Response is not valid: {response}")

        self.number_of_tested_cases += 1


    def test_all(self):
        for i, row in self.test_data.iterrows():
            prompt = row['prompt']
            expected_completion = row['completion']
            response = row['response']

            self.test(prompt, expected_completion, response)

    def print_results(self):
        print(f"Number of tested cases: {self.number_of_tested_cases}")
        print(f"Number of not valid outputs: {self.number_of_not_valid_outputs}")
        print(f"Number of wrong outputs: {self.number_of_wrong_outputs}")
        print(f"Number of wrong parameters: {self.number_of_wrong_parameters}")
        print(f"Number of all parameters: {self.number_of_all_parameters}")


tester = xTester('llama3-2-3B_tst_ft-conditions', log=False)
tester.test_all()
tester.print_results()
