import unittest
from trading_strategy_tester.trade.trade_commissions.percentage_commissions import PercentageCommissions


class TestPercentageCommissions(unittest.TestCase):

    def test_basic_percentage(self):
        # Arrange
        commission = PercentageCommissions(1.0)  # 1%
        invested = 1000
        contracts = 5  # unused

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 10.0)  # 1% of 1000

    def test_zero_percentage(self):
        # Arrange
        commission = PercentageCommissions(0.0)
        invested = 1000
        contracts = 10

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 0.0)

    def test_full_percentage(self):
        # Arrange
        commission = PercentageCommissions(100.0)
        invested = 750
        contracts = 1

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 750.0)  # 100% of 750

    def test_over_100_percentage_capped(self):
        # Arrange
        commission = PercentageCommissions(150.0)  # is set at 100%
        invested = 500
        contracts = 2

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 500.0)

    def test_negative_percentage_clamped(self):
        # Arrange
        commission = PercentageCommissions(-10.0)  # is set to 0%
        invested = 500
        contracts = 5

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 0.0)

    def test_fractional_percentage(self):
        # Arrange
        commission = PercentageCommissions(0.5)  # 0.5%
        invested = 800
        contracts = 4

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 4.0)  # 0.5% of 800


    def test_zero_invested(self):
        # Arrange
        commission = PercentageCommissions(5.0)
        invested = 0
        contracts = 3

        # Act
        result = commission.get_commission(invested, contracts)

        # Assert
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()
