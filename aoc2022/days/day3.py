from string import ascii_letters


alphabet = [c for c in list(ascii_letters)]
letter_priorities = {c: p for p, c in enumerate(alphabet, start=1)}


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [line.strip() for line in f]
        
        part1_sum = []
        part2_sum = []

        group_counter = 0
        group_cache = []

        for rucksack in content:
            compartment_1 = set(rucksack[:len(rucksack)//2])
            compartment_2 = set(rucksack[len(rucksack)//2:])

            duplicates = list(compartment_1 & compartment_2)
            part1_sum.extend(duplicates)
        
            group_counter += 1
        
            if group_counter % 3:
                group_cache.append(set(rucksack))
            else:
                group_cache.append(set(rucksack))
                badge = list(group_cache[0] & group_cache[1] & group_cache[2])[0]
                part2_sum.append(badge)

                group_counter = 0
                group_cache = []
        
        part1_sum = sum([letter_priorities[d] for d in part1_sum])
        part2_sum = sum([letter_priorities[d] for d in part2_sum])

        print(f'[+] Part 1 solution: {part1_sum}')
        print(f'[+] Part 2 solution: {part2_sum}')
