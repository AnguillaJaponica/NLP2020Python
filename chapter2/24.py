import re
import json

filename = 'jawiki-country.json'
with open(filename, mode='r') as f:
    for line in f:
        line = json.loads(line)
        if line['title'] == 'イギリス':
            text_uk = line['text']
            break
pattern = r'\[\[ファイル:(.+?)\|'
result = '\n'.join(re.findall(pattern, text_uk))
print(result)
