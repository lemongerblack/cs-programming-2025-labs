a = eval("[" + input("Введите имя и 3 оценки таким образом через запятую: ('Анна', [5, 4, 5])_ ") + "]")
s = {}
for i in a:
    if i[0] not in s:
        s[i[0]] = float(str(sum(i[1]) / len(i[1]))[:3])
print(f"{max(s, key = s.get)} имеет наивысший средний балл: {s.get(max(s, key = s.get))}")