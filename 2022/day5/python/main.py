# https://adventofcode.com/2022/day/5

import copy
import math
import re
from collections import namedtuple

# Input
PUZZLE_FILE = "input.txt"

# Generate the character positions of
# each stack in the "crate" line
def stack_char(num_stacks: int) -> int:
    for stack in range(num_stacks):
        if stack == 0:
            # First stack is at char position 1
            yield 1
        else:
            # All other stacks are at position
            # 1 + <stack number> * 4
            yield 1 + (stack * 4)


# Answering helper function, puts together as a
# string the top crate values of each stack, in order
def top_of_stacks(stacks: dict[list]) -> str:
    return "".join([s[-1] for s in stacks.values()])


# Moves
move_pattern = re.compile(r"\d+")
Move = namedtuple("Move", ["qty", "src", "dest"])

# Read first line to determine the number of stacks
first_line = open(PUZZLE_FILE, "r").readline().strip("\n")
num_stacks = math.ceil(len(first_line) / 4)

# List of Move()s
instructions = []

# Dictionnary of stacks (lists) of the type {<stack number> : []}
stacks = {stack_key: [] for stack_key in range(1, num_stacks + 1)}

# Read input into 'crates' ([x] [x], etc.)
# and 'instructions' (move 1 from 2 to 1, etc.)
with open(PUZZLE_FILE, "r") as f:
    for line in f.readlines():

        # "Move instruction" line
        if line.startswith("move"):
            # Extract move parameters (numbers), append new Move to list
            instructions.append(Move(*(int(i) for i in move_pattern.findall(line))))

        # "Crate layout" line
        elif line.strip().startswith("["):
            # The spacing is important
            crate_line = line.strip("\n")
            for idx, pos in enumerate(stack_char(num_stacks)):
                if crate_line[pos] != " ":
                    stacks[idx + 1].insert(0, crate_line[pos])

# Part 1
stack_part1 = copy.deepcopy(stacks)
for move in instructions:
    for qty in range(move.qty):
        src = stack_part1[move.src].pop()  # Pop
        stack_part1[move.dest].append(src)  # Push

print(top_of_stacks(stack_part1))

# Part 2
stack_part2 = copy.deepcopy(stacks)
for move in instructions:
    # Get the <move.qty>th elements from the source list
    src = stack_part2[move.src][-move.qty :]
    # Remove the <move.qty>th elements from the source list
    stack_part2[move.src] = stack_part2[move.src][: -move.qty]
    # Add them to the destination
    stack_part2[move.dest] += src

print(top_of_stacks(stack_part2))
