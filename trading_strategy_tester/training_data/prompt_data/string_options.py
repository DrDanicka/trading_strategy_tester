prompt_starts = [
    'Could you develop a {strategy_type} strategy for {ticker} that ',
    'Would you be able to create a {strategy_type} strategy for {ticker} that ',
    'Please design a strategy for {ticker} that ',
    'Can you generate a {strategy_type} strategy for {ticker} that ',
    'Would you mind crafting a {strategy_type} strategy for {ticker} that ',
    'Could you outline a {strategy_type} strategy for {ticker} that ',
    'I need a {strategy_type} strategy for {ticker} that ',
    'Can you help formulate a {strategy_type} strategy for {ticker} that ',
    'Would you kindly create a {strategy_type} strategy for {ticker} that ',
    'Can you provide a {strategy_type} strategy for {ticker} that ',
    'Might you be able to develop a {strategy_type} strategy for {ticker} that ',
    'Could you draft a {strategy_type} trading strategy for {ticker} that ',
    'Please come up with a {strategy_type} strategy for {ticker} that ',
    'Can you structure a {strategy_type} strategy for {ticker} that ',
    'Would you be willing to create a {strategy_type} strategy for {ticker} that ',
    'Can you tailor a {strategy_type} strategy for {ticker} that ',
    'I’m looking for a {strategy_type} strategy for {ticker} that ',
    'Could you put together a {strategy_type} strategy for {ticker} that ',
    'Is it possible for you to create a {strategy_type} strategy for {ticker} that '
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
    '{action} when the {condition} is applicable',
    '{action} when the {condition} is apposite',
    '{action} when the {condition} is befitting',
    '{action} when the {condition} is felicitous',
    '{action} when the {condition} is nice',
    '{action} when the {condition} is proper',
    '{action} when the {condition} is right',
    '{action} when the {condition} is seemly',
    '{action} when the {condition} is to the point',
]

crossover_conditions = [
    '{indicator} crossed above {value}',
    '{indicator} rises above {value}',
    '{indicator} climbs above {value}',
    '{indicator} jumps above {value}',
    '{indicator} moves above {value}',
    '{indicator} goes above {value}',
    '{indicator} exceeds {value}',
    '{indicator} surpasses {value}',
    '{indicator} breaks through {value}',
    '{indicator} goes beyond {value}',
    '{indicator} crossed up {value}',
    '{indicator} crosses over {value}'
]

crossunder_conditions = [
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
    '{indicator} sways by {percent} percent over {days} days',
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
    '{indicator} sways by {percent} percent within a interval',
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

buy_actions = ['buy', 'buys', 'purchase', 'purchases', 'acquire', 'acquires',
               'go long', 'goes long', 'take a long position', 'takes a long position', 'longs']

sell_actions = ['sell', 'sells', 'sell off', 'sells off', 'sell out', 'sells out',
                'go short', 'goes short', 'take a short position', 'takes a short position', 'shorts']

stop_loss_normal = [
    'Set normal stop-loss at {percentage}%',
    'Apply normal stop-loss at {percentage}%',
    'Use normal stop-loss at {percentage}%',
    'Set stop-loss at {percentage}%',
    'Set normal stop-loss at {percentage} percent',
    'Apply normal stop-loss at {percentage} percent',
    'Use normal stop-loss at {percentage} percent',
    'Set stop-loss at {percentage} percent',
    'Apply stop-loss at {percentage}%',
    'Use stop-loss at {percentage}%',
    'Set stop-loss at {percentage}%',
    'Set normal stop-loss at {percentage} percent',
    'Apply normal stop-loss at {percentage} percent'
]

stop_loss_trailing = [
    'Set trailing stop-loss at {percentage}%',
    'Apply trailing stop-loss at {percentage}%',
    'Use trailing stop-loss at {percentage}%',
    'Set trailing stop-loss at {percentage} percent',
    'Apply trailing stop-loss at {percentage} percent',
    'Use trailing stop-loss at {percentage} percent'
]

take_profit = [
    'Set take-profit at {percentage}%',
    'Apply take-profit at {percentage}%',
    'Use take-profit at {percentage}%',
    'Set take-profit at {percentage} percent',
    'Apply take-profit at {percentage} percent',
    'Use take-profit at {percentage} percent'
]

parameter_equality_options = [
    '{name} is equal to {value}',
    '{name} equals {value}',
    '{name} is {value}',
    '{name} is set to {value}'
]

dates = [
    'Set the {type} date to {year}-{month}-{day}',
    'Set the {type} date as {year}-{month}-{day}',
    'Set the {type} date equal to {year}-{month}-{day}',
    'Set {type} of the strategy to {year}-{month}-{day}',
    'Set the {type} date to {year}-{month}-{day} for the strategy'
]

periods = [
    'Set the period to {period}',
    'Set the period as {period}',
    'Set the period equal to {period}',
    'Set the period to {period} for the strategy',
    'Set the period as {period} for the strategy'
    'Set the period of the date to {period}'
]

intervals = [
    'Set the interval to {interval}',
    'Set the interval as {interval}',
    'Set the interval equal to {interval}',
    'Set the interval to {interval} for the data',
]

initial_capital = [
    'Set the initial capital to {capital}$',
    'I have {capital}$ as the initial capital',
    'I have {capital}$ to invest',
]

order_size_uds = [
    'Set order size per trade to {order_size} USD',
    'Set order size to {order_size} USD',
    'Set order size per trade to {order_size} dollars',
    'Set order size to {order_size} dollars',
    'Set order size per trade to {order_size}$',
    'Set order size to {order_size}$',
]

order_size_percent_of_equity = [
    'Set order size per trade to {order_size} percent of equity',
    'Set order size to {order_size} percent of equity'
]

order_size_contracts = [
    'Set order size to {order_size} contracts',
    'Go into every trade with {order_size} contracts',
    'Set order size per trade to {order_size} contracts',
    'Set order size to {order_size} contracts'
]

trade_commissions_money = [
    'Set trade commissions to {commissions}$',
    'Set commissions to {commissions}$',
    'Set trade commissions to {commissions} dollars',
    'Set commissions to {commissions} dollars',
]

trade_commissions_percentage = [
    'Set trade commissions to {commissions} percent',
    'Set commissions to {commissions} percent',
    'Set trade commissions to {commissions}%',
    'Set commissions to {commissions}%'
]