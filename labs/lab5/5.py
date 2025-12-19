a = input("введите список нименование товара и его ценну. Пример: картошка 50 лук 15___").split()
s = {}
for i in range(0, len(a) - 1, 2):
    if a[i] not in s:
        s[a[i]] = int(a[i + 1])
print(f"Максимальная цена у товара: {max(s, key = s.get)}, цена: {s.get(max(s, key = s.get))}")
print(f"Минимальная цена у товара: {min(s, key = s.get)}, цена: {s.get(min(s, key = s.get))}")