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

otvet = []

if "a" not in mask:
      otvet.append("строчные буквы")
if "A" not in mask:
      otvet.append("заглавные буквы")
if "0" not in mask:
      otvet.append("числа")
if "_" not in mask:
      otvet.append("специальные символы")

print("Надажный пароль" if len(otvet) == 0 else "Ненадежный пароль отсутствуют: " + ", ".join(otvet))