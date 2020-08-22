ans = defaultdict(int)
for sentence in sentences:
    if '猫' in [morph['surface'] for morph in sentence]:
        for morph in sentence:
            if morph['pos'] not in ['記号', '助詞', '助動詞']:
                ans[morph['base']] += 1
del ans['猫']
ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)

keys = [a[0] for a in ans[0:10]]
values = [a[1] for a in ans[0:10]]
plt.figure(fignize=(8, 4))
plt.bar(keys, values)
plt.show()
