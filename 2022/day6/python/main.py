# https://adventofcode.com/2022/day/4


def detect_marker(datastream: str, start_of_message: int) -> int:
    for idx, _ in enumerate(datastream):
        # Buffer is <start_of_message> chars from the index
        buffer = datastream[idx : idx + start_of_message]
        if len(buffer) == len(set(buffer)):
            # No duplicates: marker is the index of end of buffer
            return idx + start_of_message


# Read input line
with open("input.txt", "r") as f:
    input = f.readline().strip()

print("Part 1:", detect_marker(input, 4))
print("Part 2:", detect_marker(input, 14))
