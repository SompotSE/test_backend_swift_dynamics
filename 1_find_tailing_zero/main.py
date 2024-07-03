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
import sys

class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        validate_num = so.validate_number(number)
        if validate_num != None:
            return validate_num
        else:
            if number < 0:
                return None
            elif number < 5:
                return 0
            else:
                count = 0
                five_count = number // 5
                while five_count > 0:
                    count += five_count
                    five_count //= 5
                return count


    def convart_string_to_int(self, number_str: str) -> int:
        try:
            return int(number_str)
        except ValueError:
            sys.exit(f"{number_str} is not a valid integer. Please try again.")


    def validate_number(self, number: int) -> str | None:
        if number < 0:
            return "Number can not be negative"
        return None
    

so = Solution()
number_str: str = input("Number : ")
number_int: int = so.convart_string_to_int(number_str)
tailing_zeroes = so.find_tailing_zeroes(number_int)
print(tailing_zeroes)
