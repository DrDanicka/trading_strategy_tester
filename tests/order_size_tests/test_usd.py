import unittest
from trading_strategy_tester.trade.order_size.usd import USD


class TestUSDOrderSize(unittest.TestCase):

    def test_basic_usage(self):
        # Arrange
        usd = USD(500)
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 500)
        self.assertEqual(contracts_used, 5.0)

    def test_exact_capital(self):
        # Arrange
        usd = USD(1000)
        share_price = 250
        capital = 1000

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 1000)
        self.assertEqual(contracts_used, 4.0)

    def test_investment_more_than_capital(self):
        # Arrange
        usd = USD(2000)
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 1000)
        self.assertEqual(contracts_used, 10.0)

    def test_zero_investment(self):
        # Arrange
        usd = USD(0)
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_zero_capital(self):
        # Arrange
        usd = USD(500)
        share_price = 50
        capital = 0

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_fractional_shares(self):
        # Arrange
        usd = USD(100)
        share_price = 33.33
        capital = 500

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 100)
        self.assertAlmostEqual(contracts_used, 3.0, places=2)

    def test_negative_usd_value(self):
        # Arrange
        usd = USD(-100)
        share_price = 50
        capital = 1000

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_negative_capital(self):
        # Arrange
        usd = USD(100)
        share_price = 50
        capital = -200

        # Act
        invested_amount, contracts_used = usd.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

if __name__ == '__main__':
    unittest.main()
