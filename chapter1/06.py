def ngram(n, str):
    return list(zip(*[str[i:] for i in range(n)]))


str1 = 'paraparaparadise'
str2 = 'paragraph'

x = set(ngram(2, str1))
y = set(ngram(2, str2))
union = x | y
intersection = x & y
diff = x - y

print('X:', x)
print('Y:', y)
print('和集合:', union)
print('積集合:', intersection)
print('差集合:', diff)
print('xにseが含まれるか:', {('s', 'e')} <= x)
print('Yにseが含まれるか:', {('s', 'e')} <= y)
