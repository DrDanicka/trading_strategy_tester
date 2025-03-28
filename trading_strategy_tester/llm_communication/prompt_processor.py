from trading_strategy_tester.enums.llm_model_enum import LLMModel
import ollama

# ----- Import conditions -----

# Import fibonacci retracement level conditions
from trading_strategy_tester.conditions.fibonacci_retracement_levels_conditions.downtrend_fib_retracement import DowntrendFibRetracementLevelCondition
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
from trading_strategy_tester.trade.order_size.order_size import OrderSize
from trading_strategy_tester.trade.order_size.percent_of_equity import PercentOfEquity
from trading_strategy_tester.trade.order_size.usd import USD
from trading_strategy_tester.trade.trade_commissions.money_commissions import MoneyCommissions
from trading_strategy_tester.trade.trade_commissions.percentage_commissions import PercentageCommissions
from trading_strategy_tester.trade.trade_commissions.trade_commissions import TradeCommissions

# ----- Import trading series -----
from trading_strategy_tester.trading_series.adx_series.adx_series import ADX
from trading_strategy_tester.trading_series.aroon_series.aroon_up_series import AROON_UP
from trading_strategy_tester.trading_series.aroon_series.aroon_down_series import AROON_DOWN
from trading_strategy_tester.trading_series.atr_series.atr_series import ATR
from trading_strategy_tester.trading_series.bb_series.bb_lower_series import BBLOWER
from trading_strategy_tester.trading_series.bb_series.bb_upper_series import BBUPPER
from trading_strategy_tester.trading_series.bb_series.bb_middle_series import BBMIDDLE
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
    'OrderSize': OrderSize,
    'PercentOfEquity': PercentOfEquity,
    'USD': USD,
    'MoneyCommissions': MoneyCommissions,
    'PercentageCommissions': PercentageCommissions,
    'TradeCommissions': TradeCommissions,
    'ADX': ADX,
    'AROON_UP': AROON_UP,
    'AROON_DOWN': AROON_DOWN,
    'ATR': ATR,
    'BBLOWER': BBLOWER,
    'BBUPPER': BBUPPER,
    'BBMIDDLE': BBMIDDLE,
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

'''
Delete After strats:

Strategy(ticker='AAPL',position_type=PositionTypeEnum.LONG,buy_condition=CrossOverCondition(RSI('AAPL'),CONST(30)),sell_condition=CrossOverCondition(CONST(70),RSI('AAPL')),start_date=datetime(2020, 1, 1),end_date=datetime(2025, 1, 1))

Strategy(ticker='TSLA', position_type=PositionTypeEnum.LONG, buy_condition=OR( CrossOverCondition(first_series=RSI('TSLA'), second_series=CONST(30)), LessThanCondition(first_series=EMA('TSLA'), second_series=CLOSE('TSLA'))), sell_condition=OR( CrossOverCondition(first_series=CONST(70), second_series=RSI('TSLA')), IntraIntervalChangeOfXPercentCondition(series=CLOSE('TSLA'), percent=5)), stop_loss=StopLoss(percentage=5, stop_loss_type=StopLossType.NORMAL), take_profit=TakeProfit(percentage=10), start_date=datetime(2020, 1, 1), end_date=datetime(2024, 1, 1), initial_capital=1000)

'''

def process_prompt(prompt: str, llm_model: LLMModel = LLMModel.LLAMA_1B):
    '''
    This function processes the prompt and returns the result.
    '''
    client = ollama.Client()

    # Process the prompt using the specified LLM model
    if llm_model in [
        LLMModel.LLAMA_1B,
        LLMModel.QWEN_0_5B
    ]:
        # Process the prompt using llama
        response = client.generate(
            model = llm_model.value,
            prompt = prompt
        )
        result = response.response
    elif llm_model == LLMModel.CHAT_GPT_API:
        # Process the prompt using chat-gpt-api
        result = ...
    elif llm_model == LLMModel.STRATEGY_OBJECT:
        # TODO add validation
        result = prompt
    else:
        raise ValueError("Invalid LLM model specified")

    # Evaluate the result
    strat : Strategy = eval(result, namespace)
    strat.execute()

    return strat.get_trades(), strat.get_graphs(), strat.get_statistics()