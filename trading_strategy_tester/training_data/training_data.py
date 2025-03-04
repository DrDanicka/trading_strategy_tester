import random
import pandas as pd

from trading_strategy_tester.enums.position_type_enum import PositionTypeEnum
from trading_strategy_tester.enums.smoothing_enum import SmoothingType
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.enums.fibonacci_levels_enum import FibonacciLevels

# Create training data for the model

prompt_starts = [
    'Could you develop a {strategy_type} strategy for {ticker} that',
    'Would you be able to create a {strategy_type} strategy for {ticker} that',
    'Please design a strategy for {ticker} that',
    'Can you generate a {strategy_type} strategy for {ticker} that',
    'Would you mind crafting a {strategy_type} strategy for {ticker} that',
    'Could you outline a {strategy_type} strategy for {ticker} that',
    'I need a {strategy_type} strategy for {ticker} that',
    'Can you help formulate a {strategy_type} strategy for {ticker} that',
    'Would you kindly create a {strategy_type} strategy for {ticker} that',
    'Can you provide a {strategy_type} strategy for {ticker} that',
    'Might you be able to develop a {strategy_type} strategy for {ticker} that',
    'Could you draft a {strategy_type} trading strategy for {ticker} that',
    'Please come up with a {strategy_type} strategy for {ticker} that',
    'I’d appreciate it if you could design a {strategy_type} strategy for {ticker} that',
    'Can you structure a {strategy_type} strategy for {ticker} that',
    'Would you be willing to create a {strategy_type} strategy for {ticker} that',
    'Can you tailor a {strategy_type} strategy for {ticker} that',
    'I’m looking for a {strategy_type} strategy for {ticker} that',
    'Could you put together a {strategy_type} strategy for {ticker} that',
    'Is it possible for you to create a {strategy_type} strategy for {ticker} that'
]


buy_sell_action_conditions = [
    '{action} when the {condition} is met',
    '{action} when the {condition} is true',
    '{action} when the {condition} is satisfied',
    '{action} when the {condition} is fulfilled',
    '{action} when the {condition} is valid',
    '{action} when the {condition} is correct',
    '{action} when the {condition} is right',
    '{action} when the {condition} is accurate',
    '{action} when the {condition} is exact',
    '{action} when the {condition} is precise',
    '{action} when the {condition} is proper',
    '{action} when the {condition} is appropriate',
    '{action} when the {condition} is fitting',
    '{action} when the {condition} is suitable',
    '{action} when the {condition} is relevant',
    '{action} when the {condition} is pertinent',
    '{action} when the {condition} is germane',
    '{action} when the {condition} is applicable',
    '{action} when the {condition} is apposite',
    '{action} when the {condition} is apt',
    '{action} when the {condition} is befitting',
    '{action} when the {condition} is felicitous',
    '{action} when the {condition} is good',
    '{action} when the {condition} is just',
    '{action} when the {condition} is meet',
    '{action} when the {condition} is nice',
    '{action} when the {condition} is proper',
    '{action} when the {condition} is right',
    '{action} when the {condition} is seemly',
    '{action} when the {condition} is tailor-made',
    '{action} when the {condition} is to the point',
    '{action} when the {condition} is useful',
    '{action} when the {condition} is well-suited',
    '{action} when the {condition} is well-timed',
    '{action} when the {condition} is well-qualified',
    '{action} when the {condition} is well-chosen',
    '{action} when the {condition} is well-aimed',
    '{action} when the {condition} is well-fitted',
    '{action} when the {condition} is well-matched',
    '{action} when the {condition} is well-tailored',
]

crossover_conditions_up = [
    '{indicator} crossed above {value}',
    '{indicator} rises above {value}',
    '{indicator} climbs above {value}',
    '{indicator} jumps above {value}',
    '{indicator} moves above {value}',
    '{indicator} goes above {value}',
    '{indicator} exceeds {value}',
    '{indicator} surpasses {value}',
    '{indicator} breaches {value}',
    '{indicator} breaks through {value}',
    '{indicator} goes beyond {value}',
    '{indicator} crossed up {value}',
    '{indicator} crosses over {value}'
]

crossover_conditions_down = [
    '{indicator} is beneath {value}',
    '{indicator} crosses below {value}',
    '{indicator} falls below {value}',
    '{indicator} drops below {value}',
    '{indicator} descends below {value}',
    '{indicator} moves below {value}',
    '{indicator} goes below {value}',
    '{indicator} drops under {value}',
    '{indicator} slips under {value}',
    '{indicator} falls under {value}',
    '{indicator} moves under {value}',
    '{indicator} crosses down {value}',
    '{indicator} crosses under {value}'
    '{indicator} dips below {value}'
]

change_of_x_percent_per_y_days_conditions = [
    '{indicator} changes by {percent} percent over {days} days',
    '{indicator} moves by {percent} percent over {days} days',
    '{indicator} shifts by {percent} percent over {days} days',
    '{indicator} varies by {percent} percent over {days} days',
    '{indicator} fluctuates by {percent} percent over {days} days',
    '{indicator} oscillates by {percent} percent over {days} days',
    '{indicator} swings by {percent} percent over {days} days',
    '{indicator} sways by {percent} percent over {days} days',
    '{indicator} wobbles by {percent} percent over {days} days',
    '{indicator} rocks by {percent} percent over {days} days',
    '{indicator} rolls by {percent} percent over {days} days',
    '{indicator} pitches by {percent} percent over {days} days',
    '{indicator} yaws by {percent} percent over {days} days',
    '{indicator} veers by {percent} percent over {days} days',
    '{indicator} turns by {percent} percent over {days} days',
    '{indicator} twists by {percent} percent over {days} days',
    '{indicator} spins by {percent} percent over {days} days'
]

intra_interval_change_of_x_percent_conditions = [
    '{indicator} changes by {percent} percent within a interval',
    '{indicator} moves by {percent} percent within a interval',
    '{indicator} shifts by {percent} percent within a interval',
    '{indicator} varies by {percent} percent within a interval',
    '{indicator} fluctuates by {percent} percent within a interval',
    '{indicator} oscillates by {percent} percent within a interval',
    '{indicator} swings by {percent} percent within a interval',
    '{indicator} sways by {percent} percent within a interval',
    '{indicator} wobbles by {percent} percent within a interval',
    '{indicator} rocks by {percent} percent within a interval',
    '{indicator} rolls by {percent} percent within a interval',
    '{indicator} pitches by {percent} percent within a interval',
    '{indicator} yaws by {percent} percent within a interval',
    '{indicator} veers by {percent} percent within a interval',
    '{indicator} turns by {percent} percent within a interval',
    '{indicator} twists by {percent} percent within a interval',
    '{indicator} spins by {percent} percent within a interval'
]

greater_than_conditions = [
    '{indicator} is greater than {value}',
    '{indicator} is more than {value}',
    '{indicator} is higher than {value}',
    '{indicator} is larger than {value}',
    '{indicator} is bigger than {value}',
    '{indicator} is above {value}',
]

less_than_conditions = [
    '{indicator} is less than {value}',
    '{indicator} is lower than {value}',
    '{indicator} is smaller than {value}',
    '{indicator} is beneath {value}',
    '{indicator} is below {value}',
]

downtrend_for_x_days_conditions = [
    '{indicator} is in a downtrend for {days} days',
    '{indicator} is in a bearish trend for {days} days',
    '{indicator} is in a negative trend for {days} days',
    '{indicator} is in a falling trend for {days} days',
    '{indicator} is in a declining trend for {days} days',
    '{indicator} is in a descending trend for {days} days',
    '{indicator} is in a dropping trend for {days} days',
    '{indicator} downtrends for {days} days',
    '{indicator} bearish trends for {days} days',
    '{indicator} negative trends for {days} days',
    '{indicator} falling trends for {days} days',
    '{indicator} declining trends for {days} days',
]

uptrend_for_x_days_conditions = [
    '{indicator} is in an uptrend for {days} days',
    '{indicator} is in a bullish trend for {days} days',
    '{indicator} is in a positive trend for {days} days',
    '{indicator} is in a rising trend for {days} days',
    '{indicator} is in an ascending trend for {days} days',
    '{indicator} is in a growing trend for {days} days',
    '{indicator} is in a climbing trend for {days} days',
    '{indicator} uptrends for {days} days',
    '{indicator} bullish trends for {days} days',
    '{indicator} positive trends for {days} days',
    '{indicator} rising trends for {days} days',
    '{indicator} ascending trends for {days} days',
    '{indicator} growing trends for {days} days',
    '{indicator} climbing trends for {days} days',
]

downtrend_fibonacci_retracement_conditions = [
    'price is in a {level}% fibonacci level during a downtrend',
    'price is within a {level}% fibonacci level during a downtrend',
    'price is at a {level}% fibonacci level during a downtrend',
    'price is at the {level}% fibonacci level during a downtrend'
]

uptrend_fibonacci_retracement_conditions = [
    'price is in a {level}% fibonacci level during an uptrend',
    'price is within a {level}% fibonacci level during an uptrend',
    'price is at a {level}% fibonacci level during an uptrend',
    'price is at the {level}% fibonacci level during an uptrend'
]

buy_actions = ['buy', 'buys', 'purchase', 'purchases', 'acquire', 'acquires', 'obtain', 'obtains', 'get', 'gets',
               'go long', 'goes long', 'take a long position', 'takes a long position', 'longs']

sell_actions = ['sell', 'sells', 'sell off', 'sells off', 'sell out', 'sells out', 'dispose', 'disposes', 'dump',
                'dumps', 'go short', 'goes short', 'take a short position', 'takes a short position', 'shorts']

implemented_indicators = pd.DataFrame(
    data=[['Average Directional Index', 'ADX', 'ADX', 'ticker:str adx_smoothing:int length:int'],
          ['Aroon Indicator Down', 'AROON DOWN', 'AROON_DOWN', 'ticker:str, length:int'],
          ['Aron Indicator Up', 'AROON UP', 'AROON_UP', 'ticker:str, length:int'],
          ['Average True Range', 'ATR', 'ATR', 'ticker:str length:int smoothing:SmoothingType'],
          ['Bollinger Bands Lower band', 'BBLOWER', 'BBLOWER', 'ticker:str source:SourceType length:int ma_type:SmoothingType std_dev:float offset:int'],
          ['Bollinger Bands Middle band', 'BBMIDDLE', 'BBMIDDLE', 'ticker:str source:SourceType length:int ma_type:SmoothingType std_dev:float offset:int'],
          ['Bollinger Bands Upper band', 'BBUPPER', 'BBUPPER', 'ticker:str source:SourceType length:int ma_type:SmoothingType std_dev:float offset:int'],
          ['Bull and Bear Power', 'BBP', 'BBP', 'ticker:str length:int'],
          ['Commodity Channel Index', 'CCI', 'CCI', 'ticker:str source:SourceType length:int'],
          ['Commodity Channel Index Smoothened', 'CCI Smoothened', 'CCI_SMOOTHENED', 'ticker:str source:SourceType length:int smoothing_type:SmoothingType smoothing_length:int'],
          ['Chaikin Oscillator', 'Chaikin osc.', 'CHAIKIN_OSC', 'ticker:str fast_length:int slow_length:int'],
          ['Choppiness Index', 'CHOP', 'CHOP', 'ticker:str length:int offset:int'],
          ['Chaikin Money Flow', 'CMF', 'CMF', 'ticker:str length:int'],
          ['Chande Momentum Oscillator', 'CMO', 'CMO', 'ticker:str source:SourceType length:int'],
          ['Coppock Curve', 'COPPOCK', 'COPPOCK', 'ticker:str length:int long_roc_length:int short_roc_length:int'],
          ['Donchain Channel Basis', 'DC basis', 'DC_BASIS', 'ticker:str length:int offset:int'],
          ['Donchain Channel Upper', 'DC upper', 'DC_UPPER', 'ticker:str length:int offset:int'],
          ['Donchain Channel Lower', 'DC lower', 'DC_LOWER', 'ticker:str length:int offset:int'],
          ['Close Price', 'Close', 'CLOSE', 'ticker:str'],
          ['', '', 'CONST', 'const_number:int'],
          ['High Price', 'High', 'HIGH', 'ticker:str'],
          ['Low Price', 'Low', 'LOW', 'ticker:str'],
          ['Open Price', 'Open', 'OPEN', 'ticker:str'],
          ['Volume', 'Vol', 'VOLUME', 'ticker:str'],
          ['Negative Directional Indicator', 'DI-', 'DI_MINUS', 'ticker:str length:int'],
          ['Positive Directional Indicator', 'DI+', 'DI_PLUS', 'ticker:str length:int'],
          ['Detrended Price Oscillator', 'DPO', 'DPO', 'ticker:str length:int'],
          ['Elder Force Index', 'EFI', 'EFI', 'ticker:str length:int'],
          ['Ease of Movement', 'EOM', 'EOM', 'ticker:str length:int divisor:int'],
          ['Hammer Candlestick Pattern', 'HAMMER', 'HAMMER', 'ticker:str'],
          ['Kijun-sen', 'Ichinoku Base', 'ICHIMOKU_BASE', 'ticker:str length:int'],
          ['Tenkan-sen', 'Ichinoku Conversion', 'ICHIMOKU_CONVERSION', 'ticker:str length:int'],
          ['Senkou Span A', 'Ichinoku Leading Span A', 'ICHIMOKU_LEADING_SPAN_A', 'ticker:str displacement:int'],
          ['Chikou Span', 'Ichinoku Lagging Span', 'ICHIMOKU_LAGGING_SPAN', 'ticker:str displacement:int'],
          ['Senkou Span B', 'Ichinoku Leading Span B', 'ICHIMOKU_LEADING_SPAN_B', 'ticker:str length:int displacement:int'],
          ['Keltner Channel Lower', 'KC Lower', 'KC_LOWER', 'ticker:str source:SourceType length:int multiplier:int use_exp_ma:bool atr_length:int'],
          ['Keltner Channel Upper', 'KC Upper', 'KC_UPPER', 'ticker:str source:SourceType length:int multiplier:int use_exp_ma:bool atr_length:int'],
          ['Know Sure Thing', 'KST', 'KST', 'ticker:str source:SourceType roc_length_1:int roc_length_2:int roc_length_3:int roc_length_4:int sma_length_1:int sma_length_2:int sma_length_3:int sma_length_4:int'],
          ['Know Sure Thing Signal', 'KST Signal', 'KST_SIGNAL', 'ticker:str source:SourceType roc_length_1:int roc_length_2:int roc_length_3:int roc_length_4:int sma_length_1:int sma_length_2:int sma_length_3:int sma_length_4:int signal_length:int'],
          ['Exponential Moving Average', 'EMA', 'EMA', 'ticker:str source:SourceType length:int offset:int'],
          ['Simple Moving Average', 'SMA', 'SMA', 'ticker:str source:SourceType length:int offset:int'],
          ['Moving Average Convergence Divergence', 'MACD', 'MACD', 'ticker:str source:SourceType fast_length:int slow_length:int ma_type:SmoothingType'],
          ['Moving Average Convergence Divergence Signal', 'MACD Signal', 'MACD_SIGNAL', 'ticker:str source:SourceType fast_length:int slow_length:int oscillator_ma_type:SmoothingType signal_ma_type:SmoothingType signal_length:int'],
          ['Mass Index', 'Mass Index', 'MASS_INDEX', 'ticker:str length:int'],
          ['Money Flow Index', 'MFI', 'MFI', 'ticker:str length:int'],
          ['Momentum Indicator', 'Momentum', 'MOMENTUM', 'ticker:str source:SourceType length:int'],
          ['On Balance Volume', 'OBV', 'OBV', 'ticker:str'],
          ['Positive Volume Index', 'PVI', 'PVI', 'ticker:str'],
          ['Price Volume Trend', 'PVT', 'PVT', 'ticker:str'],
          ['Rate of Change', 'ROC', 'ROC', 'ticker:str source:SourceType length:int'],
          ['Relative Strength Index', 'RSI', 'RSI', 'ticker:str source:SourceType length:int'],
          ['Stochastic Percent D', 'Stochastic %D', 'STOCH_PERCENT_D', 'ticker:str length:int d_smooth_length:int'],
          ['Stochastic Percent K', 'Stochastic %K', 'STOCH_PERCENT_K', 'ticker:str length:int'],
          ['Triple Exponential Average', 'TRIX', 'TRIX', 'ticker:str length:int'],
          ['Ultimate Oscillator', 'UO', 'UO', 'ticker:str fast_length:int middle_length:int slow_length:int'],
          ['Williams %R', 'WILLR', 'WILLR', 'ticker:str source:SourceType length:int'],
          ],
    columns=['Indicator', 'Shortcut', 'Class_name', 'Parameters']
)

parameter_equality_options = [
    '{name} is equal to {value}',
    '{name} equals {value}',
    '{name} is {value}',
    '{name} is set to {value}'
]

conditions_with_2_trading_series = {
    1: (crossover_conditions_up, 'CrossOverCondition'),
    2: (crossover_conditions_down, 'CrossOverCondition'),
    3: (greater_than_conditions, 'GreaterThanCondition'),
    4: (less_than_conditions, 'LessThanCondition'),
}

conditions_with_trading_series_and_number = {
    1: (uptrend_for_x_days_conditions, 'UptrendForXDaysCondition'),
    2: (downtrend_for_x_days_conditions, 'DowntrendForXDaysCondition'),
}

conditions_with_trading_series_and_2_numbers = {
    1: (change_of_x_percent_per_y_days_conditions, 'ChangeOfXPercentPerYDaysCondition')
}

conditions_with_trading_series_and_percentage = {
    1: (intra_interval_change_of_x_percent_conditions, 'IntraIntervalChangeOfXPercentCondition')
}

conditions_with_fib_levels = {
    1: (downtrend_fibonacci_retracement_conditions, 'DowntrendFibRetracementLevelCondition'),
    2: (uptrend_fibonacci_retracement_conditions, 'UptrendFibRetracementLevelCondition')
}

conditions_dict = {
    1: conditions_with_2_trading_series,
    2: conditions_with_trading_series_and_number,
    3: conditions_with_trading_series_and_2_numbers,
    4: conditions_with_trading_series_and_percentage,
    5: conditions_with_fib_levels
}


def process_one_condition(ticker: str):
    trading_series_index = random.randint(0, len(implemented_indicators) - 1)

    # Get rows of the trading series
    trading_series = implemented_indicators.iloc[trading_series_index]

    number_of_parameters_trading_series = len(trading_series['Parameters'].split()) - 1

    # Chose weather to use name or shortcut in prompt
    is_name_not_shortcut = random.choice([True, False])
    chosen_trading_series = trading_series['Indicator'] if is_name_not_shortcut else trading_series['Shortcut']

    const_number = -1
    # Check if the trading series is CONST
    if chosen_trading_series == '':
        # If the trading series is CONST, we need to use a number
        const_number = random.randint(1, 99)
        class_with_parameters = f"CONST({const_number}"
    else:
        class_with_parameters = f"{trading_series["Class_name"]}('{ticker}'"

    parameter_values = []

    # Deal with the parameters
    if number_of_parameters_trading_series > 0:
        number_of_parameters_trading_series = random.randint(0, number_of_parameters_trading_series)

        # Randomly choose parameters
        parameters = random.sample(trading_series['Parameters'].split()[1:], k=number_of_parameters_trading_series)

        for parameter in parameters:
            parameter_name, parameter_type = parameter.split(':')
            if parameter_type == 'int':
                parameter_value = random.randint(1, 99)
                parameter_values.append(
                    random.choice(parameter_equality_options).format(name=parameter_name, value=parameter_value))
            elif parameter_type == 'float':
                parameter_value = random.uniform(0.1, 99.9)
                parameter_values.append(
                    random.choice(parameter_equality_options).format(name=parameter_name, value=parameter_value))
            elif parameter_type == 'SmoothingType':
                parameter_value = random.choice([
                    SmoothingType.SMA.value,
                    SmoothingType.EMA.value,
                    SmoothingType.RMA.value,
                    SmoothingType.WMA.value
                ])
                parameter_values.append(f'smoothing type set to {parameter_value}')
            elif parameter_type == 'SourceType':
                parameter_value = random.choice([
                    SourceType.CLOSE.value,
                    SourceType.OPEN.value,
                    SourceType.HIGH.value,
                    SourceType.LOW.value,
                    SourceType.HLC3.value,
                    SourceType.HL2.value,
                    SourceType.OHLC4.value,
                    SourceType.HLCC4.value
                ])
                parameter_values.append(f'source set to {parameter_value}')

            elif parameter_type == 'bool':
                parameter_value = random.choice([True, False])
                parameter_values.append(
                    f'{parameter_name} is set to {parameter_value}')

            class_with_parameters += f', {parameter_name}={parameter_value}'

    # Finish the text
    final_text = chosen_trading_series \
        if const_number == -1\
        else f'{random.choice([const_number, f'{const_number} line', f'{const_number} level', f'line {const_number}'])}'
    if len(parameter_values) > 0:
        final_text += random.choice([' where ', ' with ', ' having '])
        final_text += ', '.join(parameter_values)

    # Finish the class with parameters
    class_with_parameters += ')'

    return final_text, class_with_parameters


def create_condition(ticker: str):
    condition_type = random.randint(1, len(conditions_dict))
    current_condition_dict = conditions_dict[condition_type]

    condition_number = random.randint(1, len(conditions_dict[condition_type]))
    possible_texts, class_name = current_condition_dict[condition_number]

    # Conditions with 2 trading series
    if condition_type == 1:
        # Randomly choose 2 trading series
        trading_series1_text, trading_series1_parameters = process_one_condition(ticker)
        trading_series2_text, trading_series2_parameters = process_one_condition(ticker)

        # Create text of the prompt
        body_of_condition = random.choice(possible_texts)
        body_of_condition = body_of_condition.format(indicator=trading_series1_text, value=trading_series2_text)

        # Create parameters of the class based of the condition_number
        if condition_number in [1, 3, 4]:
            # CrossOverCondition from down to up, GreaterThanCondition, LessThanCondition
            class_with_parameters = f"{class_name}(first_series={trading_series1_parameters}, second_series={trading_series2_parameters})"
        else:
            # CrossOverCondition from up to down, we have to switch the trading series
            class_with_parameters = f"{class_name}(first_series={trading_series2_parameters}, second_series={trading_series1_parameters})"
    # Conditions with trading series and a number
    elif condition_type == 2:
        trading_series_text, trading_series_parameters = process_one_condition(ticker)

        # Create text of the prompt
        body_of_condition = random.choice(possible_texts)
        number_of_days = random.randint(1, 99)
        body_of_condition = body_of_condition.format(indicator=trading_series_text, days=number_of_days)

        # Create parameters of the class based of the condition_number
        class_with_parameters = f"{class_name}(series={trading_series_parameters}, number_of_days={number_of_days})"
    # Conditions with trading series and 2 numbers
    elif condition_type == 3:
        trading_series_text, trading_series_parameters = process_one_condition(ticker)

        # Create text of the prompt
        body_of_condition = random.choice(possible_texts)
        percent = random.uniform(0.1, 99.9)
        number_of_days = random.randint(1, 99)
        body_of_condition = body_of_condition.format(indicator=trading_series_text, percent=percent, days=number_of_days)

        # Create parameters of the class based of the condition_number
        class_with_parameters = f"{class_name}(series={trading_series_parameters}, percent={percent}, number_of_days={number_of_days})"
    # Conditions with trading series and percentage
    elif condition_type == 4:
        trading_series_text, trading_series_parameters = process_one_condition(ticker)

        # Create text of the prompt
        body_of_condition = random.choice(possible_texts)
        percent = random.uniform(0.1, 99.9)
        body_of_condition = body_of_condition.format(indicator=trading_series_text, percent=percent)

        # Create parameters of the class based of the condition_number
        class_with_parameters = f"{class_name}(series={trading_series_parameters}, percent={percent}')"
    # Conditions with fibonacci levels
    elif condition_type == 5:
        trading_series_text, trading_series_parameters = process_one_condition(ticker)

        # Create text of the prompt
        body_of_condition = random.choice(possible_texts)
        level = random.choice([
            FibonacciLevels.LEVEL_0,
            FibonacciLevels.LEVEL_23_6,
            FibonacciLevels.LEVEL_38_2,
            FibonacciLevels.LEVEL_50,
            FibonacciLevels.LEVEL_61_8,
            FibonacciLevels.LEVEL_100
        ])
        body_of_condition = body_of_condition.format(indicator=trading_series_text, level=level.value)

        # Create parameters of the class based of the condition_number
        class_with_parameters = f"{class_name}(series={trading_series_parameters}, level={level}')"
    else:
        raise ValueError("Invalid condition type")

    return body_of_condition, class_with_parameters

# TODO add tests for this utility
def build_logical_expression(ops, words):
    and_groups = []
    current_group = [words[0]]

    for i, op in enumerate(ops):
        if op == "and":
            current_group.append(words[i + 1])
        else:  # "or"
            and_groups.append(current_group if len(current_group) > 1 else current_group[0])
            current_group = [words[i + 1]]

    and_groups.append(current_group if len(current_group) > 1 else current_group[0])

    # Construct the formatted logical expression
    if len(and_groups) == 1:
        structured_expression = (
            f"AND({', '.join(and_groups[0])})" if isinstance(and_groups[0], list) else and_groups[0]
        )
    else:
        structured_expression = f"OR({', '.join(['AND(' + ', '.join(group) + ')' if isinstance(group, list) else group for group in and_groups])})"

    # Construct the simple concatenation expression
    simple_expression = " ".join(word if i == 0 else f"{ops[i-1]} {word}" for i, word in enumerate(words))

    return structured_expression, simple_expression


def create_training_data():
    training_data = []

    # Load tickers with company names
    sp500_tickers = pd.read_csv('sp500.csv')

    # Load implemented indicators
    #implemented_indicators = pd.read_csv('indicators.csv')

    number_of_training_data = 1
    for i in range(number_of_training_data):
        # Ticker
        ticker_index = random.randint(0, len(sp500_tickers) - 1)
        ticker_not_company = random.choice([True, False])
        # Always uses ticker as Strategy parameter
        ticker_parameter = sp500_tickers['Ticker'][ticker_index]
        # Can use company name and ticker in a prompt
        if ticker_not_company:
            chosen_ticker = ticker_parameter
        else:
            chosen_ticker = sp500_tickers['Company Name'][ticker_index]

        # Strategy type
        strategy_type = {
            'long': PositionTypeEnum.LONG,
            'short': PositionTypeEnum.SHORT,
            'long-short combination': PositionTypeEnum.LONG_SHORT_COMBINED,
            '': PositionTypeEnum.LONG # Default when no strategy type is specified
        }

        chosen_strategy_type = random.choice(list(strategy_type.keys()))
        strategy_type_parameter = strategy_type[chosen_strategy_type]

        # Buy condition
        number_of_buy_conditions = random.randint(1, 4)
        buy_conditions = [create_condition(ticker_parameter) for _ in range(number_of_buy_conditions)]

        # Sell condition
        number_of_sell_conditions = random.randint(1, 4)
        sell_conditions = [create_condition(ticker_parameter) for _ in range(number_of_sell_conditions)]

        # Connect conditions with logical operators
        # TODO think about if then else conditions
        logical_operators = ['and', 'or']

        # Logical operators between buy conditions
        buy_logical_operators = random.choices(logical_operators, k=number_of_buy_conditions - 1)

        # Logical operators between sell conditions
        sell_logical_operators = random.choices(logical_operators, k=number_of_sell_conditions - 1)

        # Build logical expressions
        buy_conditions_text, buy_conditions_parameters = build_logical_expression(buy_logical_operators, [condition[0] for condition in buy_conditions])
        sell_conditions_text, sell_conditions_parameters = build_logical_expression(sell_logical_operators, [condition[0] for condition in sell_conditions])






        buy_sell_action_condition = random.choice(buy_sell_action_conditions)
        crossover_condition_up = random.choice(crossover_conditions_up)
        crossover_condition_down = random.choice(crossover_conditions_down)
        change_of_x_percent_per_y_days_condition = random.choice(change_of_x_percent_per_y_days_conditions)
        intra_interval_change_of_x_percent_condition = random.choice(intra_interval_change_of_x_percent_conditions)
        greater_than_condition = random.choice(greater_than_conditions)
        less_than_condition = random.choice(less_than_conditions)
        downtrend_for_x_days_condition = random.choice(downtrend_for_x_days_conditions)
        uptrend_for_x_days_condition = random.choice(uptrend_for_x_days_conditions)
        downtrend_fibonacci_retracement_condition = random.choice(downtrend_fibonacci_retracement_conditions)
        uptrend_fibonacci_retracement_condition = random.choice(uptrend_fibonacci_retracement_conditions)

        prompt_start = random.choice(prompt_starts).format(strategy_type=strategy_type, ticker=chosen_ticker)

        training_data.append({
            'prompt_start': prompt_start,
            'buy_sell_action_condition': buy_sell_action_condition,
            'crossover_condition_up': crossover_condition_up,
            'crossover_condition_down': crossover_condition_down,
            'change_of_x_percent_per_y_days_condition': change_of_x_percent_per_y_days_condition,
            'intra_interval_change_of_x_percent_condition': intra_interval_change_of_x_percent_condition,
            'greater_than_condition': greater_than_condition,
            'less_than_condition': less_than_condition,
            'downtrend_for_x_days_condition': downtrend_for_x_days_condition,
            'uptrend_for_x_days_condition': uptrend_for_x_days_condition,
            'downtrend_fibonacci_retracement_condition': downtrend_fibonacci_retracement_condition,
            'uptrend_fibonacci_retracement_condition': uptrend_fibonacci_retracement_condition
        })

    return training_data

create_training_data()