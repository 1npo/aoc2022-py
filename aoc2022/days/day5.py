# Some people, when confronted with a problem, think “I know, I'll use
# regular expressions.” Now they have two problems.
import re
from collections import deque 
from copy import deepcopy


STACK_ITEM_P = re.compile('\[([A-Z])\][ \n]')


def parse_input(filepath: str) -> tuple:
    """ 😔 """
    with open(filepath, 'r') as f:
        content = f.readlines()

    deques = {}
    instructions = []
    
    # Get the stacks and instructions
    for line in content:
        segments = [(line[i:i+4]) for i in range(0, len(line), 4)]

        if segments[0] != 'move':
            if len(set(segments)) != 1:
                for i, segment in enumerate(segments, start=1):
                    if STACK_ITEM_P.match(segment):
                        stack_item = STACK_ITEM_P.match(segment).group(1)
                        if i not in deques:
                            deques.update({i: deque([stack_item])})
                        else:
                            deques[i].append(stack_item)
            else:
                continue
        else:
            instructions.append(line)

    for k in deques.keys():
        deques[k].reverse()

    return (deques, instructions)


def rearrange_deques(deques: dict, instruction: str, part: int):
    count, src, dst = re.findall(r'\d+', instruction)
    
    count = int(count)
    src = int(src)
    dst = int(dst)
    
    if part == 2 and count > 1:
        deque_cache = deque()
        for i in range(1, count+1):
            top_of_src = deques[src].pop()
            deque_cache.append(top_of_src)

        for i in range(1, count+1): 
            deques[dst].append(deque_cache.pop())
    else:
        for i in range(1, count+1):
            deques[dst].append(deques[src].pop())


def solve(filepath: str):
    deques, instructions = parse_input(filepath)
    deques2 = deepcopy(deques)

    # PART 1

    top_items_part1 = []

    for inst in instructions:
        rearrange_deques(deques, inst, 1)
    
    for i in range(1, len(deques)+1):
        top_items_part1.append(deques[i][-1])

    # PART 2

    top_items_part2 = []
    
    for inst in instructions:
        rearrange_deques(deques2, inst, 2)

    for i in range(1, len(deques2)+1):
        top_items_part2.append(deques2[i][-1])

    print(f'[+] Part 1 solution: {"".join(top_items_part1)}')
    print(f'[+] Part 2 solution: {"".join(top_items_part2)}')

