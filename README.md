# Advent of Code 2022 (Python)

## Install

```
% git clone https://github.com/1npo/aoc2022-py.git
% cd aoc2022-py
% pip install .
```

## Show solutions

#### For all days

Use the `--all` flag (or `-a` for short), eg:

```
% aoc2022 -a
[!] Solving the puzzle for all days.
[!] December 1...
[+] Part 1 answer: 69795
[+] Part 2 answer: 208437

...
```

#### For a given day

Use the `--day` flag (or `-d` for short), and provide a day number (1-31), eg:

```
% aoc2022-py -d 1
[!] Solving the puzzle for December 1...
[+] Part 1 answer: 69795
[+] Part 2 answer: 208437
```

## Add Solutions

(***NOTE***: N = the day in December)

1. Save the puzzle input in `aoc2022/days/inputs/` with the filename `dayN.txt`.
3. Write a module in `aoc2022/days/` that...
	- Has the filename `dayN.py` 
	- Includes a `solver()` function that takes a file path (`str`) argument
4. Implement the logic for solving the puzzle in `solver()`
5. Solve the puzzle with `aoc2022-py -d N`
6. Profit!

