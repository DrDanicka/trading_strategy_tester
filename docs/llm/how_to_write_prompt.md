# How to write prompts

When using LLMs to generate trading strategies, it is important to write clear and concise prompts that accurately describe the desired strategy. Here are some tips and examples to help you write effective prompts.

## Mandatory fields

In every strategy, there are 4 mandatory fields that need to be specified, and those are:

- **ticker**: The ticker symbol of the stock or asset you want to trade. For example, "AAPL" for Apple Inc. You can find those for every equity on [Yahoo Finance](https://finance.yahoo.com/).
- [**position_type**](../dev/modules/enums/position_type.md): The type of position you want to take. This can be either `LONG`, `SHORT`, or `LONG_SHORT_COMBINED`. If you do not specify this, the default value is `LONG`.
- [**buy_condition**](../dev/modules/conditions/index.md): The condition that triggers a buy signal. This can be any of the conditions available in the library and can be combined using logical operators.
- [**sell_condition**](../dev/modules/conditions/index.md): The condition that triggers a sell signal. This can be any of the conditions available in the library and can be combined using logical operators.

Those fields are mandatory, and the best practice is to start with them. So the first sentence of a prompt should be something like:
```
Can you please generate a strategy for AAPL where you buy when RSI moves 
above 30 and you sell when RSI crosses below 70.
```
Simple and clear. The model will understand that you want to create a strategy for AAPL and that you want to buy when RSI moves above 30 and sell when RSI crosses below 70. Position type is not specified, so the model will use the default value which is `LONG`.

Another and more complicated example of a prompt with mandatory fields:
```
Could you outline a long strategy for NVDA that sells off when the Ichinoku 
Conversion oscillates by 19.9 percent over 43 days or ATR changes by 95.02 
percent over 45 days and take a long position when the TRIX where length 
is equal to 26 varies by 13.6 percent within a interval.
```
Let's break this down:

- **ticker**: The ticker symbol is defined right at the beginning of the prompt, so the model will know that you want to create a strategy for ticker `NVDA`.
- **position_type**: The position type is defined as `long` in the prompt, so the model will know that you want to create a `LONG` strategy.
- **buy_condition**: The buy or long condition is defined as a second condition this time and it is:

```
take a long position when the TRIX where length is equal to 26 varies by 
13.6 percent within a interval.
```
This is still just one condition that can be exactly defined in the library as:
```
IntraIntervalChangeOfXPercentCondition(series=TRIX('NVDA', length=26), percent=13.6)
```
If you want to specify parameters of an indicator as in this example of `TRIX`, you should do that right after the name of the indicator. So in this example the model will know that you want to create a `TRIX` indicator with length equal to 26.

- **sell_condition**: The sell condition is defined as a first condition this time and it is:

```
sells off when the Ichinoku Conversion oscillates by 19.9 percent over 
43 days or ATR changes by 95.02 percent over 45 days
```
This is a combination of two conditions that are separated by `or` operator. The final condition will be:
```
OR(
    ChangeOfXPercentPerYDaysCondition(
        series=ICHIMOKU_CONVERSION('NVDA'),
        percent=19.9, 
        number_of_days=43
    ), 
    ChangeOfXPercentPerYDaysCondition(
        series=ATR('NVDA'), 
        percent=95.02, 
        number_of_days=45
    )
)    
```
As you can see all the parameters are specified in the prompt and the model will know that you want to create a `ChangeOfXPercentPerYDaysCondition` condition with the parameters specified in the prompt. If you don't specify parameters for indicators, the model will use default values for them.

## Optional fields

In addition to the mandatory fields, there are several optional fields that you can include in your prompt to customize your strategy further. You include them after the main sentence about conditions of entry and exit. Here are some examples of optional fields:

### [stop_loss](../dev/modules/strategy_parameters/stop_loss.md) and [take_profit](../dev/modules/strategy_parameters/take_profit.md)

You can specify the stop loss and take profit for the strategy. For example:
```
Apply stop-loss at 42.56 percent. Apply take-profit at 25.16 percent.
```

### start_date and end_date

You can specify the start and end date for the strategy. For example:
```
Set the start date to 2004-10-28. Set end of the strategy to 2024-10-4.
```

It's recommended to specify the date format as `YYYY-MM-DD` so the model will understand it better because this was the format of the training data.

### [interval](../dev/modules/enums/interval.md)

You can specify the interval for the strategy. For example:
```
Set the interval equal to 1 week.
```

### [period](../dev/modules/enums/period.md)

You can specify the period for the strategy. For example:
```
Set the period to 6 months for the strategy.
```
If the period is specified, the model will ignore the start and end date.

### initial_capital

You can specify the initial capital for the strategy. For example:
```
Set the initial capital to 1000 dollars.
```

### [order_size](../dev/modules/strategy_parameters/order_size.md)

You can specify the order size for the strategy. See what order sizes are available at [OrderSize](../dev/modules/strategy_parameters/order_size.md) documentation. For example:
```
Set order size per trade to 20 dollars.
```
This will set: `order_size=USD(value=20)`.

or

```
Set order size to 2 contracts.
```

This will set: `order_size=Contracts(value=2)`.

### [trade_commissions](../dev/modules/strategy_parameters/trade_commissions.md)

You can specify the trade commissions for the strategy. See what trade commissions are available at [TradeCommissions](../dev/modules/strategy_parameters/trade_commissions.md) documentation. For example:
```
Set trade commissions to 0.01 percent.
```
This will set: `trade_commissions=PercentageCommissions(value=0.01)`.

or

```
Set trade commissions to 0.5 dollars.
```
This will set: `trade_commissions=MoneyCommissions(value=0.5)`.

This is how you can write prompts for LLMs to generate trading strategies. Quick recap:

- Start with mandatory fields: `ticker`, `position_type`, `buy_condition`, and `sell_condition`. The best practice is to set them in the first sentence.
- Define optional fields after the first sentence. If you do not specify them, the model will use default values for them that you can find [here](../dev/modules/strategy.md).

## Examples of full prompts

```
Can you please generate a strategy for AAPL where you buy when RSI moves 
above 30 and you sell when RSI crosses below 70. Apply stop-loss at 10 percent. 
Set take-profit at 5 percent. Set the initial capital to 10000 dollars.
```

or 

```
Could you outline a long strategy for NVDA that sells off when the Ichinoku 
Conversion oscillates by 19.9 percent over 43 days or ATR changes by 95.02 
percent over 45 days and take a long position when the TRIX where length 
is equal to 26 varies by 13.6 percent within a interval. Set the start date 
to 2022-1-1 and set end of the strategy to 2024-1-1. Set trade commissions 
to 0.01 percent.
```

## Workflow

The expected workflow for generating trading strategies with an LLM is as follows:

1. **Choose a model**  
   Use any LLM to generate strategy prompts, but we **recommend using Llama 3.2**.  
   This is the fine-tuned model that generates **all parameters in a single step**.  
   It is both fast and produces good results.

2. **Generate the initial strategy**  
   Start by writing a clear prompt using the guidelines above.  
   Llama 3.2 will generate a complete draft of the strategy including both mandatory and optional fields.

3. **Review the result in the "Generated" tab**  
   Once the strategy is generated, inspect the output in the *Generated* tab.  
   This tab shows the parsed structure of the strategy that is simulated and validated.

4. **Decide on next steps**  
    - If the generated strategy looks good and matches your expectations, you can proceed directly.  
    - If the strategy is not fully aligned with your intent, you can **manually edit** the parameters resubmit as `Strategy object` in LLM selection.


## Performance note  

Generating strategies using LLMs can be time-consuming, especially when running models locally. On an Apple M3 Pro chip, a single query to the 3B model takes approximately **15 seconds**. On older GPUs like the NVIDIA 1070, the runtime is similar. However, on machines **without a dedicated GPU**, a single call to the 3B model can take up to **1 minute** or more.

In the case of the approach that generates strategy fields individually, **up to 12 models may run in parallel** (one per field). This means that on non-GPU systems, total generation time can stretch to **several minutes**. On systems with a capable GPU, this multi-model parallelism usually completes in **around one minute**.

Keep this in mind when choosing between full-strategy generation and per-field generation workflows.


## Important note at the end

It is highly recommended to work with the documentation of a [`Strategy`](../dev/modules/strategy.md) object to know what parameters are available for each condition and how to use them. You can also check the [TradingSeries](../dev/modules/trading_series.md) documentation to see what parameters are available for each indicator. The model will understand the prompt better if you specify the parameters in the prompt.

If you are not sure how to write something in the prompt, you can look at the file at this [link](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/training_data/prompt_data/string_options.py). There are some options on how to specify the parameters in the prompt. If you use the same patterns as in the file, the model will understand it better because those are the patterns that were used for training the model.