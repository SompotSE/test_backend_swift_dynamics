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

import sys

class Solution:

    def number_to_roman(self, number: int) -> str:
        validate_num = so.validate_number(number)
        if validate_num != None:
            return validate_num
        else:
            # if not (1 <= num <= 3999):
            #     raise ValueError("Number must be between 1 and 3999")
            roman_numerals = so.init_roman_numerals()
            result = ""
            for value, numeral in roman_numerals.items():
                while number >= value:
                    result += numeral
                    number -= value

            return result


    def convart_string_to_int(self, number_str: str) -> int:
        try:
            return int(number_str)
        except ValueError:
            sys.exit(f"{number_str} is not a valid integer. Please try again.")


    def validate_number(self, number: int) -> str | None:
        if number <= 0:
            return "Number can not less than 0"
        return None


    def init_roman_numerals(self):
        return {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

    
so = Solution()
number_str: str = input("Number : ")
number_int: int = so.convart_string_to_int(number_str)
roman_number = so.number_to_roman(number_int)
print(roman_number)