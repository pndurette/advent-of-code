# https://adventofcode.com/2023/day/2

import re

# Part 1

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input1 = f.read().splitlines()

# Example input:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

count1 = 0
count2 = 0
for idx, line in enumerate(input1):
    # Game starts valid (for part 1)
    # It gets invalidated if any draw, for any set,
    # has more colour than what is allowed (MAX_RED, MAX_GREEN, MAX_BLUE)
    valid_game = True

    # Most of a colour per game counter (for part 2)
    most_red = 0
    most_green = 0
    most_blue = 0

    # Take the right part of the line (after ':')
    game_data = line.split(":")[1]

    # Split on the game 'sets' (semi-colon seperated)
    game_sets = game_data.split(";")

    for set in game_sets:
        # Split on 'draws' per set (colon-sperated)
        game_draws = set.split(",")

        for draw in game_draws:
            # Extract the number of cubes and their colour from a set
            # Support that will linger from the splits
            # e.g. " 4 red" -> ("4", "red")
            num, colour = re.match(r'\s*(\d+) (\w+)', draw).groups()

            # Part 1
            if (
                (colour == "red" and int(num) > MAX_RED) or
                (colour == "blue" and int(num) > MAX_BLUE) or
                (colour == "green" and int(num) > MAX_GREEN)
            ):
                valid_game = False

            # Part 2
            if colour == "red" and int(num) > most_red:
                most_red = int(num)
            elif colour == "blue" and int(num) > most_blue:
                most_blue = int(num)
            elif colour == "green" and int(num) > most_green:
                most_green = int(num)

    # Increment part 1 count
    if valid_game:
        count1 += idx + 1

    # Increment part 2 count
    count2 += (most_red * most_green * most_blue)

print("Part 1:", count1)
print("Part 2:", count2)