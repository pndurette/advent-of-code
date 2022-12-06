#! /bin/bash

# https://adventofcode.com/2022/day/5

# Load file
PUZZLE_FILE="input.txt"

# Split into crates and instructions
CRATES="$(cat $PUZZLE_FILE | grep -v 'move')"
INSTRUCTIONS="$(cat $PUZZLE_FILE | grep 'move')"

# Get the number of crate stacks
# (last character of last line of the crates diagram, after removing spaces)
NUM_STACKS=$(echo $CRATES | tail -n 1 | tr -d ' ' | grep -o .$)

# Create "stack files" in stacks/
gen_stacks() {
    mkdir -p stacks
    for ((s=0;s<NUM_STACKS;s++)); do
        # Get the character column of the stack from the input
        # The 1st columm is at pos. 2; the 2nd+ columns are 4 pos. after the previous
        # i.e. 2 + $s * 4
        STACK_CHAR_COLUMN=$(expr 2 + $s \* 4)

        # Create the "stack file" (stacks/<stack>)
        # Remove last line (numbers), cut the stack column, remove new lines
        echo "$CRATES" | head -n -1 | cut -c $STACK_CHAR_COLUMN | awk NF > stacks/$(expr $s + 1)
    done
}

# PART 1

# Define standard stack operations based on our "stack files"
# (i.e. push <stack> <value>; pop <stack>)
push() { STACK=stacks/$1; shift; printf "$@\n$(cat $STACK)" > $STACK; }
pop() { STACK=stacks/$1; cat $STACK | head -n 1; sed -i '1d' $STACK; }

# Generate stacks
gen_stacks

# Parse each instruction
IFS='
'
for instruction in $INSTRUCTIONS; do
    # Extract variables from instruction
    # e.g. from "move 1 from 2 to 1"
    MOVE=$(echo $instruction | cut -d ' ' -f 2)
    FROM=$(echo $instruction | cut -d ' ' -f 4)
    TO=$(echo $instruction | cut -d ' ' -f 6)

    for ((j=0;j<MOVE;j++)); do
        # Pop FROM
        CRATE=$(pop $FROM)
        echo -n . # Progress
        # Push TO
        push $TO $CRATE
    done
done

echo && echo -n "Part 1: "
for stack in $(ls stacks/*); do
    echo -n $(cat $stack | awk NF | head -n 1)
done
echo

# PART 2

# Define special stack operations based on our "stack files"
# (i.e. push <stack> <moves (elements)>; pop <stack> <moves (elements)>)
# (for push_9001, seperate <moves> argument(s) with newlines)
push_9001() { STACK=stacks/$1; shift; printf "$(echo $@ | sed 's/\s/\n/g')\n$(cat $STACK)" > $STACK; }
pop_9001() { STACK=stacks/$1; cat $STACK | head -n $2; sed -i "1,${2}d" $STACK; }

# Generate stacks
gen_stacks

IFS='
'
for instruction in $INSTRUCTIONS; do
    # Extract variables from instruction
    # e.g. from "move 1 from 2 to 1"
    MOVE=$(echo $instruction | cut -d ' ' -f 2)
    FROM=$(echo $instruction | cut -d ' ' -f 4)
    TO=$(echo $instruction | cut -d ' ' -f 6)
    
    # Pop FROM
    CRATE=$(pop_9001 $FROM $MOVE)
    echo -n . # Progress
    # Push TO
    push_9001 $TO $CRATE
done

echo && echo -n "Part 2: "
for stack in $(ls stacks/*); do
    echo -n $(cat $stack | awk NF | head -n 1)
done
echo