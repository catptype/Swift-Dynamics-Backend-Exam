"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

import logging
import sys

# Define environment constant
PRODUCTION = False

# Configure logging based on production status
logging.basicConfig(
    level=logging.INFO if PRODUCTION else logging.DEBUG,
    format="[%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# Increase limit for integer to string conversion to support large factorials
sys.set_int_max_str_digits(10000000)

class Solution:
    def __init__(self) -> None:
        self._cache: dict[int, int] = {0: 1}

    def _calculate_factorial(self, number: int) -> int:
        # Check cache and log status
        if number in self._cache:
            logger.debug("Cache Hit: %s", number)
            return self._cache[number]
        
        logger.debug("Cache Miss: %s", number)
        # Calculate factorials iteratively from the last cached point
        start = len(self._cache)
        for i in range(start, number + 1):
            self._cache[i] = self._cache[i - 1] * i
        
        return self._cache[number]

    def find_tailing_zeroes(self, number: int) -> int | str:
        # Validate input
        if number < 0:
            logger.warning("number (%s) can not be negative", number)
            return "number can not be negative"
        
        # Calculate factorial
        factorial_result = self._calculate_factorial(number)
        count = 0
        
        # Convert to string to count trailing zeros
        str_val: str = str(factorial_result)
        
        # Iterate backwards to count zeros
        for char in reversed(str_val):
            if char == "0":
                count += 1
            else:
                break
        
        logger.debug("%s! has %s tailing zeros", number, count)
        return count
    
def main():
    solution = Solution()
    input_list = [120, 5, -1, 50, 100, 12000, 30000]
    for input in input_list:
        logger.info("input = %s", input)
        output = solution.find_tailing_zeroes(input)
        logger.info("output = %s\n", output)

if __name__ == "__main__":
    main()