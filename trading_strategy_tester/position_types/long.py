import pandas as pd

from trading_strategy_tester.position_types.position_type import PositionType


class Long(PositionType):

    def clean_buy_sell_columns(self, df: pd.DataFrame):
        df['Long'] = None
        df['Short'] = None

        bought = False

        for index, row in df.iterrows():
            # If there is only True value to BUY
            if not bought and row['BUY'] and not row['SELL']:
                bought = True
                df.at[index, 'Long'] = 'LongEntry'
            # If there is True value to SELL
            elif bought and row['SELL']:
                bought = False
                df.at[index, 'BUY'] = False
                df.at[index, 'Long'] = 'LongExit'
            else:
                df.at[index, 'BUY'] = False
                df.at[index, 'SELL'] = False

        if bought:
            if not df.loc[df.index[-1], 'BUY']:
                df.loc[df.index[-1], 'SELL'] = True
                df.at[df.index[-1], 'Long'] = 'LongExit'
            else:
                # Set last index of BUY to False
                df.loc[df.index[-1], 'BUY'] = False
                df.at[df.index[-1], 'Long'] = None