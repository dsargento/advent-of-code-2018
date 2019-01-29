import parser
import time

my_parser = parser.Parser("./input.txt")

two_letters = 0
three_letters = 0
for line in my_parser.lines:
    letter_list = []
    two_flag = False
    three_flag = False
    for char in line:
        if char not in letter_list:
            letter_list.append(char)
    for letter in letter_list:
        if line.count(letter) == 2:
            two_flag = True
        if line.count(letter) == 3:
            three_flag = True
    if two_flag:
        two_letters += 1
    if three_flag:
        three_letters += 1

print(two_letters * three_letters)
# for line_index, line_value in enumerate(my_parser.lines):
#     for index in range(len(my_parser.lines)):
#         if my_parser.lines[index] == my_parser.lines[index] and index != line_index:
#             char_count = 0
#             for char_index, char in enumerate(my_parser.lines[index]):
#                 try:
#                     if line_value[char_index] == char:
#                         char_count += 1
#                 except IndexError:
#                     continue
#             if char_count == (len(line_value) - 1):
#                 print(line_value)
