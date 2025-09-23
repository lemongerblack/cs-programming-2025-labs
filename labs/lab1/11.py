print("Введите 3 числа через запятую. Пример: x,y,z")
s = input()
a, b, c = (int(x) for x in s.split(","))
print(f"Результат вычислений: {(a + c) // b}")