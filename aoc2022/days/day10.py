def render(screen: list):
    for i in range(0, 201, 40):
        print(''.join(screen[i: i+40]))


def draw_pixel(screen: list, cycle: int, X: int):
    sprite_pos = [X-1, X, X+1]

    if (cycle-1) % 40 in sprite_pos:
        screen[cycle-1] = '▓'


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [tuple(line.strip().split()) for line in f]
        
        X = 1
        cycle = 0
        signal = 0
        screen = ['░'] * 40 * 6

        for line in content:
            if line[0] == 'noop':
                cycle += 1
                draw_pixel(screen, cycle, X)

            if line[0] == 'addx':
                for _ in range(2):
                    cycle += 1
                    draw_pixel(screen, cycle, X)
                    if cycle in range(20, 221, 40):
                        signal += (X * cycle)
                        

                X += int(line[1])

        print(f'[+] Part 1 solution: {signal}')
        print(f'[+] Part 2 solution is rendering...')
        render(screen)

