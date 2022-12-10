# Usage: terraform plan

locals {
  input = file("${path.module}/input.txt")

  # Grid size (via the length of line 0)
  grid_size = length(split("\n", local.input)[0])

  # Split all numbers and bunch by grid size
  trees_raw = regexall("[0-9]", local.input)
  rows = chunklist(local.trees_raw, local.grid_size)

  # Create lists for columns too
  # (so they can easily be traversed)
  columns = [
    for col in range(local.grid_size) : [
      for row in local.rows : row[col]
    ]
  ]

  # Part 1
  visible = [
    for row in range(1, local.grid_size - 1) : [
      for col in range(1, local.grid_size - 1) :
      # Filter only visible trees
      format("%s (%s, %s)", local.rows[row][col], row, col) if(
        local.rows[row][col] > reverse(sort(slice(local.rows[row], 0, col)))[0] ||                   # Left
        local.rows[row][col] > reverse(sort(slice(local.rows[row], col + 1, local.grid_size)))[0] || # Right
        local.rows[row][col] > reverse(sort(slice(local.columns[col], 0, row)))[0] ||                # Top
        local.rows[row][col] > reverse(sort(slice(local.columns[col], row + 1, local.grid_size)))[0] # Bottom
      )
    ]
  ]

  # The visible trees are the length of structure above added to the edge
  visible_num = local.grid_size * 4 - 4 + length(flatten(local.visible))

  # Part 2 (DOESN'T WORK, and NEVER will. This was a silly idea.)
  scenic = [
    for row in range(1, local.grid_size - 1) : [
      for col in range(1, local.grid_size - 1) :
      # Debug block: (<value> (<x>,<y>) — (left <l>, right <r>, top <t> , down <d>) (test: <anything to test>))
      # Uncomment the whole format() instead of the list below
      # format("%s (%s, %s) — (left: %s, right: %s, top: %s, down: %s) (tests: %s, %s)",
      #   local.rows[row][col], row, col,
      #   try(length(regex("^[^${local.rows[row][col]}-8]+", join("", reverse(slice(local.rows[row], 0, col))))), 1),             # Left
      #   try(length(regex("^[^${local.rows[row][col]}-8]+", join("", slice(local.rows[row], col + 1, local.grid_size)))), 1),    # Right
      #   try(length(regex("^[^${local.rows[row][col]}-8]+", join("", reverse(slice(local.columns[col], 0, row))))), 1),          # Top
      #   try(length(regex("^[^${local.rows[row][col]}-8]+", join("", slice(local.columns[col], row + 1, local.grid_size)))), 1), # Bottom
      #   jsonencode(reverse(slice(local.columns[col], 0, row))),
      #   "^[^${local.rows[row][col]}-8]+(?:${local.rows[row][col]})"
      # )
      [
        try(length(regex("^[^${local.rows[row][col]}-8]+", join("", reverse(slice(local.rows[row], 0, col))))), 1),             # Left
        try(length(regex("^[^${local.rows[row][col]}-8]+", join("", slice(local.rows[row], col + 1, local.grid_size)))), 1),    # Right
        try(length(regex("^[^${local.rows[row][col]}-8]+", join("", reverse(slice(local.columns[col], 0, row))))), 1),          # Top
        try(length(regex("^[^${local.rows[row][col]}-8]+", join("", slice(local.columns[col], row + 1, local.grid_size)))), 1), # Bottom
      ]
    ]
  ]

  # Multiply the "scenic score" for each point
  scenic_scores = flatten([
    for row in local.scenic : [
      for item in row : [
        tostring(item[0] * item[1] * item[2] * item[3])
      ]
    ]
  ])

  # Get the largest scenic score
  scenic_score_largest = reverse(sort(local.scenic_scores))[0]
}

# output "visible" {
#   value = local.visible
# }

output "part1" {
  value = local.visible_num
}

# output "scenic" {
#   value = local.scenic
# }

# output "scenic_scores" {
#   value = local.scenic_scores
# }

output "part2" {
  value = local.scenic_score_largest + 0
}

#### All the following garbage and tests, left for posterity:

# > length(regex("[0-5]+", join("", ["3", "3"])))
# 2
# > length(regex("[0-9]+", join("", ["3", "5", "3"])))
# 3
# > length(regex("[0-5]+", join("", ["3", "5"])))
# 2
# > length(regex("[0-5]+", join("", ["6", "5"])))
# 1
# > length(regex("[0-5]+", join("", ["3", "6", "4"])))
# 1
# > length(regex("[0-5]+", join("", ["6", "6", "4"])))
# 1
# > length(regex("[0-5]+", join("", ["6", "4", "4"])))
# 2
# > length(regex("[0-5]+", join("", ["6", "2", "6", "4", "5"])))
# 1
# > length(regex("[0-5]+", join("", ["6", "2", "4", "4", "5"])))
# 4
# > length(regex("[0-5]+", join("", ["6", "2", "4", "4"])))
# 0 to number - 1, list is numbers till before the number
# > try(length(regex("[0-2]+", join("", reverse(["3", "0"])))),0)

# we check for 5, till 5 or not 6-9
# ^[5|^6-9]+


# regex("^[0-${local.rows[row][col] - 1}]+" (or *)
# bug is when next number is same as current, get 0 instead of 1

# ^[^0-4]*

# Ill keep this, and just remove the 0s (1 or 0 doesn't change?)

# ---- 
# 33549
#   ^ (2 to the right, must count the block...)

# Current is 5, string to check is "49", match is 49 (length 2)
# [[:digit:](?:[5-9])
# regex("[[:digit:]](?:[5-9])", "54925")

# index(reverse(slice(local.rows[row], 0, col)), tostring(local.rows[row][col] + 0)) + 1,

# try(length(regex("^[0-${local.rows[row][col]}]*[^${local.rows[row][col] + 1}-9]*", join("", reverse(slice(local.rows[row], 0, col))))), 0), # Left
# try(length(regex("^[${local.rows[row][col] + 1}-9])", join("", slice(local.rows[row], col + 1, local.grid_size)))), 0),    # Right
# try(length(regex("^[0-${local.rows[row][col]}]*[^${local.rows[row][col] + 1}-9]*", join("", reverse(slice(local.columns[col], 0, row))))), 0),          # Top
# try(length(regex("^[0-${local.rows[row][col]}]*[^${local.rows[row][col] + 1}-9]*", join("", slice(local.columns[col], row + 1, local.grid_size)))), 0), # Bottom

# index(<the slice>, <the number>) (or the next?)
# The result + 1 is the number of positions, if not in index, the numbner till end of slice (not blocked)

# > try(index(["4", "9"], "5") + 1, 2)

# [[:digit:](?:[0-9]))",
# ^[^6-9]+ — for number 5, find everything from 6-9, at least once

# WINNER?
# "^[0-${local.rows[row][col]}]*[^${local.rows[row][col] + 1}-9]*"


#  + scenic = [
#       + [
#           + "5 (1, 1) — (left: 1, right: 1, top: 1, down: 1) (tests: [\"0\"], ^[^5-8]+(?:5))",
#           + "5 (1, 2) — (left: 1, right: 2, top: 1, down: 1) (tests: [\"3\"], ^[^5-8]+(?:5))",
#           + "1 (1, 3) — (left: 1, right: 1, top: 1, down: 1) (tests: [\"7\"], ^[^1-8]+(?:1))",
#         ],
#       + [
#           + "5 (2, 1) — (left: 1, right: 3, top: 1, down: 1) (tests: [\"5\",\"0\"], ^[^5-8]+(?:5))",
#           + "3 (2, 2) — (left: 1, right: 1, top: 1, down: 1) (tests: [\"5\",\"3\"], ^[^3-8]+(?:3))",
#           + "3 (2, 3) — (left: 1, right: 1, top: 1, down: 1) (tests: [\"1\",\"7\"], ^[^3-8]+(?:3))",
#         ],
#       + [
#           + "3 (3, 1) — (left: 1, right: 1, top: 1, down: 1) (tests: [\"5\",\"5\",\"0\"], ^[^3-8]+(?:3))",
#           + "5 (3, 2) — (left: 2, right: 2, top: 1, down: 1) (tests: [\"3\",\"5\",\"3\"], ^[^5-8]+(?:5))",
#           + "4 (3, 3) — (left: 1, right: 1, top: 2, down: 1) (tests: [\"3\",\"1\",\"7\"], ^[^4-8]+(?:4))",
#         ],
#     ]

#  #* s[1] * s[2] * s[3]