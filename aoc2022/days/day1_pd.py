import pandas as pd


def solve(filepath: str):
    # Load the data as a single-column dataframe, and replace blank lines with 0s
    content = pd.read_csv(filepath,
            names=['calories_list'],
            header=None,
            skip_blank_lines=False,
            dtype='Int64').replace([pd.NA], [0])
    
    # Add a column that assigns a unique ID to each elf
    content['elf_id'] = ((content['calories_list'] == 0).cumsum() + 1).astype('Int64')

    # Create an index of each elf and the sum of calories they're holding
    elf_calories_index = content.groupby(['elf_id']).sum()
    
    # Find the elf holding the most calories, and return the sum of those calories
    most_calories = elf_calories_index.max()[0]

    # Find the sum of calories held by the top three elves
    top_three_most_calories = elf_calories_index.nlargest(3, ['calories_list']).sum()[0]

    print(f'[+] Part 1 answer: {most_calories}')
    print(f'[+] Part 2 answer: {top_three_most_calories}')


if __name__ == '__main__':
    solve('inputs/day1.txt')

