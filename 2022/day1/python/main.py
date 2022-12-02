# https://adventofcode.com/2022/day/1

# Recursive function to split a list on a delimeter element
# Returns a list of list of strings
def split(a_list: list[str], delim: str) -> list[list[str]]:
    # Exit condition: the list doesn't contain the delimiter
    if not delim in a_list:
        return [a_list]

    # Cut the list when a delimiter is reached
    # Call itself with the rest
    for idx, element in enumerate(a_list):
        if element == delim:
            return [a_list[0:idx]] + split(a_list[idx + 1 :], delim)


# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input = f.read().splitlines()

# Split in chunks on "" (empty list items)
chunks = split(input, "")

# Sum the chunks (and convert each value to int beforehand)
calories = [sum((int(v) for v in values)) for values in chunks]

# Sort the calories
calories = sorted(calories)

# Part 1: return the largest (last element) of the sorted list
print("Part 1:", calories[-1])

# Part 2: return the sum of the 3 largest elements
print("Part 2:", sum(calories[-3:]))