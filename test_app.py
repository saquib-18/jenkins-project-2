import unittest
from app import calculate_result


class TestResultCalculation(unittest.TestCase):

    def test_full_marks(self):
        self.assertEqual(calculate_result(100, 100), 100)

    def test_half_marks(self):
        self.assertEqual(calculate_result(50, 100), 50)

    def test_zero_marks(self):
        self.assertEqual(calculate_result(0, 100), 0)


if __name__ == "__main__":
    unittest.main()
