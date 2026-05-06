# The maximum standard Roman numeral is 3,999

"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""

import logging
import random

# Define environment constant
READER_FRIENDLY = True # Set False if want exact output following the instruction
PRODUCTION = False

# Configure logging based on production status
logging.basicConfig(
    level=logging.INFO if PRODUCTION else logging.DEBUG,
    format="[%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

class Solution:
    def __init__(self) -> None:
        self._roman_map = {
            1000: "M", 
            900: "CM", 500: "D", 400: "CD", 100: "C", 
            90: "XC", 50: "L", 40: "XL", 10: "X", 
            9: "IX", 5: "V", 4: "IV", 1: "I"
        }

    def number_to_roman(self, number: int) -> str:
        # Range validation based on Roman numeral constraints
        if number < 1 or number > 3999:
            logger.warning("number out of range (1-3999)")
            return "number out of range (1-3999)"

        roman_text = ""
        for val, symbol in self._roman_map.items():
            count = number // val
            if count > 0:
                roman_text += symbol * count
                number %= val
                
        return roman_text
    
def main():
    solution = Solution()

    # Test Case 1: Randomized valid numbers
    logger.info("--- Test Case 1: Valid Random Numbers (1-3999) ---")
    list_size = 10
    random_input = [random.randint(1, 3999) for _ in range(list_size)]
    for input in random_input:
        logger.info("input = %s", f"{input:,}")
        output = solution.number_to_roman(input)
        logger.info("output = %s\n", output)
    
    # Test Case 2: Out of range inputs
    logger.info("--- Test Case 2: Out of Range Inputs ---")
    out_of_range = [0, -50, 4000, 10000]
    for input in out_of_range:
        logger.info("input = %s", f"{input:,}")
        output = solution.number_to_roman(input)
        logger.info("output = %s\n", output)

if __name__ == "__main__":
    main()
