import os.path
import unittest
import pandas as pd
from datetime import datetime

from trading_strategy_tester.download.download_module import DownloadModule
from trading_strategy_tester.enums.source_enum import SourceType
from trading_strategy_tester.indicators.volume.efi import efi
from trading_strategy_tester.trading_series.efi_series.efi_series import EFI

class TestEFI(unittest.TestCase):

    def setUp(self):
        """
        Testing on AAPL stock from 2020-1-1 until 2024-1-1
        """
        # Create a sample series to test
        self.data = pd.read_csv(os.path.join('testing_data', 'AAPL_testing_data.csv'))
        # Create downloader for series testing
        self.downloader = DownloadModule(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2024, 1, 1)
        )

    def test_efi_length_13_tradingview_data(self):
        """
        Test EFI with the default length of 13 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 13

        trading_view_efi = pd.Series([
            25350566.37, 10509692.44, 46986548.09, 33817284.96, 42212154.27, 47162338.28, 18397944.73, 27287809.31,
            56077215.12, 49498231.83, 32533090.58, 14504987.02, 18539978.77, 143933.24, -872743.01, -6475511.94,
            -7822682.13, -6018251.86, -3066826.29, -9023046.83
        ], name=f'EFI_{length}').reset_index(drop=True)
        calculated_efi = efi(
            self.data[SourceType.CLOSE.value],
            self.data[SourceType.VOLUME.value],
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_efi, trading_view_efi)


    def test_efi_length_21_tradingview_data(self):
        """
        Test EFI with the default length of 21 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        length = 21

        trading_view_efi = pd.Series([
            28627572.17, 18885470.05, 41336580.23, 33469773.5, 38843555.01, 42299908.4, 24437333.41, 29545484.62,
            47660772.38, 44239277.81, 33921365.56, 22322729.21, 24179747.39, 11960466.73, 10239260.61, 5663680.05,
            3702827.03, 3803327.27, 4788636.36, 284181.22
        ], name=f'EFI_{length}').reset_index(drop=True)
        calculated_efi = efi(
            self.data[SourceType.CLOSE.value],
            self.data[SourceType.VOLUME.value],
            length
        ).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_efi, trading_view_efi)


    def test_efi_series_length_13_tradingview_data(self):
        """
        Test EFI series with the default length of 13 days.
        Expected data are from TradingView and the test tests last 20 days of indicator data.
        The data is rounded to 2 decimal places.
        """

        ticker = 'AAPL'
        length = 13

        trading_view_efi = pd.Series([
            25350566.37, 10509692.44, 46986548.09, 33817284.96, 42212154.27, 47162338.28, 18397944.73, 27287809.31,
            56077215.12, 49498231.83, 32533090.58, 14504987.02, 18539978.77, 143933.24, -872743.01, -6475511.94,
            -7822682.13, -6018251.86, -3066826.29, -9023046.83
        ], name=f'{ticker}_EFI_{length}').reset_index(drop=True)
        efi_series = EFI(ticker, length)
        calculated_efi = efi_series.get_data(self.downloader, pd.DataFrame()).tail(20).reset_index(drop=True).round(2)
        pd.testing.assert_series_equal(calculated_efi, trading_view_efi)


if __name__ == '__main__':
    unittest.main()