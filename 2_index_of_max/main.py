"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""

import sys

class Solution():
    
    def find_max_index(self, numbers: list) -> int | str:  
        if len(numbers) == 0:
            return "List can not blank."
        else:
            index = 0
            value = numbers[0]

            for i, num in enumerate(numbers):
                if num > value:
                    value = num
                    index = i
            return index


    def validate_input_number(self, input_str: str):
        if input_str[:1] != "[" or input_str[-1:] != "]":
            sys.exit("Data input is not list.")
    

    def validate_input_list_blank(self, input_str: str) -> list | None:
        if len(input_str) == 2 and (input_str[:1] == "[" or input_str[-1:] == "]"):
            return []
        return None


    def split_data_input(self, input_str: str) -> list:
        return input_str[1:-1].split(',')


    def perpare_data_list(self, list_str: list) -> list:
        number_list: list = []
        for str in list_str:
            if so.convart_string_to_int(str) not in number_list:
                number_list.append(so.convart_string_to_int(str))
        return  number_list
    

    def convart_string_to_int(self, number_str: str) -> int:
        try:
            return int(number_str)
        except ValueError:
            sys.exit(f"{number_str} is not a valid integer. Please try again.")


so = Solution()

numbers: str = input("Number : ")
so.validate_input_number(numbers)
list_blank = so.validate_input_list_blank(numbers)
result = ""
if list_blank == None:
    string_list: list = so.split_data_input(numbers)
    number_list: list = so.perpare_data_list(string_list)
    result = so.find_max_index(number_list)
else:
    result = so.find_max_index(list_blank)

print(result)