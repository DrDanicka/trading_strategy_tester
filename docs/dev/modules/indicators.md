
# `indicators` — Technical Indicators Module

This module contains categorized implementations of technical indicators used across trading strategies. These indicators are grouped into submodules by type: momentum, trend, volatility, overlap, volume, and candlestick patterns.

---

## Module Structure

### 1. Momentum Indicators
*Located in [`trading_strategy_tester/indicators/momentum/`](../../../trading_strategy_tester/indicators/momentum)*

- [`willr.py`](../../../trading_strategy_tester/indicators/momentum/willr.py) — Williams %R
- [`macd.py`](../../../trading_strategy_tester/indicators/momentum/macd.py) — Moving Average Convergence Divergence
- [`cmo.py`](../../../trading_strategy_tester/indicators/momentum/cmo.py) — Chande Momentum Oscillator
- [`roc.py`](../../../trading_strategy_tester/indicators/momentum/roc.py) — Rate of Change
- [`bbp.py`](../../../trading_strategy_tester/indicators/momentum/bbp.py) — Bull and Bear Power
- [`cci.py`](../../../trading_strategy_tester/indicators/momentum/cci.py) — Commodity Channel Index
- [`uo.py`](../../../trading_strategy_tester/indicators/momentum/uo.py) — Ultimate Oscillator
- [`stoch.py`](../../../trading_strategy_tester/indicators/momentum/stoch.py) — Stochastic %K and %D Indicators
- [`cop.py`](../../../trading_strategy_tester/indicators/momentum/cop.py) — Coppock Curve
- [`rsi.py`](../../../trading_strategy_tester/indicators/momentum/rsi.py) — Relative Strength Index
- [`trix.py`](../../../trading_strategy_tester/indicators/momentum/trix.py) — Triple Exponential Average
- [`momentum.py`](../../../trading_strategy_tester/indicators/momentum/momentum.py) — Momentum
- [`kst.py`](../../../trading_strategy_tester/indicators/momentum/kst.py) — Know Sure Thing
- [`dmi.py`](../../../trading_strategy_tester/indicators/momentum/dmi.py) — Directional Movement Index

---

### 2. Trend Indicators
*Located in [`trading_strategy_tester/indicators/trend/`](../../../trading_strategy_tester/indicators/trend)*

- [`mass.py`](../../../trading_strategy_tester/indicators/trend/mass.py) — Mass Index
- [`adx.py`](../../../trading_strategy_tester/indicators/trend/adx.py) — Average Directional Index
- [`aroon.py`](../../../trading_strategy_tester/indicators/trend/aroon.py) — Aroon Up and Down Indicators
- [`dpo.py`](../../../trading_strategy_tester/indicators/trend/dpo.py) — Detrended Price Oscillator

---

### 3. Volatility Indicators
*Located in [`trading_strategy_tester/indicators/volatility/`](../../../trading_strategy_tester/indicators/volatility)*

- [`dc.py`](../../../trading_strategy_tester/indicators/volatility/dc.py) — Donchian Channels
- [`bb.py`](../../../trading_strategy_tester/indicators/volatility/bb.py) — Bollinger Bands
- [`atr.py`](../../../trading_strategy_tester/indicators/volatility/atr.py) — Average True Range
- [`chop.py`](../../../trading_strategy_tester/indicators/volatility/chop.py) — Choppiness Index
- [`kc.py`](../../../trading_strategy_tester/indicators/volatility/kc.py) — Keltner Channels

---

### 4. Overlap Indicators
*Located in [`trading_strategy_tester/indicators/overlap/`](../../../trading_strategy_tester/indicators/overlap)*

- [`ema.py`](../../../trading_strategy_tester/indicators/overlap/ema.py) — Exponential Moving Average
- [`sma.py`](../../../trading_strategy_tester/indicators/overlap/sma.py) — Simple Moving Average
- [`ichimoku.py`](../../../trading_strategy_tester/indicators/overlap/ichimoku.py) — Ichimoku Cloud components

---

### 5. Volume-Based Indicators
*Located in `indicators/volume/`*

- `pvt.py` — Price Volume Trend
- `efi.py` — Elder Force Index
- `pvi.py` — Positive Volume Index
- `mfi.py` — Money Flow Index
- `obv.py` — On Balance Volume
- `eom.py` — Ease of Movement
- `chaikin_osc.py` — Chaikin Oscillator
- `cmf.py` — Chaikin Money Flow

---

### 6. 🕯️ Candlestick Patterns
*Located in `indicators/candlestick_patterns/`*

- `hammer.py` — Hammer Pattern

---

This modular structure allows easy extension and targeted imports for strategy evaluation and indicator-based conditions.
