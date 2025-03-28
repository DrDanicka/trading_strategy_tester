import unittest
from trading_strategy_tester.trade.order_size.contracts import Contracts


class TestContractsOrderSize(unittest.TestCase):

    def test_exact_investment(self):
        # Arrange
        contracts = Contracts(10)
        share_price = 50
        capital = 1000  # 10 * 50

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 500)  # 10 * 50
        self.assertEqual(contracts_used, 10)

    def test_insufficient_capital(self):
        # Arrange
        contracts = Contracts(10)
        share_price = 100
        capital = 500  # not enough to buy 10

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 500)
        self.assertEqual(contracts_used, 5.0)  # 500 / 100

    def test_zero_capital(self):
        # Arrange
        contracts = Contracts(10)
        share_price = 100
        capital = 0

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_zero_contracts(self):
        # Arrange
        contracts = Contracts(0)
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_fractional_contracts(self):
        # Arrange
        contracts = Contracts(2.5)
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 250)
        self.assertEqual(contracts_used, 2.5)

    def test_contracts_more_than_capital(self):
        # Arrange
        contracts = Contracts(20)
        share_price = 100
        capital = 1000  # want 2000, only 1000 available

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 1000)
        self.assertEqual(contracts_used, 10.0)  # 1000 / 100

    def test_negative_capital(self):
        # Arrange
        contracts = Contracts(10)
        share_price = 100
        capital = -500

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

    def test_negative_contracts(self):
        # Arrange
        contracts = Contracts(-10)
        share_price = 100
        capital = 1000

        # Act
        invested_amount, contracts_used = contracts.get_invested_amount(share_price, capital)

        # Assert
        self.assertEqual(invested_amount, 0)
        self.assertEqual(contracts_used, 0)

if __name__ == '__main__':
    unittest.main()
