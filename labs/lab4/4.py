a = input("Введите число для проверки делимости на 6: ")
sm = 0
for i in a:
    sm += int(i)

if sm % 3 == 0 and int(a[-1]) % 2 == 0:
    print("Делиться(;")
else:
    print("Не делиться-_-")