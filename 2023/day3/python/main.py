# https://adventofcode.com/2023/day/3

import re

# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.example.txt", "r") as f:
    input1 = f.read().splitlines()

# Example input
# 0 467..114..
# 1 ...*......
# 2 ..35..633.
# 3 ......#...
# 4 617*......
# 5 .....+.58.
# 6 ..592.....
# 7 ......755.
# 8 ...$.*....
# 0 .664.598..

count1 = 0
count2 = 0

for idx, line in enumerate(input1):
    print(f"--- Line {idx}")

    # Match on all numbers of the line
    matches = re.finditer(r'(\d+)', line)
    for match in matches:
        # Numbers start invalid, gets valid if touched by a non-period
        valid = False

        # Extract number, start and end (excluded) positions
        number = int(match.group(0))
        start, end = match.span()

        # Check left
        #   x999
        if start > 0:
            if line[start - 1] != ".":
                valid = True
                count1 += number
                continue

        # Check right:
        #   999x
        if end < len(line):
            if line[end] != ".":
                valid = True
                count1 += number
                continue

        # Check up
        #  xxxxx
        #   999
        if idx > 0:
            up_start = start - 1 if start > 0 else start
            up_end = end + 1 if end < len(line) - 1 else end
            for up in input1[idx-1][up_start:up_end]:
                if up != ".":
                    valid = True
                    count1 += number
                    break
            
            if valid: continue

        # Check down
        #   999
        #  xxxxx
        if idx < len(input1) - 1:
            down_start = start - 1 if start > 0 else start
            down_end = end + 1 if end < len(line) - 1 else end
            for down in input1[idx+1][down_start:down_end]:
                if down != ".":
                    valid = True
                    count1 += number
                    break

            if valid: continue

print("Part 1:", count1)
print("Part 2:", count2)

# No part 2, it's late sunday night, and I couldn't think straight, need to go to bed Zzz