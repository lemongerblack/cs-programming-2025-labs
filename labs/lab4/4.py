a = input("Введите число для проверки делимости на 6: ")
sm = 0
for i in a:
    sm += int(i)

if sm % 3 == 0 and int(a[-1]) % 2 == 0:
    print("Делится(;")
else:
    print("Не делиться-_-")

#print("Делится(;" if sm % 3 == 0 and int(a[-1]) % 2 == 0 else "Не делиться-_-")
