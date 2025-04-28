
# `BBP` — Bull and Bear Power Trading Series

The `BBP` trading series represents the Bull and Bear Power (BBP) indicator, which helps assess the relative positioning of the price within the Bollinger Bands. It is a measure of market momentum and volatility.

It is built upon the [Bull and Bear Power indicator](https://github.com/DrDanicka/trading_strategy_tester/blob/main/trading_strategy_tester/indicators/momentum/bbp.py) implementation from the [indicators module](../indicators.md).

---

## Parameters

```python
BBP(
    ticker: str,
    length: int = 13
)
```

- **`ticker`** (`str`): The symbol of the asset (e.g., `"AAPL"`).

- **`length`** (`int`): The period used to calculate the underlying Bollinger Bands. Default is 13, which is a common setting.

---

## Description

- Positive BBP values indicate bulls have greater market power.
- Negative BBP values indicate bears have greater market power.
- The farther BBP moves from zero, the stronger the dominance of either bulls or bears.

---

## Example Usage

```python
BBP(
    ticker="AAPL",
    length=13
)
```

This creates a BBP Trading Series for AAPL using a 13-period setting.
