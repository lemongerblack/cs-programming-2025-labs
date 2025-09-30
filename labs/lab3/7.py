s = input("введите строку:")
snew = ""
for i in range(len(s)):
    snew += (s[i] + str(i+1))
print(snew)