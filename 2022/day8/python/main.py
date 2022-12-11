# https://adventofcode.com/2022/day/8


def max_view(tree: int, view: list[int]) -> int:
    """
    For a given <tree> value, return the number of positions (int)
    before hitting a tree of equal or larger value, or the edge in list <view>
    """
    for idx, value in enumerate(view):
        if value >= tree:
            return idx + 1
    return len(view)


# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input = f.read().splitlines()

# List of row lists
rows = [list(row) for row in input]

# List of column lists (transposed rows)
columns = []
for row in range(len(rows)):
    column = []
    for col in range(len(rows)):
        column.append(rows[col][row])
    columns.append(column)

# Part 1: Visible trees
visible = 0
for row in range(1, len(rows) - 1):
    for col in range(1, len(rows) - 1):
        if (
            rows[row][col] > max(rows[row][0:col])  # left
            or rows[row][col] > max(rows[row][col + 1 : len(rows)])  # right
            or rows[row][col] > max(columns[col][0:row])  # top
            or rows[row][col] > max(columns[col][row + 1 : len(rows)])  # bottom
        ):
            visible += 1

# Add the edge
print("Part 1:", visible + len(rows) * 4 - 4)

# Part 2: Scenic scores
scenic_scores = []
for row in range(1, len(rows) - 1):
    for col in range(1, len(rows) - 1):
        scenic_scores.append(
            max_view(rows[row][col], rows[row][0:col][::-1])  # left
            * max_view(rows[row][col], rows[row][col + 1 : len(rows)])  # right
            * max_view(rows[row][col], columns[col][0:row][::-1])  # top
            * max_view(rows[row][col], columns[col][row + 1 : len(rows)])  # bottom
        )

# Get the max
print("Part 2:", max(scenic_scores))
