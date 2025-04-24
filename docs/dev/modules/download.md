
# `DownloadModule` — Financial Data Download Module

The `DownloadModule` provides a flexible and configurable way to download and cache historical market data using the Yahoo Finance API via the `yfinance` library. It supports both time-window (`start_date` to `end_date`) and period-based downloads and ensures data is reused from disk when available.

---

## Class: `DownloadModule`

### Constructor

```python
DownloadModule(
    start_date: datetime = datetime(2024, 1, 1),
    end_date: datetime = datetime.today(),
    interval: Interval = Interval.ONE_DAY,
    period: Period = Period.NOT_PASSED
)
```

**Parameters:**
- `start_date`: Start date for data download (used if `period` is `NOT_PASSED`)
- `end_date`: End date for data download
- `interval`: Granularity of data. Supported intervals are linked [here](TODO ADD LINK TO INTERVAL).
- `period`: Predefined period. Period has higher priority than `start_date` and `end_date`. So if not `NOT_PASSED`, it will be used for the download. Supported periods are linked [here](TODO ADD LINK TO PERIOD).

---

## Methods

###  `download_save_and_return_ticker(ticker: str, filepath: str, datetime_type: str) -> pd.DataFrame`

Downloads market data for the given `ticker` using the specified date method, saves it as a CSV, and returns it as a `DataFrame`.

---

### `return_cached_or_download_date(ticker: str) -> pd.DataFrame`

Returns cached data if exists, otherwise downloads it using the date range from `start_date` to `end_date`.

File is cached at:

```
_data/{ticker}_{start_date}_{end_date}_{interval}.csv
```

---

### `return_cached_or_download_period(ticker: str) -> pd.DataFrame`

Returns cached data if available or downloads data using the predefined `period`.

File is cached at:

```
_data/{ticker}_{period}_{interval}.csv
```

---

###  `download_ticker(ticker: str) -> pd.DataFrame`

High-level function that automatically determines whether to download by period or by date, based on the `period` setting.

---

## Caching Behavior

- Cached files are stored under a `_data/` directory inside the module path
- Prevents redundant downloads for the same ticker during a strategy execution run
- Uses descriptive filenames based on ticker and parameters
