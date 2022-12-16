import re
from loguru import logger
from math import prod

LOG_FILE='/tmp/aoc-day11.log'
LOG_FMT='<green>[{function: <17}]</green> {message}'
logger.remove()
logger.add(LOG_FILE, format=LOG_FMT, level='DEBUG')


# This is the real monkey business right here
MONKEY_P = re.compile('^Monkey (\d):')
START_ITEMS_P = re.compile('^Starting items: ((\d+[, ]*)*)')
OPERATION_P = re.compile('^Operation: new = (old*|\d+)+ (\*|/|-|\+)+ (old*|\d+)+')
TEST_CASE_P = re.compile('^Test: divisible by (\d+)')
TEST_RES_P = re.compile('^If (true|false)+: throw to monkey (\d)+')


class Monkey:
    def __init__(self):
        self.monkey_num = 0
        self.items = []
        self.operation = None
        self.operand1 = None
        self.operand2 = None
        self.test_case = None
        self.test_res_true = 0
        self.test_res_false = 0
        self.total_inspections = 0
        self.part = 0
    
    def __repr__(self):
        return (f'monkey_num={self.monkey_num}, items={self.items}, operation={self.operation}, '
                f'operand1={self.operand1}, operand2={self.operand2}, test_case={self.test_case},'
                f'test_res_true={self.test_res_true}, test_res_false={self.test_res_false}, '
                f'total_inspections={self.total_inspections}')

    def throw(self, mod: int = None) -> dict:
        self.total_inspections += len(self.items)

        for item in self.items:
            updated_item = self.perform_operation(item)
            
            if mod:
                updated_item %= mod
            
            test_result = self.test_worry(updated_item)
            
            if test_result == True:
                catcher = int(self.test_res_true)
            elif test_result == False:
                catcher = int(self.test_res_false)

            yield catcher, updated_item
        
        self.items = []

    def catch(self, item: int):
        self.items.append(item)

    def perform_operation(self, item: int) -> int:
        if self.operand1 == 'old':
            operand1 = int(item)
        else:
            operand1 = int(self.operand1)

        if self.operand2 == 'old':
            operand2 = int(item)
        else:
            operand2 = int(self.operand2)
        
        if self.operation == '*':
            if self.part == 1:
                return (operand1 * operand2) // 3
            elif self.part == 2:
                return operand1 * operand2
        
        if self.operation == '+':
            if self.part == 1:
                return (operand1 + operand2) // 3
            elif self.part == 2:
                return operand1 + operand2
    
    def test_worry(self, item: int) -> bool:
        return True if item % int(self.test_case) == 0 else False


def build_monkey_troop(content: list, part: int) -> list:
    monkey = Monkey()
    monkey_troop = []

    for line in content:
        if monkey_num := MONKEY_P.findall(line):
            monkey.monkey_num = monkey_num[0]

        if items := START_ITEMS_P.findall(line):
            monkey.items = items[0][0].split(', ')

        if operation := OPERATION_P.findall(line):
            monkey.operation = operation[0][1]
            monkey.operand1 = operation[0][0]
            monkey.operand2 = operation[0][2]

        if test_case := TEST_CASE_P.findall(line):
            monkey.test_case = test_case[0]

        if test_res := TEST_RES_P.findall(line):
            if test_res[0][0] == 'true':
                monkey.test_res_true = test_res[0][1]
            elif test_res[0][0] == 'false':
                monkey.test_res_false = test_res[0][1]
        
        if not line:
            monkey_troop.append(monkey)
            monkey = Monkey()
    
    for monkey in monkey_troop:
        monkey.part = part

    return monkey_troop


def monkey_in_the_middle(monkey_troop: list, rounds: int):
    monkey_business_levels = []
    
    mod = prod([int(monkey.test_case) for monkey in monkey_troop]) if rounds == 10_000 else None

    for _ in range(rounds):
        for monkey in monkey_troop:
            for catcher, item in monkey.throw(mod):
                monkey_troop[catcher].catch(item)
    
    for monkey in monkey_troop:
        monkey_business_levels.append(monkey.total_inspections)

    monkeys = sorted(monkey_business_levels)
    return monkeys[-2] * monkeys[-1]


def solve(filepath: str):
    with open(filepath, 'r') as f:
        content = [line.strip() for line in f]
        content.append('')
        
        # I had to cheat to solve part 2 😭😭😭
        # Thanks camaron-ai for the explanation and Nuhser for the example
        # https://github.com/camaron-ai/adventofcode-2022/tree/main/day11
        # https://github.com/Nuhser/Advent-of-Code/blob/master/2022/day11.py

        monkey_troop1 = build_monkey_troop(content, 1)
        monkey_troop2 = build_monkey_troop(content, 2)
        
        print(f'[+] Part 1 solution: {monkey_in_the_middle(monkey_troop1, 20)}')
        print(f'[+] Part 2 solution: {monkey_in_the_middle(monkey_troop2, 10000)}')

