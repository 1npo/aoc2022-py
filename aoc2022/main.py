import os
import argparse
from importlib import import_module
from pkgutil import iter_modules
from datetime import datetime
from aoc2022 import days


day_numbers = [i for i in range(1, int(datetime.now().strftime("%d")) + 1)]
input_files = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'days/inputs')


def run_solver(day: int, mod_path: str):
    print(f'[!] December {day}...')
    mod = import_module(mod_path)
    mod.solve(os.path.join(input_files, f'day{day}.txt'))


def main():
    # Get parameters from user
    parser = argparse.ArgumentParser(description='Advent of Code 2022')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-d', '--day', action='store', type=int)
    parser.add_argument('-p', '--pandas', action='store_true')
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
        print(f'[!] Solving the puzzle for December {args.day}...')
        if args.pandas:
            run_solver(args.day, f'aoc2022.days.day{args.day}_pd')
        else:
            run_solver(args.day, f'aoc2022.days.day{args.day}')
        

if __name__ == '__main__':
    main()

