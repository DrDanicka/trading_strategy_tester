import pandas as pd

def rsi(df: pd.DataFrame, column: str, length: int = 14) -> pd.Series:
    delta = df[column].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=length).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=length).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

