#ch = sorted(map(int, (input("Введите три чесла через прообел: ")).split()))
#print(ch[0])

ch = input("Введите три чесла через пробел: ")
a = [int(i) for i in ch.split()]
for i in range(len(a) - 1):
    f = 0
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            f += 1
            a[j], a[j + 1] = a[j + 1], a[j]
    if f == 0:
        break
print(a[0])