while True:
    old = input("Введите возрост собаки в годах:")
    if old.isdigit:
        int(old)
        print(old * 10.5 if 1 <= old <= 2 else 21 + (old - 2) * 4)
        break
        if old < 1:
            print("ведите число больше 0")
    else:
        print("Введите число -_-")
