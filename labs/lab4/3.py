while True:
    old = input("Введите возрост собаки в годах:")
    if old.isdigit:
        int(old)
        print(old * 10.5 if 1 <= old <= 2 else 21 + (old - 2) * 4)
        break
    else:
        print("Ошибка: возраст должен быть не меньше 1" if int(old) < 1 else "Введите число -_-")
