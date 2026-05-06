"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""

import logging
import random

# Define environment constant
PRODUCTION = False

# Configure logging based on production status
logging.basicConfig(
    level=logging.INFO if PRODUCTION else logging.DEBUG,
    format="[%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

class Solution:
    def find_max_index(self, numbers: list[int]) -> int | str:
        # Check for empty list
        if not numbers:
            logger.warning("list can not blank")
            return "list can not blank"
        
        # Track max value and index
        max_val = numbers[0]
        max_idx = 0
        
        # Iterate to find the highest value
        for i, num in enumerate(numbers):
            if num > max_val:
                max_val = num
                max_idx = i
        
        return max_idx
    
def main():
    solution = Solution()
    
    # Test Case 1: Random list
    list_size = 10
    random_input = [random.randint(0, 1000000) for _ in range(list_size)]
    logger.info("--- Test Case 1: Random List ---")
    logger.info("Input size: %s", list_size)
    logger.debug("Input: %s", random_input)
    
    output1 = solution.find_max_index(random_input)
    logger.info("Output: %s (Value: %s)\n", output1, random_input[output1])

    # Test Case 2: Empty list
    empty_input = []
    logger.info("--- Test Case 2: Empty List ---")
    logger.info("Input: %s", empty_input)
    
    output2 = solution.find_max_index(empty_input)
    logger.info("Output: %s\n", output2)

if __name__ == "__main__":
    main()