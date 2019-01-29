import parser
import time

my_parser = parser.Parser("./input.txt")
count = 0
found = 0
history = set()

# While no duplicate is found
while found == 0:
    # Iterate through our sequence
    for x in my_parser.sequence:
        # Add the current number to the count
        count += x
        # If the current number is in our history
        if count in history:
            # We found it!
            found = 1
            break
        # Append the current count to the history
        history.add(count)

print(history)
print(count)
