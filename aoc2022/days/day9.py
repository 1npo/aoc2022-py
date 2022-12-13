from copy import deepcopy

# https://medium.com/@ojhasaurabh2099/traversing-a-grid-using-dfs-ac7a391f7af8
DIR_COORDS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


def move_head(head: dict, direction: str):
    head['cur_pos'][0] += DIR_COORDS[direction][0]
    head['cur_pos'][1] += DIR_COORDS[direction][1]


def move_tail(head: dict, tail: dict, direction: str):
    diff_x = head['cur_pos'][0] - tail['cur_pos'][0]
    diff_y = head['cur_pos'][1] - tail['cur_pos'][1]
    
    if abs(diff_x) == 2 and not diff_y:
        tail['cur_pos'][0] += 1 if diff_x > 0 else -1
    elif abs(diff_y) == 2 and not diff_x:
        tail['cur_pos'][1] += 1 if diff_y > 0 else -1
    elif (abs(diff_y) == 2 and abs(diff_x) in (1, 2)) or \
    (abs(diff_x) == 2 and abs(diff_y) in (1,2)):
        tail['cur_pos'][0] += 1 if diff_x > 0 else -1
        tail['cur_pos'][1] += 1 if diff_y > 0 else -1

    tail_x = tail['cur_pos'][0]
    tail_y = tail['cur_pos'][1]

    tail['visited'].add((tail_x, tail_y))


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [tuple(line.strip().split()) for line in f]
        
        head = {'cur_pos': [0, 0]}
        tail = {'cur_pos': [0, 0], 'visited': set()}
        
        head2 = deepcopy(head) 
        tails = [deepcopy(tail) for _ in range(9)]
        
        for inst in content:
            direction = inst[0]
            num_steps = int(inst[1])
            
            # Part 1
            for _ in range(num_steps):
                move_head(head, direction)
                move_tail(head, tail, direction)
        
            # Part 2
            for _ in range(num_steps):
                move_head(head2, direction)
                move_tail(head2, tails[0], direction)
                for i in range(len(tails)):
                    if i != 0:
                        move_tail(tails[i-1], tails[i], direction)

        print(f'[+] Part 1 solution: {len(tail.get("visited"))}')
        print(f'[+] Part 2 solution: {len(tails[8].get("visited"))}')

