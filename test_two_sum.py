"""Unit tests for the two_sum function."""

import unittest
from two_sum_module import two_sum


class TestTwoSum(unittest.TestCase):
    """Test cases for the two_sum function."""

    def test_example_case(self):
        """Test the example case from the problem statement."""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), expected)

    def test_negative_numbers(self):
        """Test handling of negative numbers."""
        nums = [-3, 4, 3, 90]
        target = 0
        expected = [0, 2]
        self.assertEqual(two_sum(nums, target), expected)

    def test_multiple_pairs(self):
        """Test when multiple pairs could sum to target."""
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(two_sum(nums, target), expected)

    def test_duplicates(self):
        """Test when the same number is used twice."""
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), expected)

    def test_large_input(self):
        """Test performance with a large input list."""
        nums = list(range(1000000))
        target = 1999997
        expected = [999998, 999999]
        self.assertEqual(two_sum(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
