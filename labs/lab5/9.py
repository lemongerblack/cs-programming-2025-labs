a = input("введи слова через пробел__").split()
s = {}
for i in a:
    if i[0] not in s:
        s[i[0]] = [i]
    else:
        s[i[0]].append(i)
print(s)