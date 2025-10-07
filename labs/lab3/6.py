n = int(input("введите число, до которого расчитаем числа фибоначи:"))
i, fa = 0, [0, 1, 1]
f = 0
while f < n and f != n:
    if i >= 3:
        f = fa[i-2] + fa[i-1]
        if f > n:
            break
        fa.append(f)
        print(f)
    elif f <= 1:
        f = fa[i]
        print(f)
    i += 1