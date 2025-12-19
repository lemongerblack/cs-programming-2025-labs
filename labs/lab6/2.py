print("расчет прибыли от вклада без смс и регистрации(:")
print("пример ввода: 100000 3", "Первое число это сумма вклада, а второе это срок вклада в годах", sep="\n")
pr = 0
def f(s, y):
    if s < 30000:
        print("не достаточная сумма вклада")
    else:
        if (s // 10000 * 0.3) > 5:
            pr = 5
        else:
            pr = s // 10000 * 0.3
    
    if y <= 3:
        pr += 3
    elif 4 <= y <= 6:
        pr += 5
    else:
        pr += 2
    
    return pr

        
a = input("Введите сумму и срок для перевода_").split()

p = f(int(a[0]), int(a[1]))
smm = int(a[0])
sm = smm
for _ in range(int(a[1])):
    sm += (sm / 100) * p
print(sm - smm, p)