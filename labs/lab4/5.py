p = input("Введите пароль: ")
mask = ""
if len(p) >= 8:
    for i in range(len(p)):
            if 96 < ord(p[i]) < 123:
                  mask += "a"
            elif 64 < ord(p[i]) < 91:
                  mask += "A"
            elif p[i].isdigit():
                  mask += "0"
            else:
                  mask += "_"
if "a" in mask and "A" in mask and "0" in mask and "_" in mask:
      print("Пароль надежный")
else:
      print("Пароль ненадежный: отсутствуют заглавные буквы, числа и специальные символы")
print(mask)