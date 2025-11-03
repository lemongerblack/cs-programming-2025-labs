def OldD(o):
    if o <= 2: return 10.5 * o
    if o > 2: return 21 + ((o - 2) * 4)

while True:
    otvet = input("Введите возрост собаки в годах:")
    if otvet.isdigit():
        if int(otvet) < 1 or int(otvet) > 22:
            print("Ошибка: нужно ввести возрост от 1 до 22 включительно")
        else:
            print(OldD(int(otvet)))
            break
    else:
        print("Ошибка: Введите возрост используя цифры (:")