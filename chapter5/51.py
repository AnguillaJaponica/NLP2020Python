import string
import re
import pandas as pd


def preprocessing(text):
    table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(table)  # 記号をスペースに置換
    text = text.lower()  # 小文字化
    text = re.sub('[0-9]+', '0', text)  # 数字列を0に置換

    return text

df = pd.concat([train, valid, text], axis=0)
df.reset_index(drop=True, inplace=True)

df['TITLE'] = df['TITLE'].map(lambda x: preprocessing(x))
print(df.head())
