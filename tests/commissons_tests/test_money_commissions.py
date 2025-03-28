import unittest
from trading_strategy_tester.trade.trade_commissions.money_commissions import MoneyCommissions


class TestMoneyCommissions(unittest.TestCase):

    def test_basic_usage(self):
        # Arrange
        commission = MoneyCommissions(2.0)  # $2 per contract
        invested = 1000
        contracts = 5

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 10.0)

    def test_zero_commission(self):
        # Arrange
        commission = MoneyCommissions(0.0)
        invested = 500
        contracts = 3

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 0.0)

    def test_zero_contracts(self):
        # Arrange
        commission = MoneyCommissions(5.0)
        invested = 1000
        contracts = 0

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 0.0)

    def test_fractional_contracts(self):
        # Arrange
        commission = MoneyCommissions(1.5)
        invested = 600
        contracts = 2.5

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 3.75)

    def test_negative_commission_value_clamped_to_zero(self):
        # Arrange
        commission = MoneyCommissions(-3.0)  # is set to 0
        invested = 1000
        contracts = 4

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()
