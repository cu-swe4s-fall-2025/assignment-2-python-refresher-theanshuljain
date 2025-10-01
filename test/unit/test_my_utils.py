"""
Unit tests for functions in my_utils.py

Includes tests for:
- calculate_mean
- calculate_median
- calculate_stddev
"""

import unittest
import random
from my_utils import calculate_mean, calculate_median, calculate_stddev


class TestCalculateMean(unittest.TestCase):
    """Unit tests for calculate_mean."""

    def test_mean_positive(self):
        values = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(calculate_mean(values), 3.0)

    def test_mean_random(self):
        random.seed(42)
        values = [random.randint(0, 100) for _ in range(20)]
        expected = sum(values) / len(values)
        self.assertAlmostEqual(calculate_mean(values), expected)

    def test_mean_negative_empty(self):
        with self.assertRaises(ValueError):
            calculate_mean([])


class TestCalculateMedian(unittest.TestCase):
    """Unit tests for calculate_median."""

    def test_median_positive_odd(self):
        values = [3, 1, 2]
        self.assertEqual(calculate_median(values), 2.0)

    def test_median_positive_even(self):
        values = [1, 2, 3, 4]
        self.assertEqual(calculate_median(values), 2.5)

    def test_median_random(self):
        random.seed(42)
        values = [random.randint(0, 50) for _ in range(11)]
        sorted_vals = sorted(values)
        expected = float(sorted_vals[len(values) // 2])
        self.assertEqual(calculate_median(values), expected)

    def test_median_negative_empty(self):
        with self.assertRaises(ValueError):
            calculate_median([])


class TestCalculateStddev(unittest.TestCase):
    """Unit tests for calculate_stddev."""

    def test_stddev_positive(self):
        values = [2, 4, 4, 4, 5, 5, 7, 9]
        # Known population stddev = 2.0
        self.assertAlmostEqual(calculate_stddev(values), 2.0)

    def test_stddev_random(self):
        random.seed(42)
        values = [random.randint(1, 20) for _ in range(15)]
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        expected = variance ** 0.5
        self.assertAlmostEqual(calculate_stddev(values), expected)

    def test_stddev_negative_empty(self):
        with self.assertRaises(ValueError):
            calculate_stddev([])


if __name__ == "__main__":
    unittest.main()
