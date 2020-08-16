import re

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'
str = re.sub(r'[,\.]', '', str)
words = str.split()
ans = [len(w) for w in words]
print(ans)
