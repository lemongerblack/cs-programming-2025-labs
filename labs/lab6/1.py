print("Перевод времени без смс и регистрации(:")
print("пример ввода: 10h m", "c - секунды", "m - минуты", "h - часы", sep="\n")
a = input("Введите время для перевода_").split()
hmc = [1, 60, 3600]
h, m, c = 0, 1, 2
t = int(a[0][:-1])
if eval(a[0][-1]) <= eval(a[-1]) and a[0][-1] != "m":
    print(t * hmc[eval(a[-1])])
elif a[0][-1] == "m":
    if a[-1] == "h":
        print(t / 60)
    else:
        print(t * 60)
else:
    hmc = hmc[::-1]
    print(t / hmc[eval(a[-1])])