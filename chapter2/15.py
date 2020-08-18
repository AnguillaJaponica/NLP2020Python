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


def output_tail(n):
    print(df.tail(n))


output_tail(5)
