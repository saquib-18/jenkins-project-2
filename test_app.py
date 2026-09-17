# test_app.py

import unittest

from app import calculate_result


class TestCalculateResult(unittest.TestCase):

    def test_full_marks(self):
        percentage, result = calculate_result(100, 100)

        self.assertEqual(percentage, 100)
        self.assertEqual(result, "PASS")

    def test_85_marks(self):
        percentage, result = calculate_result(85, 100)

        self.assertEqual(percentage, 85)
        self.assertEqual(result, "PASS")

    def test_50_marks(self):
        percentage, result = calculate_result(50, 100)

        self.assertEqual(percentage, 50)
        self.assertEqual(result, "PASS")

    def test_40_marks(self):
        percentage, result = calculate_result(40, 100)

        self.assertEqual(percentage, 40)
        self.assertEqual(result, "PASS")

    def test_below_pass_marks(self):
        percentage, result = calculate_result(30, 100)

        self.assertEqual(percentage, 30)
        self.assertEqual(result, "FAIL")

    def test_zero_marks(self):
        percentage, result = calculate_result(0, 100)

        self.assertEqual(percentage, 0)
        self.assertEqual(result, "FAIL")

    def test_invalid_marks_above_total(self):
        with self.assertRaises(ValueError):
            calculate_result(110, 100)

    def test_invalid_negative_marks(self):
        with self.assertRaises(ValueError):
            calculate_result(-10, 100)

    def test_invalid_total_marks(self):
        with self.assertRaises(ValueError):
            calculate_result(50, 0)


if __name__ == "__main__":
    unittest.main()
