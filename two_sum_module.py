"""Implementation of the two_sum problem with logging."""

import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Return indices of two numbers in nums that add up to target.

    Args:
        nums (list[int]): List of integers to search.
        target (int): The sum to find.

    Returns:
        list[int]: Indices of the two numbers, or empty list if none found.
    """
    num_to_index = {}
    logging.debug("Starting two_sum with nums=%s, target=%s", nums, target)

    for i, num in enumerate(nums):
        complement = target - num
        logging.debug(
            "Index=%s, Num=%s, Complement=%s, Map=%s",
            i, num, complement, num_to_index
        )

        if complement in num_to_index:
            logging.info(
                "Found match: %s + %s -> %s",
                num_to_index[complement], i, target
            )
            return [num_to_index[complement], i]

        num_to_index[num] = i
        logging.debug("Updated map: %s", num_to_index)

    logging.warning("No two numbers add up to target")
    return []


if __name__ == "__main__":
    input_nums = [int(x) for x in input("Enter numbers: ").split()]
    input_target = int(input("Enter target: "))
    res = two_sum(input_nums, input_target)
    print("Result:", " ".join(map(str, res)) if res else "No solution")
