import pandas as pd

from trading_strategy_tester.position_types.position_type import PositionType


class Short(PositionType):

    def clean_buy_sell_columns(self, df: pd.DataFrame):
        df['Long'] = None
        df['Short'] = None

        sold = False

        for index, row in df.iterrows():
            # If there is only True value to SELL
            if not sold and row['SELL'] and not row['BUY']:
                sold = True
                df.at[index, 'Short'] = 'ShortEntry'
            # If there is True value to BUY
            elif sold and row['BUY']:
                sold = False
                df.at[index, 'SELL'] = False
                df.at[index, 'Short'] = 'ShortExit'
            else:
                df.at[index, 'BUY'] = False
                df.at[index, 'SELL'] = False

        if sold:
            if not df.loc[df.index[-1], 'SELL']:
                df.loc[df.index[-1], 'BUY'] = True
                df.loc[df.index[-1], 'Short'] = 'ShortExit'
            else:
                # Set  last index of SELL to False
                df.loc[df.index[-1], 'SELL'] = False
                df.at[df.index[-1], 'Short'] = None