import os
import argparse
from importlib import import_module
from pkgutil import iter_modules
from datetime import datetime
from aoc2022 import days


day_numbers = [i for i in range(1, int(datetime.now().strftime("%d")) + 1)]
input_files = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'days/inputs')

def main():
    # Get parameters from user
    parser = argparse.ArgumentParser(description='Advent of Code 2022')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-d', '--day', action='store', type=int)
    args, _ = parser.parse_known_args()

    # Build an index of each day and its associated module
    modules = {} 
    for (_, module_name, _) in iter_modules(days.__path__):
        day_number = int(module_name.split('day')[1])
        modules.update({day_number: module_name})
    
    # Run one or all of the modules, based on the flag provided by the user
    if args.all and args.day:
        print('[-] ERROR: Please choose either "all" or "days", not both!')

    elif args.all:
        for day, mod_name in modules.items():
            print(f'[!] Solving the puzzle for December {day}...')
            mod = import_module(f'aoc2022.days.{mod_name}')
            mod.solve(os.path.join(input_files, f'day{day}.txt'))
    
    elif args.day:
        print(f'[!] Solving the puzzle for December {args.day}...')
        mod = import_module(f'aoc2022.days.day{args.day}')
        mod.solve(os.path.join(input_files, f'day{args.day}.txt'))

if __name__ == '__main__':
    main()

