# https://adventofcode.com/2022/day/3

import re

# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input = f.read().splitlines()


def priority(char: str) -> int:
    # Use ASCII value of <char> to calculate its priority
    # considering that: a-z is 1-26 and that A-Z is 26-52
    if re.match(r"[a-z]", char): return ord(char) - 96
    if re.match(r"[A-Z]", char): return ord(char) - 38


def duplicate(rucksack: list[str]) -> str:
    # Split the rucksack in half,
    # then find the intersection
    half1 = rucksack[:int(len(rucksack)/2)]
    half2 = rucksack[int(len(rucksack)/2):]
    return list(set(half1) & set(half2))[0]


def groups(input: list[str], size: int) -> list[list[str]]:
    # Yield <size>-sized chunks of <input>
    for i in range(0, len(input), size):
        yield input[i : i + size]


def duplicate_group(group: list[str]) -> str:
    # Given a list <group> of 3 strings, find the intersection
    return list(set(group[0]) & set(group[1]) & set(group[2]))[0]


part1 = 0
for rucksack in input:
    part1 += priority(duplicate(rucksack))

part2 = 0
for g in groups(input, 3):
    part2 += priority(duplicate_group(g))

print("Part 1:", part1)
print("Part 2:", part2)
