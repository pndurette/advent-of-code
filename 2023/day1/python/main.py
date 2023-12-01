# https://adventofcode.com/2023/day/1

import re

# Part 1

# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input1 = f.read().splitlines()

# Use a regex to filter out any non-numeric characters
input1 = [re.sub("[^0-9]", "", line) for line in input1]

# Create number as "<1st><last>" of each line (e.g. 1234 -> 14)
values1 = [int(f"{line[0]}{line[-1]}") for line in input1]

# Sum the numbers
print("Part 1:", sum(values1))

# Part 2

# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input2 = f.read().splitlines()

# Dict to match digit str to an str that introduces the digit but keeps
# the first and last char of the digit str for overlaps (and subsequent matches)
# e.g. "eightwo" -> "e8t2o"
str_digit = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

# Replace all occurance of the str digit with the str that keeps the digit
# and the first and last char
for key, value in str_digit.items():
    for i, line in enumerate(input2):
        input2[i] = line.replace(key, value)    

# The rest is like part 1

# Use a regex to filter out any non-numeric characters
input2 = [re.sub("[^0-9]", "", line) for line in input2]

# Create number as "<1st><last>" of each line (e.g. 1234 -> 14)
values2 = [int(f"{line[0]}{line[-1]}") for line in input2]

# Sum the numbers
print("Part 2:", sum(values2))
