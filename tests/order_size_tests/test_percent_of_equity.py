import unittest
from trading_strategy_tester.trade.order_size.percent_of_equity import PercentOfEquity


class TestPercentOfEquity(unittest.TestCase):

    def test_basic_usage(self):
        # Arrange
        percent = PercentOfEquity(50)  # 50% of capital
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 500)
        self.assertEqual(contracts_used, 5.0)

    def test_zero_percent(self):
        # Arrange
        percent = PercentOfEquity(0)
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_hundred_percent(self):
        # Arrange
        percent = PercentOfEquity(100)
        share_price = 50
        capital = 1000

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 1000)
        self.assertEqual(contracts_used, 20.0)

    def test_over_100_percent_capped(self):
        # Arrange
        percent = PercentOfEquity(150)  # should cap at 100%
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 1000)
        self.assertEqual(contracts_used, 10.0)

    def test_negative_percent_set_to_zero(self):
        # Arrange
        percent = PercentOfEquity(-20)  # should set to 0
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_fractional_percent(self):
        # Arrange
        percent = PercentOfEquity(12.5)
        share_price = 200
        capital = 1600

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 200)
        self.assertEqual(contracts_used, 1.0)

    def test_zero_capital(self):
        # Arrange
        percent = PercentOfEquity(50)
        share_price = 100
        capital = 0

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_negative_capital(self):
        # Arrange
        percent = PercentOfEquity(50)
        share_price = 100
        capital = -500

        # Act
        invested_amount, contracts_used = percent.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

if __name__ == '__main__':
    unittest.main()
