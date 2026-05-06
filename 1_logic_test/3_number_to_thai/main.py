"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

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
        self._digits = {0: "ศูนย์", 1: "หนึ่ง", 2: "สอง", 3: "สาม", 4: "สี่", 5: "ห้า", 6: "หก", 7: "เจ็ด", 8: "แปด", 9: "เก้า"}
        self._units = {1: "สิบ", 2: "ร้อย", 3: "พัน", 4: "หมื่น", 5: "แสน", 6: "ล้าน"} # 10^unit

    def _format_friendly(self, text: str) -> str:
        # Dictionary to split words by Thai units
        for unit in ["ล้าน", "แสน", "หมื่น", "พัน", "ร้อย", "สิบ"]:
            text = text.replace(unit, f"{unit} ")
        # Clean up spaces or leading/trailing
        return " ".join(text.split())
    
    def _build_thai_text(self, number: int) -> str:
        text = ""
        num_str = str(number)[::-1]
        
        for i, digit in enumerate(num_str):
            val = int(digit)
            if val == 0:
                continue
            
            # Position-based logic
            if i == 0:  # Ones place
                if val == 1 and number > 1:
                    text = "เอ็ด" + text
                else:
                    text = self._digits[val] + text
            elif i == 1:  # Tens place
                if val == 1:
                    text = "สิบ" + text
                elif val == 2:
                    text = "ยี่สิบ" + text
                else:
                    text = self._digits[val] + "สิบ" + text
            else:  # Hundreds and above
                unit = self._units.get(i, "ล้าน")
                text = self._digits[val] + unit + text
                
        return text
    
    def number_to_thai(self, number: int) -> str:
        if number < 0 or number > 10000000:
            return "number out of range"
        if number == 0:
            return self._digits[0]
        if number == 10000000:
            return "สิบล้าน"

        raw_text = self._build_thai_text(number).strip()
        return self._format_friendly(raw_text) if READER_FRIENDLY else raw_text
    
def main():
    solution = Solution()

    # Test Case 1: Randomized valid numbers
    logger.info("--- Test Case 1: Valid Random Numbers (0-10,000,000) ---")
    list_size = 10
    random_input = [random.randint(0, 10000000) for _ in range(list_size)]
    for input in random_input:
        logger.info("input = %s", f"{input:,}")
        output = solution.number_to_thai(input)
        logger.info("output = %s\n", output)

    # Test Case 2: Out of range inputs
    logger.info("--- Test Case 2: Out of Range Inputs ---")
    out_of_range = [-50, 10000001]
    for input in out_of_range:
        logger.info("input = %s", f"{input:,}")
        output = solution.number_to_thai(input)
        logger.info("output = %s\n", output)


if __name__ == "__main__":
    main()