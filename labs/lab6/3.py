while True:
    d = input("Введите диапозон чисел через пробел").split()
    try:
        if (d[0][0] == "-") or (d[1][0] == "-"):
            print("В диапозоне не могут быть отрицательные числа")
        elif int(d[0]) > int(d[1]):
            print("Диапозон должен написан в порядке возростания")
        else:
            o = []
            for i in range(int(d[0]), int(d[1])):
                k = 0
                for j in range(1, i + 1):
                    if i % j == 0:
                        k += 1
                if k == 2:
                    o.append(i)
            if len(o) == 0:
                print("Ошибка, В диапозоне отстутствуют простые числа.")
            else:
                print(o)
                break
    except:
        print("Введите числа")
