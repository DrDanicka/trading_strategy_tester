
# `TradingSeries` — Series for Trading Strategies Module

The `TradingSeries` module provides a broad collection of classes that represent various financial indicators, price points, candlestick patterns, and volume-based signals. These series can be used inside conditions to define complex trading strategies.

Most of the `TradingSeries` build upon the indicators from [indicators module](indicators.md), but they are designed to be used in conditions with other `TradingSeries` classes.

All `TradingSeries` classes inherit from the abstract base class `TradingSeries`, which defines a consistent interface for calculating and serializing the series.

---

## Abstract Base: `TradingSeries`

All trading series inherit from this abstract class, ensuring a consistent interface for indicator calculation.

```python
class TradingSeries(ABC):
    def __init__(self, ticker: str):
        self._ticker = ticker  # Store the ticker symbol as a protected attribute

    @property
    @abstractmethod
    def ticker(self) -> str:
        pass

    @abstractmethod
    def get_data(self, downloader: DownloadModule, df: pd.DataFrame) -> pd.Series:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
```

- `ticker() -> str`: Returns the ticker symbol associated with the series.
- `get_data(downloader: DownloadModule, df: pd.DataFrame) -> pd.Series`: Fetches the data for the series using the provided downloader and DataFrame.
- `get_name() -> str`: Returns a human-readable name of the series.
- `to_dict() -> dict`: Serializes the series into a dictionary for testing purposes.

---

# Available Trading Series

Below is a complete list of all implemented TradingSeries classes in alphabetical order. There is a link for each class to its documentation, which includes a description of the class and its parameters

- [`ADX`](trading_series/adx.md) - Average Directional Index Trading Series
- [`AROON_DOWN`](trading_series/aroon_down.md) - Aroon Down Trading Series
- [`AROON_UP`](trading_series/aroon_up.md) - Aroon Up Trading Series
- [`ATR`](trading_series/atr.md) - Average True Range Trading Series
- [`BBP`](trading_series/bbp.md) - Bull and Bear Power Trading Series
- [`BB_LOWER`](trading_series/bb_lower.md) - Bollinger Bands Lower Band Trading Series
- [`BB_MIDDLE`](trading_series/bb_middle.md) - Bollinger Bands Middle Band Trading Series
- [`BB_UPPER`](trading_series/bb_upper.md) - Bollinger Bands Upper Band Trading Series
- [`CCI`](trading_series/cci.md) - Commodity Channel Index Trading Series
- [`CCI_SMOOTHENED`](trading_series/cci_smoothened.md) - Smoothed Commodity Channel Index Trading Series
- [`CHAIKIN_OSC`](trading_series/chaikin_osc.md) - Chaikin Oscillator Trading Series
- [`CHOP`](trading_series/chop.md) - Choppiness Index Trading Series
- [`CLOSE`](trading_series/default.md#close-closing-price-trading-series) - Closing Price Trading Series
- [`CMF`](trading_series/cmf.md) - Chaikin Money Flow Trading Series
- [`CMO`](trading_series/cmo.md) - Chande Momentum Oscillator Trading Series
- [`CONST`](trading_series/default.md#const-constant-value-trading-series) - Constant Value Trading Series
- [`COPPOCK`](trading_series/coppock.md) - Coppock Curve Trading Series
- [`DC_BASIS`](trading_series/dc_basis.md) - Donchian Channel Basis Trading Series
- [`DC_LOWER`](trading_series/dc_lower.md) - Donchian Channel Lower Band Trading Series
- [`DC_UPPER`](trading_series/dc_upper.md) - Donchian Channel Upper Band Trading Series
- [`DI_MINUS`](trading_series/di_minus.md) - Directional Movement Index Minus Trading Series
- [`DI_PLUS`](trading_series/di_plus.md) - Directional Movement Index Plus Trading Series
- [`DPO`](trading_series/dpo.md) - Detrended Price Oscillator Trading Series
- [`EFI`](trading_series/efi.md) - Elder Force Index Trading Series
- [`EMA`](trading_series/ma.md#ema-exponential-moving-average-trading-series) - Exponential Moving Average Trading Series
- [`EOM`](trading_series/eom.md) - Ease of Movement Trading Series
- [`HAMMER`](trading_series/hammer.md) - Hammer Candlestick Pattern Trading Series
- [`HIGH`](trading_series/default.md#high-highest-price-trading-series) - Highest Price Trading Series
- [`ICHIMOKU_BASE`](trading_series/ichimoku_series.md#ichimoku_base-ichimoku-base-line) - Ichimoku Base Line (Kijun-sen)
- [`ICHIMOKU_CONVERSION`](trading_series/ichimoku_series.md#ichimoku_conversion-ichimoku-conversion-line) - Ichimoku Conversion Line (Tenkan-sen)
- [`ICHIMOKU_LAGGING_SPAN`](trading_series/ichimoku_series.md#ichimoku_lagging_span-ichimoku-lagging-span) - Ichimoku Lagging Span (Chikou Span)
- [`ICHIMOKU_LEADING_SPAN_A`](trading_series/ichimoku_series.md#ichimoku_leading_span_a-ichimoku-leading-span-a) - Ichimoku Leading Span A (Senkou Span A)
- [`ICHIMOKU_LEADING_SPAN_B`](trading_series/ichimoku_series.md#ichimoku_leading_span_b-ichimoku-leading-span-b) - Ichimoku Leading Span B (Senkou Span B)
- [`KC_LOWER`](trading_series/kc_lower.md) - Keltner Channel Lower Band Trading Series
- [`KC_UPPER`](trading_series/kc_upper.md) - Keltner Channel Upper Band Trading Series
- [`KST`](trading_series/kst.md) - Know Sure Thing Trading Series
- [`KST_SIGNAL`](trading_series/kst_signal.md) - Know Sure Thing Signal Line Trading Series
- [`LOW`](trading_series/default.md#low-lowest-price-trading-series) - Lowest Price Trading Series
- [`MACD`](trading_series/macd.md) - Moving Average Convergence Divergence Trading Series
- [`MACD_SIGNAL`](trading_series/macd_signal.md) - Moving Average Convergence Divergence Signal Line Trading Series
- [`MASS`](trading_series/mass.md) - Mass Index Trading Series
- [`MFI`](trading_series/mfi.md) - Money Flow Index Trading Series
- [`MOMENTUM`](trading_series/momentum.md) - Momentum Trading Series
- [`OBV`](trading_series/obv.md) - On Balance Volume Trading Series
- [`OPEN`](trading_series/default.md#open-opening-price-trading-series) - Opening Price Trading Series
- [`PERCENT_D`](trading_series/percent_d.md) - Stochastic %D Trading Series
- [`PERCENT_K`](trading_series/percent_k.md) - Stochastic %K Trading Series
- [`PVI`](trading_series/pvi.md) - Positive Volume Index Trading Series
- [`PVT`](trading_series/pvt.md) - Price Volume Trend Trading Series
- [`ROC`](trading_series/roc.md) - Rate of Change Trading Series
- [`RSI`](trading_series/rsi.md) - Relative Strength Index Trading Series
- [`SMA`](trading_series/ma.md#sma-simple-moving-average-trading-series) - Simple Moving Average Trading Series
- [`TRIX`](trading_series/trix.md) - Triple Exponential Average Trading Series
- [`UO`](trading_series/uo.md) - Ultimate Oscillator Trading Series
- [`VOLUME`](trading_series/default.md#volume-volume-trading-series) - Volume Trading Series
- [`WILLR`](trading_series/willr.md) - Williams %R Trading Series