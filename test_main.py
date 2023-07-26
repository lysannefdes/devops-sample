import unittest
from main import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, 7), 3)

if __name__ == "__main__":
    unittest.main()