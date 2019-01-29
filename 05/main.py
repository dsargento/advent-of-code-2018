import parser
import re
import sys

sys.setrecursionlimit(999999999)
polymer = parser.Parser('./input.txt').file_content[0]
my_string = polymer

def my_react(my_string):
    deleted = True

    while deleted:
        deleted = False
        my_string = list(my_string)
        # Iterate through string
        for index, x in enumerate(my_string):
            # Handle Index errors because we'll be looking at the next character
            try:
                if x.islower():
                    if my_string[index + 1] == x.upper():
                        my_string[index] = ''
                        my_string[index + 1] = ''

                        deleted = True
                        break
                elif x.isupper():
                    if my_string[index + 1] == x.lower():
                        my_string[index] = ''
                        my_string[index + 1] = ''
                        deleted = True
                        break
                else:
                    raise IndexError
            except IndexError:
                break
        my_string = "".join(my_string)

    print(len(my_string))
    print(my_string)


regex_list = (
    '[Aa]',
    '[Bb]',
    '[Cc]',
    '[Dd]',
    '[Ed]',
    '[Ff]',
    '[Gg]',
    '[Hh]',
    '[Ii]',
    '[Jj]',
    '[Kk]',
    '[Ll]',
    '[Mm]',
    '[Nn]',
    '[Oo]',
    '[Pp]',
    '[Qq]',
    '[Rr]',
    '[Ss]',
    '[Tt]',
    '[Uu]',
    '[Vv]',
    '[Ww]',
    '[Xx]',
    '[Yy]',
    '[Zz]',
)

shortest_index = None
lowest = None
for index, x in enumerate(regex_list):
    tmp_string = my_string
    old_string = None
    tmp_string = re.sub(x, '', tmp_string)
    my_react(tmp_string)

    length = len(tmp_string)

    if lowest is None or length < lowest:
        lowest = length
        shortest_index = index

print("shortest_index: {}".format(regex_list[shortest_index]))
print("min: {}".format(lowest))
