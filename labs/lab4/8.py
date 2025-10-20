smp = float(input("Введите сумму покупки:"))
sk = [0, 5, 10, 15]
pr = [smp < 1000, 1000 <= smp <= 5000, 5000 <= smp <= 10000, smp > 10000].index(True)
print(f"Ваша скидка: {sk[pr]}")
print(f"К оплате: {smp - (smp / 100 * sk[pr])}")