def isps(ch):
    p = ["состовное число", "простое число"]
    f = 0
    for i in range(1, int(ch)+ 1):
        if int(ch) % i == 0:
            f += 1
    return p[(f == 2)]

while True:
    ch = input("Введите неотрицательное число: ")
    if ch.isdigit():
        print(isps(ch))
        break
    elif ch[0] == "-" and ch[1:].isdigit():
        print("Введите неотрицательное число (':")
    else:
        print("Введите число -_-")
