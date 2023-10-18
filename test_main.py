import unittest
from main import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, 7), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-4, 5), -20)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(100, 25), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)



if __name__ == "__main__":
    unittest.main()
