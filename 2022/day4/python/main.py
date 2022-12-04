# https://adventofcode.com/2022/day/4

import re

# Pair format w/ regex groups, e.g. "2-4,6-8"
pattern = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")

# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input = f.read().splitlines()


def assignment_enclosed(pair: str) -> bool:
    a1, a2, b1, b2 = (int(g) for g in pattern.match(pair).groups())

    # Elf A is fully enclosed in Elf B
    if a1 >= b1 and a2 <= b2: return True

    # Elf B is fully enclosed in Elf A
    if b1 >= a1 and b2 <= a2: return True

    return False


def assignment_overlap(pair: str) -> bool:
    a1, a2, b1, b2 = (int(g) for g in pattern.match(pair).groups())

    # Elf A overlaps with Elf B
    if a2 >= b1 and b2 >= a1: return True

    return False


fully_enclosed = 0
for pair in input:
    if assignment_enclosed(pair):
        fully_enclosed += 1

overlap = 0
for pair in input:
    if assignment_overlap(pair):
        overlap += 1

print("Part 1:", fully_enclosed)
print("Part 2:", overlap)
