import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

def two_sum(arr: list[int], target: int) -> list[int]:
    num_to_index = {}
    logging.debug(f"Starting two_sum with arr={arr}, target={target}")

    for i, num in enumerate(arr):
        complement = target - num
        logging.debug(f"Index={i}, Num={num}, Complement={complement}, Map={num_to_index}")

        if complement in num_to_index:
            logging.info(f"Found match: {num_to_index[complement]} + {i} -> {target}")
            return [num_to_index[complement], i]

        num_to_index[num] = i
        logging.debug(f"Updated map: {num_to_index}")

    logging.warning("No two numbers add up to target")
    return []

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter numbers: ").split()]
    target = int(input("Enter target: "))
    res = two_sum(arr, target)
    print("Result:", " ".join(map(str, res)) if res else "No solution")
