from random import randint
a = [randint(0, 100) for _ in range(randint(5, 20))]
s = {}
for i in range(len(a)):
    if str(a[i]) not in s:
        s[str(a[i])] = a[i]
print(s)