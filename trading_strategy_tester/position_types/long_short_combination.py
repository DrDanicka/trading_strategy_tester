import pandas as pd

from trading_strategy_tester.position_types.position_type import PositionType


class LongShortCombination(PositionType):
    def clean_buy_sell_columns(self, df: pd.DataFrame):
        df['Long'] = None
        df['Short'] = None

        bought = False
        sold = False

        for index, row in df.iterrows():
            # If either of Buy or Sell was executed
            if row['BUY'] or row['SELL']:
                # If the stock is not bought or sold yet, so it is just beginning
                if not bought and not sold:
                    # If its BUY
                    if row['BUY'] and not row['SELL']:
                        bought = True
                        df.at[index, 'Long'] = 'LongEntry'
                    # If its SELL
                    elif row['SELL'] and not row['BUY']:
                        sold = True
                        df.at[index, 'Short'] = 'ShortEntry'

                # If the stock is bought
                elif bought:
                    if row['SELL'] and not row['BUY']:
                        bought = False
                        sold = True
                        df.at[index, 'Long'] = 'LongExit'
                        df.at[index, 'Short'] = 'ShortEntry'
                    else:
                        df.at[index, 'BUY'] = False
                        df.at[index, 'SELL'] = False

                # If the stock is sold
                elif sold:
                    if row['BUY'] and not row['SELL']:
                        sold = False
                        bought = True
                        df.at[index, 'Short'] = 'ShortExit'
                        df.at[index, 'Long'] = 'LongEntry'
                    else:
                        df.at[index, 'BUY'] = False
                        df.at[index, 'SELL'] = False


        # In the end:
        if bought:
            if not df.loc[df.index[-1], 'BUY']:
                df.loc[df.index[-1], 'SELL'] = True
                df.at[df.index[-1], 'Long'] = 'LongExit'
            else:
                # Set last index of BUY to False
                df.at[df.index[-1], 'Long'] = None

        if sold:
            if not df.loc[df.index[-1], 'SELL']:
                df.loc[df.index[-1], 'BUY'] = True
                df.loc[df.index[-1], 'Short'] = 'ShortExit'
            else:
                # Set  last index of SELL to False
                df.at[df.index[-1], 'Short'] = None