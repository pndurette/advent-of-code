# https://adventofcode.com/2022/day/7

from anytree import Node, Resolver, RenderTree
from anytree.search import findall_by_attr, findall

# Read file as list
# (use .read().splitlines() to remove the newlines)
with open("input.txt", "r") as f:
    input = f.read().splitlines()

# anytree node resolver
resolver = Resolver("name")

# Create the root of filesystem
root = Node("root", size=0)

# Walk the filesystem and add nodes
for line in input:
    if line.startswith("$ ls"):
        # command: ls (can be ignored)
        continue

    if line.startswith("$ cd"):
        # command: cd
        # e.g. "$ cd e"
        _, _, dir = line.split()
        if dir == "/":
            current_node = root
        elif dir == "..":
            current_node = resolver.get(current_node, "..")
        else:
            current_node = resolver.get(current_node, dir)
    else:
        # Add node
        if line.startswith("dir"):
            # e.g. "dir a"
            # Add a directory mode
            _, name = line.split()
            Node(name, parent=current_node, size=0)
        else:
            # e.g. "8033020 d.log"
            # Add a file node (w/ size)
            size, name = line.split()
            Node(name, parent=current_node, size=size)

# Render filesystem
print(RenderTree(root))

# Part 1
# Get all directories (size = 0)
dirs = findall_by_attr(root, 0, name="size")
total_dir_size = 0
directory_sizes = []  # For part 2

for d in dirs:
    dir_size = 0
    files = findall(d, filter_=lambda node: int(node.size) > 0)
    for f in files:
        dir_size += int(f.size)
    if dir_size <= 100000:
        total_dir_size += dir_size
    directory_sizes.append(dir_size)

print("Part 1:", total_dir_size)

# Part 2
used_space = 0
files = findall(root, filter_=lambda node: int(node.size) > 0)
for f in files:
    used_space += int(f.size)

free_space = 70000000 - used_space
free_space_needed = 30000000 - free_space

smallest_dir_to_delete = sorted(
    [size for size in directory_sizes if size > free_space_needed]
)[0]

print("Part 2:", smallest_dir_to_delete)
