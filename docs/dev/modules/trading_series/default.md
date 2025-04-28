
# Default Trading Series

The `default_series` module provides basic fundamental trading series like Open, High, Low, Close, Volume, and constant values. These series are used to build simple conditions and combine with more complex indicators.

---

# `CLOSE` - Closing Price Trading Series

Represents the closing price of a given ticker.

## Parameters

```python
CLOSE(
    ticker: str
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol (e.g., `"AAPL"`).

## Description

- Retrieves the close prices for the given ticker from the historical dataset.
- Used in the majority of trading indicators and strategies.

## Example Usage

```python
CLOSE(ticker="AAPL")
```

---

# `OPEN` - Opening Price Trading Series

Represents the opening price of a given ticker.

## Parameters

```python
OPEN(
    ticker: str
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol (e.g., `"AAPL"`).

## Description

- Retrieves the opening prices for the given ticker from the historical dataset.

## Example Usage

```python
OPEN(ticker="AAPL")
```

---

# `HIGH` - Highest Price Trading Series

Represents the highest price reached during a trading period.

## Parameters

```python
HIGH(
    ticker: str
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol (e.g., `"AAPL"`).

## Description

- Retrieves the high prices for the given ticker from the historical dataset.

## Example Usage

```python
HIGH(ticker="AAPL")
```

---

# `LOW` - Lowest Price Trading Series

Represents the lowest price reached during a trading period.

## Parameters

```python
LOW(
    ticker: str
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol (e.g., `"AAPL"`).

## Description

- Retrieves the low prices for the given ticker from the historical dataset.

## Example Usage

```python
LOW(ticker="AAPL")
```

---

# `VOLUME` - Volume Trading Series

Represents the number of shares or contracts traded during a trading period.

## Parameters

```python
VOLUME(
    ticker: str
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol (e.g., `"AAPL"`).

## Description

- Retrieves the traded volume for the given ticker from the historical dataset.

## Example Usage

```python
VOLUME(ticker="AAPL")
```

---

# `CONST` - Constant Value Trading Series

Represents a constant value series, independent of the asset prices.

## Parameters

```python
CONST(
    const_number: int
)
```

- **`const_number`** (`int`):  
  A constant numeric value (e.g., 30, 70, 100).

## Description

- Useful for defining static thresholds in conditions (e.g., RSI crossing 70).
- Returns a constant series for comparison with dynamic indicators.

## Example Usage

```python
CONST(70)
```
