s = input("Введите два числа через пробел:")
while True:
    if s in "абвгдеёжзиклмнопрстуфхцчшщъьэюя":
        break
    else:
        s1, s2 = int(s.split()[0]), int(s.split()[1])
        print(s1 + s2)
        s = input("Введите два числа через пробел:")