import pandas as pd
df = pd.read_table(
    './popular-names.txt',
    header=None,
    sep='\t',
    names=[
        'name',
        'sex',
        'number',
        'year'])


def output_head(n):
    print(df.head(n))


output_head(5)
