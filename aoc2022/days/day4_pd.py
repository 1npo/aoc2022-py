# INCOMPLETE - WIP

import pandas as pd


def expand_df(df: pd.DataFrame, name: str) -> pd.DataFrame:
    df[[f'{name}_start', f'{name}_end']] = df[name].str.split('-', expand=True)
    return df


def solve(filepath: str):
    content = pd.read_csv(filepath,
            names=['elf1', 'elf2'],
            header=None)
    
    elf1_df = expand_df(content[['elf1']], 'elf1')
    elf2_df = expand_df(content[['elf2']], 'elf2')

    print(elf1_df)
    print(elf2_df)
    
    print(content)

