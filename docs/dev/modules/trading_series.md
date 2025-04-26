
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
- [`CLOSE`](trading_series/close.md)
- [`CMF`](trading_series/cmf.md) - Chaikin Money Flow Trading Series
- [`CMO`](trading_series/cmo.md) - Chande Momentum Oscillator Trading Series
- [`CONST`](trading_series/const.md)
- [`COPPOCK`](trading_series/coppock.md) - Coppock Curve Trading Series
- [`DC_BASIS`](trading_series/dc_basis.md) - Donchian Channel Basis Trading Series
- [`DC_LOWER`](trading_series/dc_lower.md) - Donchian Channel Lower Band Trading Series
- [`DC_UPPER`](trading_series/dc_upper.md) - Donchian Channel Upper Band Trading Series
- [`DI_MINUS`](trading_series/di_minus.md)
- [`DI_PLUS`](trading_series/di_plus.md)
- [`DPO`](trading_series/dpo.md)
- [`EFI`](trading_series/efi.md)
- [`EMA`](trading_series/ema.md)
- [`EOM`](trading_series/eom.md)
- [`HAMMER`](trading_series/hammer.md)
- [`HIGH`](trading_series/high.md)
- [`ICHIMOKU_BASE`](trading_series/ichimoku_base.md)
- [`ICHIMOKU_CONVERSION`](trading_series/ichimoku_conversion.md)
- [`ICHIMOKU_LAGGING_SPAN`](trading_series/ichimoku_lagging_span.md)
- [`ICHIMOKU_LEADING_SPAN_A`](trading_series/ichimoku_leading_span_a.md)
- [`ICHIMOKU_LEADING_SPAN_B`](trading_series/ichimoku_leading_span_b.md)
- [`KC_LOWER`](trading_series/kc_lower.md)
- [`KC_UPPER`](trading_series/kc_upper.md)
- [`KST`](trading_series/kst.md)
- [`KST_SIGNAL`](trading_series/kst_signal.md)
- [`LOW`](trading_series/low.md)
- [`MACD`](trading_series/macd.md)
- [`MACD_SIGNAL`](trading_series/macd_signal.md)
- [`MASS`](trading_series/mass.md)
- [`MFI`](trading_series/mfi.md)
- [`MOMENTUM`](trading_series/momentum.md)
- [`OBV`](trading_series/obv.md)
- [`OPEN`](trading_series/open.md)
- [`PERCENT_D`](trading_series/percent_d.md)
- [`PERCENT_K`](trading_series/percent_k.md)
- [`PVI`](trading_series/pvi.md)
- [`PVT`](trading_series/pvt.md)
- [`ROC`](trading_series/roc.md)
- [`RSI`](trading_series/rsi.md)
- [`SMA`](trading_series/sma.md)
- [`TESTING`](trading_series/testing.md)
- [`TRIX`](trading_series/trix.md)
- [`UO`](trading_series/uo.md)
- [`VOLUME`](trading_series/volume.md)
- [`WILLR`](trading_series/willr.md)