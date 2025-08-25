import unittest
from two_sum_module import two_sum  # replace with actual filename if different

class TestTwoSum(unittest.TestCase):

    def test_example_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), expected)

    def test_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        expected = [0, 2]
        self.assertEqual(two_sum(nums, target), expected)

    def test_multiple_pairs(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]  # nums[1] + nums[2] = 2 + 4
        self.assertEqual(two_sum(nums, target), expected)

    def test_duplicates(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(two_sum(nums, target), expected)

    def test_large_input(self):
        nums = list(range(1000000))  # [0, 1, 2, ... 999999]
        target = 1999997
        expected = [999998, 999999]
        self.assertEqual(two_sum(nums, target), expected)

if __name__ == "__main__":
    unittest.main()
