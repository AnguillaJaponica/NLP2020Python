ans = set()
for sentence in sentences:
    for i in range(1, len(sentence) - 1):
        if sentence[i - 1]['pos'] == '名詞' and sentence[i]['surface'] == 'の' and sentence[i+1]['pos'] == '名詞':
          ans.add(sentence[i-1]['surface'] + sentence[i]['surface'] + sentence[i+1]['surface'])
print(f'「名詞+の+名詞」の種類: {len(ans)}\n')
print('---サンプル---')
for n in list(ans)[:10]:
  print(n)