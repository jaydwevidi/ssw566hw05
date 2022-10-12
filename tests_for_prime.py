import unittest

from main import isPrime


class TestPrime(unittest.TestCase):

    def test345(self):
        result = isPrime(345)
        self.assertEqual(result, False)

    def testnegative55(self):
        result = isPrime(-55)
        self.assertEqual(result, False)

    def test17(self):
        result = isPrime(17)
        self.assertEqual(result, True)

    def test13(self):
        result = isPrime(13)
        self.assertEqual(result, True)

    def test19(self):
        result = isPrime(19)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()