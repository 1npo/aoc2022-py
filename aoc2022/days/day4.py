def range_to_set(elf: list) -> set:
    return set([i for i in range(int(elf[0]), int(elf[1]) + 1)])


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [line.strip().split(',') for line in f]
        
        part1_count = 0
        part2_count = 0

        for pair in content:
            elf1 = range_to_set(pair[0].split('-'))
            elf2 = range_to_set(pair[1].split('-'))

            if elf1.issubset(elf2) or elf2.issubset(elf1):
                part1_count += 1
            
            if elf1 & elf2:
                part2_count += 1

        print(f'[+] Part 1 solution: {part1_count}')
        print(f'[+] Part 2 solution: {part2_count}')


