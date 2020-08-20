import re
import json

filename = 'jawiki-country.json'
with open(filename, mode='r') as f:
    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            text_uk = line['text']
            break
# テンプレートの抽出
pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
template = re.findall(pattern, text_uk, re.MULTILINE + re.DOTALL)
print(template)

# フィールド名と値を辞書オブジェクトに格納
pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
for k, v in result.items():
    print(k + ': ' + v)
