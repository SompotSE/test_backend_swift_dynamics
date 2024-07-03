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
import sys

class Solution:

    def number_to_thai(self, number: int) -> str:
        validate_num = so.validate_number(number)
        if validate_num != None:
            return validate_num
        else:
            text_position = so.init_text_position()
            text_number = so.init_text_number()
            result = ""
            if (number == 0):
                return "ศูนย์"
            if number > 1000000:
                result += so.number_to_thai(number // 1000000) + "ล้าน"
                number %= 1000000
            div = 100000
            pos = 0
            while number > 0:
                d = number // div
                if div == 10 and d == 2:
                    result += "ยี่"
                elif div == 10 and d == 1:
                    pass
                elif div == 1 and d == 1 and result != "":
                    result += "เอ็ด"
                else:
                    result += text_number[d]
                if d:
                    result += text_position[pos]
                number %= div
                div //= 10
                pos += 1

            return result


    def convart_string_to_int(self, number_str: str) -> int:
        try:
            return int(number_str)
        except ValueError:
            sys.exit(f"{number_str} is not a valid integer. Please try again.")
    

    def validate_number(self, number: int) -> str | None:
        if number < 0:
            return "Number can not less than 0"
        return None
    

    def init_text_position(self):
        return ["แสน", "หมื่น", "พัน", "ร้อย", "สิบ", ""]
    

    def init_text_number(self):
        return ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

    
so = Solution()
number_str: str = input("Number : ")
number_int: int = so.convart_string_to_int(number_str)
text_number = so.number_to_thai(number_int)
print(text_number)