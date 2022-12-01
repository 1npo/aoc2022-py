def sum_elf_calories(aoc_input: list):
    calories = 0
    for line in aoc_input:
        if line:
            calories += int(line)
        else:
            yield calories
            calories = 0


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [line.strip() for line in f]
        most_calories = [count for count in sum_elf_calories(content)]
        top_three_most_calories = sum(sorted(most_calories, reverse=True)[:3])
        
        print(f'[+] Part 1 answer: {max(most_calories)}')
        print(f'[+] Part 2 answer: {top_three_most_calories}')


if __name__ == '__main__':
    solve('inputs/day1.txt')

