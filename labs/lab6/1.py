print("Перевод времени без смс и регистрации(:")
print("пример ввода: 10h m", "c - секунды", "m - минуты", "h - часы", sep="\n")
a = input("Введите время для перевода_").split()
h, m, c = 1, 60, 3600
t = int(a[0][:-1])
if eval(a[0][-1]) < eval(a[-1]):
    print(eval(a[0][-1]) * eval(a[-1]))
elif eval(a[0][-1]) == eval(a[-1]):
    print(a[0][-1])
else:
    print(eval(a[0][-1]) / eval(a[-1]))
print(a, eval(a[0][-1]), eval(a[-1]))