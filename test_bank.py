from bank import Account
import unittest


class TestBank(unittest.TestCase):
    def setUp(self):
        self.myObject = Account("Name", "0000")

    def test_deposit(self):
        self.myObject.deposit(100)
        self.assertEqual(self.myObject.balance, 100)

    def test_withdraw(self):
        


if __name__ == "__main__":
    unittest.main()
