import os
import argparse
import requests
from importlib import import_module
from pkgutil import iter_modules
from datetime import datetime
from aoc2022 import days


AOC_YEAR = 2022
day_numbers = [i for i in range(1, int(datetime.now().strftime("%d")) + 1) if i <= 25]
input_files = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'days/inputs')


def get_input(year: str, day: str):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookie = os.environ['AOC_SESSION_COOKIE']
    headers = {
        'User-Agent': 'Nick <http://github.com/1npo/aoc2022>',
        'cookie': f'session={cookie}' }
    output_file = os.path.join(input_files, f'day{day}.txt')

    with open(output_file, 'w') as f:
        f.write(requests.get(url, headers=headers).text)
    
    print(f'[!] Downloaded your input for day {day}')


def run_solver(day: int, mod_path: str):
    if not os.path.exists(f'{input_files}/day{day}.txt'):
        print(f'[!] Input for day {day} wasn\'t found. Downloading...')
        get_input(AOC_YEAR, day)

    print(f'[!] Solving the puzzle for December {day}...')
    mod = import_module(mod_path)
    mod.solve(os.path.join(input_files, f'day{day}.txt'))


def main():
    # Get parameters from user
    parser = argparse.ArgumentParser(description='Advent of Code 2022')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-d', '--day', action='store', type=int)
    parser.add_argument('-p', '--pandas', action='store_true')
    parser.add_argument('-t', '--test', action='store_true')

    args, _ = parser.parse_known_args()

    # Build an index of each day and its associated modules
    py_modules = {}
    pd_modules = {}
    for (_, module_name, _) in iter_modules(days.__path__):
        if '_pd' in module_name:
            day_number = int(module_name.split('day')[1].split('_pd')[0])
            pd_modules.update({day_number: module_name})
        else:
            day_number= int(module_name.split('day')[1])
            py_modules.update({day_number: module_name})
    
    # Warn the user to pick either 'all' or 'day', but not both
    if args.all and args.day:
        print('[-] ERROR: Please choose either "all" or "days", not both!')
        exit(1)
    
    # Solve all the puzzles
    elif args.all:
        print('[!] Solving the puzzle for all days...')
 
        if args.pandas:
            print('[!] Using the Pandas solution...')
            for day, mod_name in pd_modules.items():
                run_solver(day, f'aoc2022.days.day{day}_pd')
        else:
            for day, mod_name in py_modules.items():
                run_solver(day, f'aoc2022.days.day{day}')

    # Solve the puzzle for a given day
    elif args.day:
        if int(args.day) not in day_numbers:
            print(f'[-] Can\'t sole the puzzle for this day. Wait until December {day}!')
            exit(1)

        if args.pandas:
            run_solver(args.day, f'aoc2022.days.day{args.day}_pd')
        else:
            run_solver(args.day, f'aoc2022.days.day{args.day}')
    
    if args.test:
        print(f'[?] DEBUG: {day_numbers=}')
        print(f'[?] DEBUG: {input_files=}')


if __name__ == '__main__':
    main()

