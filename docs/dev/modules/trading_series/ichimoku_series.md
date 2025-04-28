
# Ichimoku Trading Series

The `Ichimoku` trading series provides various components of the Ichimoku Kinko Hyo system, a comprehensive trading framework offering trend direction, momentum, and support/resistance levels.

---

# `ICHIMOKU_BASE` - Ichimoku Base Line

Represents the Base Line (Kijun-sen) — a key slower-moving line in the Ichimoku system.

## Parameters

```python
ICHIMOKU_BASE(
    ticker: str,
    length: int = 26
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol (e.g., `"AAPL"`).
- **`length`** (`int`):  
  Lookback period for calculation. Default is 26.

## Description

- Midpoint between the highest high and lowest low over the past `length` periods.
- Often used as a trailing stop or dynamic support/resistance.

## Example Usage

```python
ICHIMOKU_BASE(ticker="AAPL", length=26)
```

---

# `ICHIMOKU_CONVERSION` - Ichimoku Conversion Line

Represents the Conversion Line (Tenkan-sen) — a faster-reacting line compared to the Base Line.

## Parameters

```python
ICHIMOKU_CONVERSION(
    ticker: str,
    length: int = 9
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol.
- **`length`** (`int`):  
  Lookback period for calculation. Default is 9.

## Description

- Midpoint between the highest high and lowest low over the past `length` periods.
- Useful for identifying short-term trend changes.

## Example Usage

```python
ICHIMOKU_CONVERSION(ticker="AAPL", length=9)
```

---

# `ICHIMOKU_LEADING_SPAN_A` - Ichimoku Leading Span A

Represents Senkou Span A — one of the two edges of the Kumo (cloud).

## Parameters

```python
ICHIMOKU_LEADING_SPAN_A(
    ticker: str,
    displacement: int = 26
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol.
- **`displacement`** (`int`):  
  Forward shift into the future. Default is 26.

## Description

- Average of the Conversion Line and Base Line.
- Plotted `displacement` periods ahead to form one edge of the cloud.

## Example Usage

```python
ICHIMOKU_LEADING_SPAN_A(ticker="AAPL", displacement=26)
```

---

# `ICHIMOKU_LEADING_SPAN_B` - Ichimoku Leading Span B

Represents Senkou Span B — the second edge of the Kumo.

## Parameters

```python
ICHIMOKU_LEADING_SPAN_B(
    ticker: str,
    length: int = 52,
    displacement: int = 26
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol.
- **`length`** (`int`):  
  Lookback period for Span B. Default is 52.
- **`displacement`** (`int`):  
  Forward shift into the future. Default is 26.

## Description

- Midpoint between the highest high and lowest low over the last `length` periods.
- Forms the second boundary of the cloud (Kumo).

## Example Usage

```python
ICHIMOKU_LEADING_SPAN_B(ticker="AAPL", length=52, displacement=26)
```

---

# `ICHIMOKU_LAGGING_SPAN` - Ichimoku Lagging Span

Represents the Lagging Span (Chikou Span) — a backward-shifted closing price.

## Parameters

```python
ICHIMOKU_LAGGING_SPAN(
    ticker: str,
    displacement: int = 26
)
```

- **`ticker`** (`str`):  
  Asset ticker symbol.
- **`displacement`** (`int`):  
  Number of periods the close is shifted backward. Default is 26.

## Description

- Closing price shifted back `displacement` periods.
- Used for confirmation of trend direction.

## Example Usage

```python
ICHIMOKU_LAGGING_SPAN(ticker="AAPL", displacement=26)
```
