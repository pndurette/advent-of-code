# https://adventofcode.com/2022/day/2

OPPONENT_VALUES = {"A": 1, "B": 2, "C": 3}
PLAYER_VALUES = {"X": 1, "Y": 2, "Z": 3}

# Moves:
# Rock       A X
# Paper      B Y
# Scissors   C Z

# End result (part 2):
# Lose  X
# Draw  Y
# Win   Z


def score_round(opponent: str, player: str) -> int:
    """
    Args:
        opponent (str): The opponent move (i.e. "A", "B" or "C")
        player (str): The player move (i.e. " X", "Y" or "Z")
    Returns the score of the player
    """
    score = 0

    # Draw: 3 points
    if OPPONENT_VALUES[opponent] == PLAYER_VALUES[player]:
        score += 3

    # Win: 6 points
    elif (
        # Rock (X) beats Scissors (C)
        (player == "X" and opponent == "C")
        # Scissors (Z) beats Paper (B)
        or (player == "Z" and opponent == "B")
        # Paper (Y) beats Rock (A)
        or (player == "Y" and opponent == "A")
    ):
        score += 6

    # Add hand value
    score += PLAYER_VALUES[player]

    return score


def get_player_move(opponent: str, end_result: str) -> str:
    """
    Args:
        opponent (str): The opponent move (i.e. "A", "B" or "C")
        end_result (str): The expected end result (i.e. " X", "Y" or "Z")
    Returns the move of the player (i.e. " X", "Y" or "Z")
    """

    # Player loses (X)
    if end_result == "X":
        # Rock (X) loses to Paper (B)
        if opponent == "B":
            return "X"
        # Paper (Y) loses to Scissors (C)
        elif opponent == "C":
            return "Y"
        # Scissors (Z) loses to Rock (A)
        else:
            return "Z"

    # Draw (Y)
    elif end_result == "Y":
        # Rock (A) vs Rock (X)
        if opponent == "A":
            return "X"
        # Paper (B) vs Paper (Y)
        elif opponent == "B":
            return "Y"
        # Scissors (C) vs Scissors (Z)
        else:
            return "Z"

    # Player win (Z)
    elif end_result == "Z":
        # Rock (X) beats Scissors (C)
        if opponent == "C":
            return "X"
        # Scissors (Z) beats Paper (B)
        elif opponent == "B":
            return "Z"
        # Paper (Y) beats Rock (A)
        else:
            return "Y"


# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input = f.read().splitlines()

# Part 1
score1 = 0
for round in input:
    opponent, player = tuple(round.split())
    score1 += score_round(opponent, player)

print("Part 1:", score1)

# Part 2
score2 = 0
for round in input:
    opponent, end_result = tuple(round.split())
    player = get_player_move(opponent, end_result)
    score2 += score_round(opponent, player)

print("Part 2:", score2)
