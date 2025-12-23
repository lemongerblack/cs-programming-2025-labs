s = input("Введите строку для проверки на палиндромность_").lower().split()
print("да" if "".join(s) == "".join(s)[::-1] else "нет")