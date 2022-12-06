def find_marker(content: str, marker_size: int) -> int:
    for i in range(0, len(content)):
        if len(set(content[i:i+marker_size])) == marker_size:
            return i + marker_size

def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = f.readlines()[0]

        print(f'[+] Part 1 solution: {find_marker(content, 4)}')
        print(f'[+] Part 2 solution: {find_marker(content, 14)}')

