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


def split_file(n):
    tmp = df.reset_index(drop=False)
    df_cut = pd.qcut(tmp.index, N, labels=[i for i in range(n)])
    df_cut = pd.concat([df, pd.Series(df_cut, name='sp')], axis=1)

    return df_cut


df_cut = split_file(10)
print(df_cut['sp'].value_counts())
